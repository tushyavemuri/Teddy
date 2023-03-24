import sys
import signal
import os
import socket
import teddyworker
import logging
import logging.config
from config import *

def main():
  # Logger settings
  logging.config.fileConfig("tedlog.conf")
  logging.getLogger('teddyFileLogger')
  
  looper = True

  def signalHandler(sig, frame):
    global  looper
    looper = False
    sys.exit(0)

  signal.signal(signal.SIGINT, signalHandler)

  # Creating socket instance using IPv4 TCP IP protocol
  try:
    logging.info(f"Creating socket for teddy server: {HOST} on port : {PORT}")
    teddySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    teddySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    teddySocket.bind((HOST,PORT))
  except Exception:
    logging.error(f"Creating socket failed with exception.")
    sys.exit(8)

  # Configuring no.of client to connect at same time
  teddySocket.listen(CLIENTLIMIT)
  try:
    while looper:
        logging.info(f"Teddy is ready to accept connections from buddies.")
        teddy,address = teddySocket.accept()
        logging.info(f"Connection from buddy : {address} has been established.")
        
        logging.info(f"Waiting for request from buddy : {address}")
        request = teddy.recv(1024).decode('utf-8')
        logging.info(f"Received request from buddy :  {address} and the request is : {request}")
      
        try:
          logging.info(f"Teddy worker is working on the request from buddy")
          response = teddyworker.teddyWorker(request)
        except Exception:
          logging.error(f"Teddy workker failed to perform the request with exception.")
          teddy.close()
          sys.exit(8)
        
        logging.info(f"Teddy worker completed task and responding to buddy")
        teddy.send(response.encode('utf-8'))
        logging.info(f"Closing connection with buddy : {address}")
        teddy.close()
  except Exception:
      logging.error(f"Teddy server initiation failed")
      sys.exit(8)

if __name__ == "__main__":
  main()

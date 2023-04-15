import systemutils as SU
import logging

def teddiesWorker(teddy,address):

    logging.info(f"Waiting for request from buddy : {address}")
    request = teddy.recv(1024).decode('utf-8')
    logging.info(f"Received request from buddy :  {address} and the request is : {request}")
    
    logging.info(f"Input request to teddy worker : {request}")
    result = SU.sysUtils(request)

    logging.info(f"Teddy worker completed task and responding to buddy")
    teddy.sendall(result)
    logging.info(f"Closing connection with buddy : {address}")
    teddy.close()

#inRequest = "uptime"
#requestHandler(inRequest)
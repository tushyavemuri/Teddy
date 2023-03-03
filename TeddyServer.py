import socket
import RequestHandler as RH

HOST = '127.0.0.1'  # Need to replace with server IP address
PORT = 52777        # Port number can be changed if it is already used

teddy = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
teddy.bind((HOST,PORT))

while True:
    teddy.listen(1)
    buddy,address = teddy.accept()
    print(f"Connection from {address} has been established.")
    
    request = buddy.recv(1024).decode()
    print(f"Received request from {address}: {request}")

    response = RH.requestHandler(request)
    buddy.send(response.encode())

    buddy.close()
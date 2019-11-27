import socket
import sys
import time
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=input(str("Please enter the ip of server"))
port=1234
client.connect((ip,port))
print("Connected to chat server")
while True:
            incoming_message=client.recv(1024)
            incoming_message=incoming_message.decode()
            print("server:",incoming_message)
            if(incoming_message == "Goodbye"):
                client.close()
            else:
                 message = input(str(">>"))
                 message = message.encode()
                 client.send(message)
                 print("Message has been sent...")

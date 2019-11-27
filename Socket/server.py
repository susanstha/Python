import socket
import sys
import time
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
print("Server will start on host",ip)
port = 1234
address = (ip,port)
server.bind(address)
print("Server done Binding")
print("Server is waiting")
server.listen(2)
conn,addr = server.accept()
print(addr,'Has connected to server and is online')
while True:
            message = input(str(">>"))
            message = message.encode()
            conn.send(message)
            print("Message has been sent...")
            incoming_message = conn.recv(1024)
            incoming_message = incoming_message.decode()
            print("client:", incoming_message)
            if (incoming_message == "bye"):
                message = "Goodbye"
                message = message.encode()
                conn.send(message)
                server.close()

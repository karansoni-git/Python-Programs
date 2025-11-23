import socket

client = socket.socket()

host = socket.gethostbyname(socket.gethostname())
port = 9999

client.connect((host,port))

name = input("Enter Your Name : ")

client.send(name.encode())

print(client.recv(1024).decode())

client.close()
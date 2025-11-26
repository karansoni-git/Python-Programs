import socket

host = socket.gethostbyname(socket.gethostname())
port = 9999

server = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

server.bind((host,port))

while True:
    data,addr = server.recvfrom(1024)
    print("Data : " , data.decode('utf-8'))
    print("Address : " , addr)
    msg = f"hello, {data}"
    msg = msg.encode('utf-8')
    server.sendto(msg,addr)
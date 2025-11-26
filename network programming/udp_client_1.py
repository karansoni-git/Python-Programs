import socket

client = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

host = socket.gethostbyname(socket.gethostname())
port = 9999

addr = (host,port)

while True : 
    data = input("Enter Your Name : ")
    data = data.encode('utf-8')
    
    client.sendto(data,addr)

    data,addr1 = client.recvfrom(1024)
    print("Data : " , data.decode('utf-8'))
    print("addr : " , addr1)



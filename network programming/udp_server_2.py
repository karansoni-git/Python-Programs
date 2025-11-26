import socket

server = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

host = socket.gethostbyname(socket.gethostname())
port = 9999

server.bind((host,port))

while True : 
    clientMsg,addr = server.recvfrom(1024)
    clientMsg = clientMsg.decode('utf-8')
    
    if clientMsg == 'exit':
        server.sendto("exit".encode('utf-8'),addr)
        server.close()
        break
    
    print("Client :" , clientMsg)
    
    serverMsg = input("*Server : ")
    serverMsg = serverMsg.encode('utf-8')
    server.sendto(serverMsg,addr)
    
    
print("Client close the connection!")
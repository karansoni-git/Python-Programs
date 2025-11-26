import socket

client = socket.socket(family=socket.AF_INET , type=socket.SOCK_DGRAM)

host = socket.gethostbyname(socket.gethostname())
port = 9999
addr = (host,port)

while True : 
    clientMsg = input("*Client : ")
     
    clientMsg = clientMsg.encode('utf-8')
    client.sendto(clientMsg,addr)
    
    serverMsg,addr = client.recvfrom(1024)
    serverMsg = serverMsg.decode('utf-8')
    
    if serverMsg == 'exit':
        client.close()
        break
    print("Server :",serverMsg)
    
print("Server close the connection!")
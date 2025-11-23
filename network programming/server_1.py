import socket

server = socket.socket()

server.bind(("localhost",9999))
server.listen(3)
print("server is waiting for client")
while True:
    conn,addr = server.accept()
    print("Connected with : " ,addr)
    conn.send(bytes("welcome to the server","utf-8"))
    conn.close()
    
    
# hostName = socket.gethostname() #return host computer name
# ipAddr = socket.gethostbyname(hostName) #retrun the ip address by host computer name.
# print("host name : ",hostName)
# print("Ip Address : ",ipAddr)
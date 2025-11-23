import socket

server = socket.socket()

host = socket.gethostbyname(socket.gethostname())

port = 9999

server.bind((host,port))

server.listen(3)

print("server is waiting for client")

while True:
    conn,addr = server.accept()
    print("Connection : " ,conn)
    print("Address : " ,addr)
    name = conn.recv(1024).decode()
    print("New Login Of",name ,"In TURBOLAB")
    message = f"Welcome To TURBOLAB {name.upper()}"
    conn.send(message.encode('utf-8'))
    conn.close()
    
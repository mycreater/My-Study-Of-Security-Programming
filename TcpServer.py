import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 50000

sock.bind((host, port))
sock.listen(1)

connection, address = sock.accept()
print(str(address))

while True :
    data = connection.recv(1024)
    if data == b'exit' :
        break
    print(str(data))
    connection.send(data)
    print(str(data))

connection.close()
sock.close()
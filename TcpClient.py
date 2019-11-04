import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 50000

server = (ip, port)
sock.connect(server)

msg = ''
while msg != 'exit' :
    msg = input('-> ')
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(str(data))

sock.close()
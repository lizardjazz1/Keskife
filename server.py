import socket

serv = socket.socket(
    socket.AF_INET, #address family
    socket.SOCK_STREAM, #TCP/IP protocol
)
# IP = socket.gethostbyname(socket.gethostname())
IP = '127.0.0.1'
PORT = 9090
serv.bind((IP, PORT))

serv.listen(10)
print(f'Server is listening on {IP}:{PORT}')

while True:
    user_socket, address = serv.accept()
    user_socket.send("You are connected".encode('utf-8'))
    
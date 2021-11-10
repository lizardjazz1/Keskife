import sys
import random
from Sock import Socket
import asyncio
import time

# IP = socket.gethostbyname(socket.gethostname())
IP = '127.0.0.1'
PORT = 9090

class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()

        self.users = []
        
    def set_up(self):
        self.socket.bind(
            (IP, PORT)
        )
        
        self.socket.listen(5)
        self.socket.setblocking(False)     
        print(f'Server is listening on {IP}:{PORT}')
        
    async def send_data(self, data=None):
        for user in self.users:
            await self.main_loop.sock_sendall(user, data)

    async def listen_socket(self, listened_socket=None):
        if not listened_socket:
            return

        while True:
            try:
                data = await self.main_loop.sock_recv(listened_socket, 1024)
                await self.send_data(data)

            except ConnectionResetError:
                print("Client removed")
                self.users.remove(listened_socket)
                return   
            
    async def accept_sockets(self):
        while True:
            user_socket, address = await self.main_loop.sock_accept(self.socket)
             #Аналогична self.socket.accept() НО асинхронная.
            print(f"User <{address[0]}> connected!")

            self.users.append(user_socket)
            self.main_loop.create_task(self.listen_socket(user_socket))

    async def main(self):
        await self.main_loop.create_task(self.accept_sockets())
        #Создаём задачу на каждую итерацию цикла
        print("мы тут")
if __name__ == '__main__':
    server = Server()
    server.set_up()

    server.start()
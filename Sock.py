import socket
import asyncio #библиотеки на low-level api, приложения на high-level api


class Socket:
    def __init__(self):
        self.socket = socket.socket(
            
            socket.AF_INET, #address family
            socket.SOCK_STREAM, #TCP/IP protocol
        )
        
        self.main_loop = asyncio.new_event_loop()
    
    async def send_data(self, data=None):
        raise NotImplementedError()
    #Проверка на ошибку если не переопределили в других классах
    
    async def listen_socket(self, listened_socket=None):
        raise NotImplementedError()
    
    async def main(self):
        raise NotImplementedError()

    def start(self):
        self.main_loop.run_until_complete(self.main())
        #функция запускающая цикл асинхронно

    def set_up(self):
        raise NotImplementedError()


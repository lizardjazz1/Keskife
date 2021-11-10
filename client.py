import sys
from datetime import datetime
from os import system
import asyncio
from PyQt5 import QtWidgets
from Sock import Socket
import mainmenu
import random
# import time

# IP = input('Введите IP сервера:')
IP = '127.0.0.1'
PORT = 9090

class Client(Socket):
    def __init__(self):
        super(Client, self).__init__()
        self.messages = ""
    
    def set_up(self):
        try:
            self.socket.connect(
            (IP,PORT)
        )
        except ConnectionRefusedError:
            print("Server is offline")
            exit(0)

        self.socket.setblocking(False)
        
    async def listen_socket(self, listened_socket=None):
        while True:
            data = await self.main_loop.sock_recv(self.socket, 1024) #receive
            self.messages += f"{datetime.now().time()}: {data.decode('utf-8')}\n"

            system("cls")
            print(self.messages)

    async def send_data(self, data=None):
        while True:
            data = await self.main_loop.run_in_executor(None, input)
            await self.main_loop.sock_sendall(self.socket, data.encode("utf-8"))
            print('Мы тут')
    async def main(self):
        await asyncio.gather(

            self.main_loop.create_task(self.listen_socket()),
            self.main_loop.create_task(self.send_data())

        )


if __name__ == '__main__':
    client = Client()
    client.set_up()

    client.start()
    
# class Serverapp(QtWidgets.QMainWindow, mainmenu.Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.btn_start.clicked.connect(self.serv)
#         self.btn_con.clicked.connect(self.connect)
#         self.btn_dcon.clicked.connect(self.disconnect)

#     def serv(self):
#         print('serv clicked') 
#         self.con_msg.setText('start server clicked')
#     def connect(self):
#         print('connect clicked')
#         self.btn_con.setEnabled(False)
        
#         while True:
#             time.sleep(2) 
#             with open ('Keskife/quests.csv', 'r', encoding='UTF-8') as file:
#                 lines = file.readlines()
#                 item = random.choice(lines)
#             # print(item)          

#     def disconnect(self):
#         print('disconnect clicked')
#         self.con_msg.setText('disconnect clicked') 
# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     window = Serverapp()
#     window.show()
#     sys.exit(app.exec_())





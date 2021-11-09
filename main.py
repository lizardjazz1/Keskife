from os import startfile
import sys
from PyQt5 import QtWidgets
import socket
import mainmenu
import random
import time

client = socket.socket(
    socket.AF_INET, #address family
    socket.SOCK_STREAM, #TCP/IP protocol
)
PORT = 9090
client.connect((input("Введите IP сервера:"),PORT))
while True:
    data = client.recv(1024) #receive
    print(data.decode('utf-8'))
    
class Serverapp(QtWidgets.QMainWindow, mainmenu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_start.clicked.connect(self.serv)
        self.btn_con.clicked.connect(self.connect)
        self.btn_dcon.clicked.connect(self.disconnect)

    def serv(self):
        print('serv clicked') 
        self.con_msg.setText('start server clicked')
    def connect(self):
        print('connect clicked')
        self.btn_con.setEnabled(False)
        
        while True:
            time.sleep(2) 
            with open ('Keskife/quests.csv', 'r', encoding='UTF-8') as file:
                lines = file.readlines()
                item = random.choice(lines)
            # print(item)          

    def disconnect(self):
        print('disconnect clicked')
        self.con_msg.setText('disconnect clicked') 
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Serverapp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


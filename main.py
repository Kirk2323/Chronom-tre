import sys
import socket
import threading
import time


from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QPushButton, QLabel, QGridLayout, QWidget, QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.__compt = QLabel("Compteur : ")
        self.text = QLabel("0")
        self.y = 0
        self.arret_thread = False
        reset = QPushButton("Reset")
        quit = QPushButton("Quitter")
        start = QPushButton("Start")
        connect = QPushButton("Connect")
        stop = QPushButton("Stop")

        # Ajouter les composants au grid layout
        grid.addWidget(self.__compt, 0, 0, 1, 2)
        grid.addWidget(self.text, 1, 0, 1, 2)
        grid.addWidget(stop,3,1)
        grid.addWidget(connect,4,0)
        grid.addWidget(reset, 3, 0)
        grid.addWidget(start, 2, 0, 1, 2)
        grid.addWidget(quit, 4, 1)

        reset.clicked.connect(self.__reset)
        quit.clicked.connect(self.__actionQuitter)
        start.clicked.connect(self.__start)
        connect.clicked.connect(self.__connect)
        self.setWindowTitle("Chronomètre")

    def __start(self):
        if self.text.text().isnumeric():
            self.y = self.y + 1
            self.text.setText(f"{self.y}")
        else:
            self.text.setText("Attention ce n'est pas un chiffre")


         #Voici ce que j'aurais mis afin de réaliser la boucle
         # while self.arret_thread == False:
         #    self.y = self.y +1
         #    self.text.setText(f"{self.y}")


    def __stop(self):
        self.arret_thread = True

    def __reset(self):
        self.y = 0
        self.text.setText(f"{self.y}")

    def __actionQuitter(self):
        self.__stop()
        msg ="bye"
        QCoreApplication.exit(0)

    def __connect(self):
        msg = self.y
        client_socket = socket.socket()
        client_socket.connect(("localhost", 10000))
        print("Le client vient de se connecter")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


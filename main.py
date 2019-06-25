from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import os.path
from Selector import *
from Picture import *
from Informe import *
from Help import *

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.title = "FiloPlant"
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 300
        #self.statusBar().showMessage("Sanabio & Serrano")
        self.InitWindow()

    def InitWindow(self):

        self.setStyleSheet("background-color: #32CD32") 
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        # Creando Layot Padre 
        self.wid = QWidget(self)

        self.setCentralWidget(self.wid)

        # Layout
        LGeneral = QVBoxLayout()
        LDescriptor = QVBoxLayout()

        # Filoplant
        Descrip = QLabel(self)
        Descrip.setPixmap(QPixmap('./img/filoplant.png'))
        Descrip.setAlignment(QtCore.Qt.AlignCenter) 

        bizagi = QLabel(self)
        bizagi.setPixmap(QPixmap('./img/logo.png'))
        bizagi.setAlignment(QtCore.Qt.AlignCenter) 

  #      self.endemica = QLabel("Buscar por región endémica")
   #     self.endemica.setFont(QtGui.QFont("Arial Black", 15, QtGui.QFont.Bold))
    #self.endemica.setAlignment(QtCore.Qt.AlignCenter)

        self.config = QLabel("", self)
        self.config.move(20, 260)
        self.config.setStyleSheet("background-color: transparent;")
        self.config.resize(90, 90)
        self.config.setCursor(QCursor(Qt.PointingHandCursor))
        self.config.mousePressEvent = self.clickConfig

        self.inform = QLabel("", self)
        self.inform.move(292, 310)
        self.inform.setStyleSheet("background-color: transparent;")
        self.inform.resize(90, 90)
        self.inform.setCursor(QCursor(Qt.PointingHandCursor))
        self.inform.mousePressEvent = self.clickInform

        self.tree = QLabel("", self)
        self.tree.move(553, 255)
        self.tree.setStyleSheet("background-color: transparent;")
        self.tree.resize(90, 90)
        self.tree.setCursor(QCursor(Qt.PointingHandCursor))
        self.tree.mousePressEvent = self.clickTree

        self.help = QLabel("", self)
        self.help.move(403, 182)
        self.help.setStyleSheet("background-color: transparent;")
        self.help.resize(60, 60)
        self.help.setCursor(QCursor(Qt.PointingHandCursor))
        self.help.mousePressEvent = self.clickHelp

        self.map = QLabel("", self)
        self.map.move(215, 179)
        self.map.setStyleSheet("background-color: transparent;")
        self.map.resize(60, 60)
        self.map.setCursor(QCursor(Qt.PointingHandCursor))
#        self.map.mousePressEvent = self.clickMap
           
        LDescriptor.addWidget(Descrip)
        LDescriptor.addWidget(bizagi)
        LGeneral.addLayout(LDescriptor)
        self.wid.setLayout(LGeneral)

        self.show()

    def clickTree(self, event):
        self.principle = Image()
        self.setCentralWidget(self.principle)
        self.principle.btn.inicio.clicked.connect(self.devolver)

    def clickConfig(self, event):
        self.principle = Alineamiento()
        self.setCentralWidget(self.principle)
        self.principle.btn.inicio.clicked.connect(self.devolver)

    def clickInform(self, event):
        self.principle_mid = Informe()
        self.setCentralWidget(self.principle_mid)
        self.principle_mid.inicio.clicked.connect(self.devolver)

    def clickHelp(self, event):
        self.principle_mid = Help()
        self.setCentralWidget(self.principle_mid)
        self.principle_mid.inicio.clicked.connect(self.devolver)

    def devolver(self):
        self.setCentralWidget(Window())

if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    main = Window()
    sys.exit(app.exec())

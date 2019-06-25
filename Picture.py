import matplotlib.pyplot as plt
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import Phylo
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
import os
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class ChildWindow(QWidget):
    def __init__(self, name=None):
        super(ChildWindow, self).__init__()

        self.dir_Img = name
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        pixmap = QPixmap("./Imagenes/{}.png".format(self.dir_Img))
        self.label.setPixmap(pixmap)
        

        self.setGeometry(10, 10, 640, 480)
        self.setWindowTitle("Árbol Filogenético - %s" % self.dir_Img)
        self.show()

class listado(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        
        vbox = QVBoxLayout()

        self.lista = QListWidget()
        vbox.addWidget(self.lista)

        self.setLayout(vbox)


class btns(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        vbox = QHBoxLayout()
        self.img = QPushButton("Imagenes",self)
        self.delete = QPushButton("Delete",self)
        self.inicio = QPushButton("Inicio",self)
        
        vbox.addWidget(self.img)
        vbox.addWidget(self.delete)
        vbox.addWidget(self.inicio)

        self.setLayout(vbox)

class Image(QWidget):
    def __init__(self):
        super(Image, self).__init__()

        self.children =[]

        self.title = "Imagenes"
        self.left = 100
        self.top = 100
        self.width = 200
        self.height =250

        self.btn = btns(self)

        self.listaA = listado(self)
        self.btn.img.clicked.connect(self.btnstate)
        self.btn.delete.clicked.connect(self.delete)
        grid = QGridLayout()
        grid.addWidget(self.listaA,0,0)
        grid.addWidget(self.btn,1,0)
        self.setLayout(grid)

        self.listaA.lista.clicked.connect(self.listview)
        self.listaA.lista.setAlternatingRowColors(True)

        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def listview(self):
        self.item = self.listaA.lista.currentItem()
        child = ChildWindow(self.item.text())
        self.children.append(child)
         
    def btnstate(self, b):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        self.listaA.lista.clear()
        for i in ["Imagenes"]:
            image = os.path.join(BASE_DIR, i)
            for _, _, files in os.walk(image):
                for file in files:
                    path = file
                    item = QListWidgetItem(self.listaA.lista)
                    item.setText("{}".format(path.split(".png")[0]))

    def delete(self):
        listItems = self.listaA.lista.selectedItems()
        if not listItems : return
        for item in listItems:
            self.listaA.lista.takeItem(self.listaA.lista.row(item))
            os.system("rm ./Imagenes/{}.png".format(item.text()))

if __name__=="__main__":
    App = QApplication(sys.argv)
    imagen = Image()
    sys.exit(App.exec())

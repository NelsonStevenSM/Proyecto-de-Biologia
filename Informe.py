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
from PyQt5.QtCore import Qt

class ImgWidget(QLabel):

    def __init__(self, imagePath, parent = None):
        super(ImgWidget, self).__init__(parent)
        pic = QPixmap(imagePath)
        self.setPixmap(pic)
        self.setAlignment(QtCore.Qt.AlignCenter)


class Informe(QWidget):
    def __init__(self):
        super(Informe, self).__init__()

        self.children =[]

        self.title = "Imagenes"
        self.left = 150
        self.top = 150
        self.width = 400
        self.height =750
#        self.setMinimumSize(100,100)
 #       self.setMaximumSize(400,900)
        self.setFixedSize(400,400)
        self.tableWidget = QTableWidget()

        self.inicio = QPushButton("Inicio",self)
        self.inicio.setFixedSize(100,30)

        self.tableWidget.setRowCount(21)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(1,50)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(100)
        self.tableWidget.setHorizontalHeaderLabels(["Orquídea","Imagen"])
        

        grid = QGridLayout()
        grid.addWidget(self.tableWidget,0,0)
        grid.addWidget(self.inicio,1,0)
        self.setLayout(grid)


        self.btnstate()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def btnstate(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        list_Img = []
        for i in ["img/Plant"]:
            image = os.path.join(BASE_DIR, i)
            for _, _, files in os.walk(image):
                for file in files:
                    if file.endswith("jpg"):
                        path = file
                        list_Img.append(path)
        
        for i in range(0,len(list_Img)):
            item = QTableWidgetItem(list_Img[i].split(".jpg")[0][2:-1].capitalize())
            item.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(i,0, item)
            pixmap = QPixmap("./img/Plant/{}".format(list_Img[i]))
            self.tableWidget.setCellWidget(i,1, ImgWidget(imagePath=pixmap))

if __name__=="__main__":
    App = QApplication(sys.argv)
    informe = Informe()
    sys.exit(App.exec())
#            lblImg.move(100,100)
#            lblImg.show()

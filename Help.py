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

class Help(QWidget):
    def __init__(self):
        super(Help, self).__init__()

        self.title = "Imagenes"
        self.left = 150
        self.top = 150
        self.width = 680
        self.height =440
        self.setFixedSize(680,440)

        self.inicio = QPushButton("Inicio",self)
        self.inicio.setFixedSize(100,30)

        vbox = QVBoxLayout()
        lblTitle = QLabel("Bienvenido a FiloPlant",self)
        lblTitle.setAlignment(Qt.AlignCenter)
        lblTitle.setFont(QtGui.QFont("Arial Black", 14))
        body = QLabel(self)
        body.resize(50,150)
        body.setText(
                """
La familia Orchidaceae constituye para la flora peruana la familia más diversa, con alrededor de 212 géneros 
y 2020 especies, aunque se estima que el número real podría oscilar entre 2500 y 3500 especies. La 
mayoría son hierbas epífitas o terrestres, aunque hay también las que presentan ambos hábitos. En este 
trabajo reconocemos 775 endemismos en 137 géneros, lo que la constituye también en la familia con más 
taxones restringidos al Perú. Estos endemismos han sido encontrados en varias regiones ecológicas, 
principalmente en la Bosques Muy Húmedos Montanos, Bosques Muy Húmedos Premontanos y Mesoandina. 
La destrucción de sus hábitats y el comercio ilegal de plantas silvestres la hacen particularmente 
vulnerable desde el punto de vista de conservación. Ciento cinco taxones se encuentran en áreas 
naturales protegidas. 
Este es un software que fue creado sin fines de lucro y tienen varias funcionalidades: """)


        #self.Config.setAlignment(Qt.AlignCenter)
#        self.Config.show()

        vbox.addWidget(lblTitle)
        vbox.addWidget(body)

        self.Config = QLabel(self)
        pic = QPixmap("./img/seleccionarEspecies.png")
        pic = pic.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.Config.setPixmap(pic)
        lblConfig = QLabel("Aqui se selecciona un conjunto de especies de acuerdo a la categoria que usted escoga",self)
        lblConfig.setFont(QtGui.QFont("Arial Black", 8))
        self.Config.setStyleSheet("background-color: black;")
        self.Config.setMaximumSize(32,32)
        ConfigV = QHBoxLayout()
        ConfigV.addWidget(self.Config)
        ConfigV.addWidget(lblConfig)
        vbox.addLayout(ConfigV)

        self.Config = QLabel(self)
        pic = QPixmap("./img/somos.png")
        pic = pic.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.Config.setPixmap(pic)
        lblConfig = QLabel("Aqui se muestra todas las Orquideas con su respectiva Imagen",self)
        self.Config.setStyleSheet("background-color: black;")
        self.Config.setMaximumSize(32,32)
        lblConfig.setFont(QtGui.QFont("Arial Black", 8))
        ConfigV = QHBoxLayout()
        ConfigV.addWidget(self.Config)
        ConfigV.addWidget(lblConfig)
        vbox.addLayout(ConfigV)

        self.Config = QLabel(self)
        pic = QPixmap("./img/filo.png")
        pic = pic.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.Config.setPixmap(pic)
        lblConfig = QLabel("Aqui se guardan las imagenes (Arboles Filogeneticos) que se analizaron en la primera etapa",self)
        lblConfig.setFont(QtGui.QFont("Arial Black", 8))
        ConfigV = QHBoxLayout()
        self.Config.setStyleSheet("background-color: black;")
        self.Config.setMaximumSize(32,32)
        ConfigV.addWidget(self.Config)
        ConfigV.addWidget(lblConfig)
        vbox.addLayout(ConfigV)

        self.Config = QLabel(self)
        pic = QPixmap("./img/Peru-Flag-Map.png")
        pic = pic.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.Config.setPixmap(pic)
        lblConfig = QLabel("Aqui se muestra un mapa para localizar las plantas endémicas que están en nuestra base de datos",self)
        lblConfig.setFont(QtGui.QFont("Arial Black", 8))
        self.Config.setStyleSheet("background-color: black;")
        self.Config.setMaximumSize(32,32)
        ConfigV = QHBoxLayout()
        ConfigV.addWidget(self.Config)
        ConfigV.addWidget(lblConfig)
        vbox.addLayout(ConfigV)


        vbox.addWidget(self.inicio)
        self.setLayout(vbox)


        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

if __name__=="__main__":
    App = QApplication(sys.argv)
    help = Help()
    sys.exit(App.exec())

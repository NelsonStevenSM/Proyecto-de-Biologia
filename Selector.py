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
        
        vbox = QVBoxLayout()
        self.clear = QPushButton("Clear",self)
        self.delete = QPushButton("Delete",self)
        self.generate = QPushButton("Generate",self)
        self.inicio = QPushButton("Inicio",self)
        
        vbox.addWidget(self.clear)
        vbox.addWidget(self.delete)
        vbox.addWidget(self.generate)
        vbox.addWidget(self.inicio)

        self.setLayout(vbox)

class Alineamiento(QWidget):
    def __init__(self):
        super(Alineamiento, self).__init__()
        self.title = "Alineamiento"
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height =600
    
        self.btn = btns(self)
        self.listaA = listado(self)
        self.listaB = listado(self)

        grid = QGridLayout()
        grid.addWidget(self.groupBox(),0,0)
        grid.addWidget(self.listaA,0,1)
        grid.addWidget(self.listaB,0,2)
        grid.addWidget(self.btn,0,3)
        self.setLayout(grid)

        self.listaA.lista.clicked.connect(self.listview)
        self.listaA.lista.setAlternatingRowColors(True)
        self.listaB.lista.setHidden(True)
        self.listaB.lista.setAlternatingRowColors(True)
        self.btn.delete.clicked.connect(self.delete)
        self.btn.clear.clicked.connect(self.clear)
        self.btn.generate.clicked.connect(self.generate)

        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def delete(self):
        listItems = self.listaB.lista.selectedItems()
        if not listItems : return
        for item in listItems:
            self.listaB.lista.takeItem(self.listaB.lista.row(item))

    def groupBox(self):
        group = QGroupBox("Categorias")

        self.rdYcf1 = QRadioButton("Ycf1")
        self.rdYcf1.toggled.connect(lambda:self.btnstate(self.rdYcf1))
        self.rdK = QRadioButton("K")
        self.rdK.toggled.connect(lambda:self.btnstate(self.rdK))
        self.rdD1 = QRadioButton("D1")
        self.rdD1.toggled.connect(lambda:self.btnstate(self.rdD1))
        self.rdS19 = QRadioButton("S19")
        self.rdS19.toggled.connect(lambda:self.btnstate(self.rdS19))
        self.rdSubnit = QRadioButton("subunit")
        self.rdSubnit.toggled.connect(lambda:self.btnstate(self.rdSubnit))

        self.rdYcf1.setChecked(True)
        vbox = QVBoxLayout()

        vbox.addWidget(self.rdYcf1)
        vbox.addWidget(self.rdK)
        vbox.addWidget(self.rdD1)
        vbox.addWidget(self.rdS19)
        vbox.addWidget(self.rdSubnit)

        group.setLayout(vbox)

        return group

    def listview(self):
        self.item = self.listaA.lista.currentItem()
        self.listaB.lista.addItem(self.item.text())
        self.listaB.lista.setHidden(False)
        
    def btnstate(self, b):
        btnList = ["Ycf1", "K", "D1", "S19", "subunit"]
        for i in btnList:
            if b.text() == i:
                if b.isChecked() == True:
                    File = open('./Categoria/{}.txt'.format(i),'r')
                    for linea in File.readlines():
                        item = QListWidgetItem(self.listaA.lista)
                        lineDiv = linea.split("/")
                        item.setText("{0}/{1}".format(lineDiv[2],lineDiv[3]))
                    File.close()
                else:
                    self.listaA.lista.clear()

    def clear(self):
        self.listaB.lista.setHidden(True)
        self.listaB.lista.clear()
        os.system('rm all.fasta ')

    def generate(self):
        FileOutput = open("./output.txt",'w')
        for i in range(self.listaB.lista.count()):
            itemList = self.listaB.lista.item(i).text().split('/')
            FileOutput.write("./FASTAS/{}/{}".format(itemList[0],itemList[1]))

        FileOutput.close()
        # Generar todo el fasta a alinear.
        with open('./output.txt') as f:
        	for line in f:
        		path = line.strip('\n').replace(" ","\\ ")
        		os.system('cat '+path+' >> all.fasta')
        #
        #MuscleCommandline
        os.system('muscle -in all.fasta -clwout tree.aln ')
        with open("./tree.aln", "r") as aln:
            algn = AlignIO.read(aln,"clustal")
        calculator = DistanceCalculator('identity')
        dm = calculator.get_distance(algn)
        constructor = DistanceTreeConstructor(calculator)
        upgma_tree = constructor.build_tree(algn)
        Phylo.draw(upgma_tree)

	
if __name__=="__main__":
    App = QApplication(sys.argv)
    alineamiento = Alineamiento()
    sys.exit(App.exec())

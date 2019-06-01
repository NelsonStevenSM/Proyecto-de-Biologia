from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os.path
class configButton(QWidget):
    def __init__(self,parent, path, acro):
        super().__init__(parent)

        self.info = os.path.basename(path).split('.')
        print(self.info)
       
        self.but = QPushButton(self)
        self.but.setIcon(QtGui.QIcon(QPixmap(path)))
        self.but.clicked.connect(self.handleButton)
        self.but.setIconSize(QtCore.QSize(50, 50))

        self.lbl = QLabel(acro)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))

        self.layoutConf = QVBoxLayout(self)

        self.layoutConf.addWidget(self.but)
        self.layoutConf.addWidget(self.lbl)

        self.setLayout (self.layoutConf)


    def handleButton(self):
        pass

class Buscador(QWidget):

    def __init__(self,parent):
        super(Buscador, self).__init__(parent)
        
        self.layout = QHBoxLayout(self)

        self.textB = QLineEdit(self)
        self.textB.setPlaceholderText("Buscar por Familia ... ")   

        self.layout.addWidget(self.textB)

        self.search = QPushButton("Buscar")

        self.layout.addWidget (self.search)
        self.setLayout (self.layout)



class Window(QMainWindow):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)

        self.title = "FiloPlant"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.loadImage()
        self.InitWindow()

    def InitWindow(self):

        self.setStyleSheet("background-color: #32CD32") 
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.map = QPushButton("Mapa")

        grid = QGridLayout()
        grid.setSpacing(7)
        grid.addWidget(self.button00,0,0)
        grid.addWidget(self.button01,0,1)
        grid.addWidget(self.button10,1,0)
        grid.addWidget(self.button11,1,1)
        grid.addWidget(self.button20,2,0)
        grid.addWidget(self.button21,2,1)
        grid.addWidget(self.map,3,0,1,2)
        # Creando Layot Padre 
        wid = QWidget(self)

        self.setCentralWidget(wid)

        self.form = Buscador(self)

        # Layout
        LGeneral = QHBoxLayout()
        LDescriptor = QVBoxLayout()
        LGyForm = QVBoxLayout()

        # Filoplant
        Descrip = QLabel(self)
        Descrip.setPixmap(QPixmap('./img/filoplant.jpeg'))
        
        LDescriptor.addWidget(Descrip)

        LGeneral.addLayout(LDescriptor,1)

        self.endemica = QLabel("Buscar por región endémica")
        self.endemica.setFont(QtGui.QFont("Arial Black", 15, QtGui.QFont.Bold))
        self.endemica.setAlignment(QtCore.Qt.AlignCenter)

        LGyForm.addWidget(self.endemica)

        LGyForm.addLayout(grid)
        LGyForm.addWidget(self.form)
        LGeneral.addLayout(LGyForm,1)

        wid.setLayout(LGeneral)

        self.show()

    def loadImage(self):

        self.button00 = configButton(self,"./img/Epidendrum_secundum.jpg", "BMHP")
        self.button01 = configButton(self,"./img/Masdevallia_barlaeana.jpg", "AA")
        self.button10 = configButton(self,"./img/Masdevallia_urosalpinx.jpg", "BHA")
        self.button11 = configButton(self,"./img/Masdevallia_davisii.jpg", "BS")
        self.button20 = configButton(self,"./img/Masdevallia_uniflora.jpg", "MDE")
        self.button21 = configButton(self,"./img/Phragmipedium.jpg", "PHS")

if __name__ =="__main__":

    import sys
    app = QApplication(sys.argv)
    window = Window()

    sys.exit(app.exec_())

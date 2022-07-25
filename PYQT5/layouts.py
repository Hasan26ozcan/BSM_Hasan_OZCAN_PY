import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import(QApplication,QMainWindow,QWidget)
from PyQt5.QtGui import QPalette,QColor
from matplotlib.widgets import Widget

class Color(QWidget):
    def __init__(self,color):
        super(Color,self).__init__()
        self.setAutoFillBackground(True)

        palette=self.palette()
        palette.setColor(QPalette.Window,QColor(color))
        self.setPalette(palette)
class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,600,400)

        layout1=QtWidgets.QHBoxLayout()
        layout1.addWidget(Color("red"))
        layout1.addWidget(Color("blue"))
        layout1.addWidget(Color("yellow"))
        layout1.addWidget(Color("green"))
        layout1.addWidget(Color("black"))
        layout1.addWidget(Color("orange"))
        layout1.setContentsMargins(100,20,100,10)# burda verdiğimiz deger için degerlerimizi o aralıga sıkıştırmasını saglıyor
        layout1.setSpacing(50)# burdada her eleman arasında verdiğimiz kadar bosluk birakir




        layout2=QtWidgets.QVBoxLayout()
        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("blue"))
        layout2.addWidget(Color("yellow"))
        layout2.addWidget(Color("green"))
        layout2.addWidget(Color("black"))
        layout2.addWidget(Color("orange"))
        layout2.setContentsMargins(100,20,100,10)
        layout2.setSpacing(20)

        vloyout2=QtWidgets.QVBoxLayout()
        vloyout2.addLayout(layout1)
        vloyout2.addLayout(layout2)

        # layout=QtWidgets.QGridLayout()
        # layout.addWidget(Color("red"),0,0)
        # layout.addWidget(Color("blue"),1,0)
        # layout.addWidget(Color("yellow"),0,2)
        # layout.addWidget(Color("pink"),2,0)
        # layout.addWidget(Color("green"),1,1)
        # layout.addWidget(Color("magenta"),0,2)


        widget=QWidget()
        widget.setLayout(vloyout2)


        
        self.setCentralWidget(widget)


def window():
    app=QApplication(sys.argv)
    win=mainwindow()
    win.show()
    sys.exit(app.exec_())


window()
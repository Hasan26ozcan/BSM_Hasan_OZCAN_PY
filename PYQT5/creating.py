import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QToolTip,QPushButton, QApplication)



def window():
    app= QtWidgets.QApplication(sys.argv)# uygulama oluştur
    win=QtWidgets.QMainWindow()# pencere oluştur
    win.show()# ekranda göstermek için bu methoda ihtiyacımız var
    win.setWindowTitle("first application")
    win.setGeometry(150,150,1000,600)
    win.setWindowIcon(QIcon("icon.png"))
    win.setToolTip("my tooltip")
    sys.exit(app.exec_())# çarpı ikonuna tıkladıgımızda uygulamanın kapanmasını saglıyoruz


window()













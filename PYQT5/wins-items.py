import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QToolTip,QPushButton, QApplication)
from matplotlib.pyplot import connect

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow,self).__init__()

        self.setWindowTitle("first application")
        self.setGeometry(200,200,700,700)
        self.setWindowIcon(QIcon("icon.png"))
        self.setToolTip("my tooltip")
        self.initUI()
    def initUI(self):
        self.lbl_name=QtWidgets.QLabel(self)
        self.lbl_name.setText("Adınız:")
        self.lbl_name.move(50,30)

        self.lbl_result=QtWidgets.QLabel(self)
        self.lbl_result.setText("sonuç degerimiz")
        self.lbl_result.move(150,150)



        self.lbl_surname=QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız: ")
        self.lbl_surname.move(50,60)

        self.name_text=QtWidgets.QLineEdit(self)
        self.name_text.move(150,30)
        self.name_text.resize(200,20)


        self.surname_text=QtWidgets.QLineEdit(self)
        self.surname_text.move(150,60)
        self.surname_text.resize(200,20)



        self.btn_save=QtWidgets.QPushButton(self)
        self.btn_save.setText("sing in")
        self.btn_save.move(150,100)
        self.btn_save.clicked.connect(self.clicked)
    def clicked(self):
            self.lbl_resultan=QtWidgets.QLabel(self)
            self.lbl_resultan.setText("apskdaskdasd")
            self.lbl_resultan.move(200,200)
            self.lbl_result.setText(f"butona tıklanmıştır name: {self.name_text.text()} surname: {self.surname_text.text()} ")
            self.lbl_result.resize(2000,10)
            self.lbl_result.move(150,150)




def window():
    app= QtWidgets.QApplication(sys.argv)# uygulama oluştur
    win=mywindow()# pencere oluştur

    win.show()# ekranda göstermek için bu methoda ihtiyacımız var
    sys.exit(app.exec_())# çarpı ikonuna tıkladıgımızda uygulamanın kapanmasını saglıyoruz


window()





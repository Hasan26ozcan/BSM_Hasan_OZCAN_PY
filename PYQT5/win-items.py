import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QToolTip,QPushButton, QApplication)
from matplotlib.pyplot import connect


def window():
    app= QtWidgets.QApplication(sys.argv)# uygulama oluştur
    win=QtWidgets.QMainWindow()# pencere oluştur
    
    win.setWindowTitle("first application")
    win.setGeometry(200,200,700,700)
    win.setWindowIcon(QIcon("icon.png"))
    win.setToolTip("my tooltip")

    lbl_name=QtWidgets.QLabel(win)
    lbl_name.setText("Adınız:")
    lbl_name.move(50,30)

    lbl_surname=QtWidgets.QLabel(win)
    lbl_surname.setText("Soyadınız: ")
    lbl_surname.move(50,60)

    name_text=QtWidgets.QLineEdit(win)
    name_text.move(150,30)


    surname_text=QtWidgets.QLineEdit(win)
    surname_text.move(150,60)


    def clicked(self):
        print(f"butona tıklanmıştır name: {name_text.text()} surname: {surname_text.text()} ")




    btn_save=QtWidgets.QPushButton(win)
    btn_save.setText("sing in")
    btn_save.move(150,100)
    btn_save.clicked.connect(clicked)




    win.show()# ekranda göstermek için bu methoda ihtiyacımız var
    sys.exit(app.exec_())# çarpı ikonuna tıkladıgımızda uygulamanın kapanmasını saglıyoruz


window()





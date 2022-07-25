from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from _radiobuttonform import Ui_MainWindow



class myApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioturkiye.setChecked(True)
        self.ui.radiolise.setChecked(True)
        # bunun sayesinde geldigi gibi direkt onun seçilmesini saglıyoruz
        self.ui.radioturkiye.toggled.connect(self.onclickedulke)
        self.ui.radioalmanya.toggled.connect(self.onclickedulke)
        self.ui.radioazerbaican.toggled.connect(self.onclickedulke)
        self.ui.radioyunanistan.toggled.connect(self.onclickedulke)
        self.ui.radioilkokul.toggled.connect(self.onclickedegitim)
        self.ui.radiolise.toggled.connect(self.onclickedegitim)
        self.ui.radiouniversite.toggled.connect(self.onclickedegitim)
        self.ui.radioyuksekogretim.toggled.connect(self.onclickedegitim)

        self.ui.btn_uklesecim.clicked.connect(self.getselectingulke)
        self.ui.btn_egitimsecim.clicked.connect(self.getselectingegitim)
        self.ui.btn_herikibilgide.clicked.connect(self.getherikibilgide)

    def onclickedulke(self):
        item=self.sender()
        if item.isChecked()==True:
            print(f"seçilen radio {item.text()} ")
    def onclickedegitim(self):
        item=self.sender()
        if item.isChecked()==True:
            print(f"seçilen radio {item.text()} ")
    def getselectingulke(self):
        items=self.ui.group_ulke.findChildren(QtWidgets.QRadioButton)
        for i in items:
            if(i.isChecked()==True):
                self.ui.lbl_ulke.setText(f"seçilen ülke: {i.text()}")
    def getselectingegitim(self):
        items=self.ui.group_egitim.findChildren(QtWidgets.QRadioButton)
        for i in items:
            if(i.isChecked()==True):
                self.ui.lbl_okul.setText(f"seçilen egitim: {i.text()}")
    def getherikibilgide(self):
        items=self.ui.group_egitim.findChildren(QtWidgets.QRadioButton)
        a=""
        b=""
        for i in items:
            if(i.isChecked()==True):
                a=i.text()
        items=self.ui.group_ulke.findChildren(QtWidgets.QRadioButton)
        for i in items:
            if(i.isChecked()==True):
                b=i.text()
        self.ui.lbl_ikibilgi.setText(f"{b} , {a}   ")


def window():
    app=QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())        

window()
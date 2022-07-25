import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("calculate")
        self.setGeometry(100,100,600,400)
        self.setToolTip("calculate")
        self.setWindowIcon(QIcon("icon2.png"))
        self.initUI()
    def initUI(self):
        self.lbl_sayi1=QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("sayi 1: ")
        self.lbl_sayi1.move(50,25)

        self.lbl_sayi1_btn1=QtWidgets.QLineEdit(self)
        self.lbl_sayi1_btn1.move(100,30)
        self.lbl_sayi1_btn1.resize(100,20)


        self.lbl_sayi2=QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("sayi 2: ")
        self.lbl_sayi2.move(50,50)

        self.lbl_sayi1_btn2=QtWidgets.QLineEdit(self)
        self.lbl_sayi1_btn2.move(100,55)
        self.lbl_sayi1_btn2.resize(100,20)

        # self.lbl_islem=QtWidgets.QLabel(self)
        # self.lbl_islem.setText("islem: ")
        # self.lbl_islem.move(50,70)

        self.lbl_toplam=QtWidgets.QPushButton(self)
        self.lbl_toplam.setText("TOPLAMA")
        self.lbl_toplam.move(50,100)
        self.lbl_toplam.clicked.connect(self.hesapma)

        self.lbl_carpma=QtWidgets.QPushButton(self)
        self.lbl_carpma.setText("ÇARPMA")
        self.lbl_carpma.move(50,150)
        self.lbl_carpma.clicked.connect(self.hesapma)


        self.lbl_cikartma=QtWidgets.QPushButton(self)
        self.lbl_cikartma.setText("ÇIKARTMA")
        self.lbl_cikartma.move(200,150)
        self.lbl_cikartma.clicked.connect(self.hesapma)

        self.lbl_bolme=QtWidgets.QPushButton(self)
        self.lbl_bolme.setText("BÖLME")
        self.lbl_bolme.move(200,100)
        self.lbl_bolme.clicked.connect(self.hesapma)

        self.lbl_sonuc_place=QtWidgets.QLabel(self)
        self.lbl_sonuc_place.setText("sonuç alanı")
        self.lbl_sonuc_place.move(150,200)
        self.lbl_sonuc_place.resize(200,10)





    def toplam(self):
        toplam=float(self.lbl_sayi1_btn1.text())+float(self.lbl_sayi1_btn2.text())
        self.lbl_sonuc_place.setText(str(toplam))
    def carpma(self):
        carpma=float(self.lbl_sayi1_btn1.text())*float(self.lbl_sayi1_btn2.text())
        self.lbl_sonuc_place.setText(str(carpma))
    def cikartma(self):
        cıkartma=float(self.lbl_sayi1_btn1.text())-float(self.lbl_sayi1_btn2.text())
        if(cıkartma<0):
            cıkartma=cıkartma*-1
        self.lbl_sonuc_place.setText(str(cıkartma))
    def bolme(self):
        bolme=float(self.lbl_sayi1_btn1.text())/float(self.lbl_sayi1_btn2.text())
        if (int(bolme)<1):
            bolme=float(self.lbl_sayi1_btn2.text())/float(self.lbl_sayi1_btn1.text())
        self.lbl_sonuc_place.setText(str(bolme))





    def hesapma(self):
        sender=self.sender()
        result=0.0
        sender=sender.text()
        if(sender=="TOPLAMA"):
            result=float(self.lbl_sayi1_btn1.text())+float(self.lbl_sayi1_btn2.text())
        elif(sender=="ÇARPMA"):
            result=float(self.lbl_sayi1_btn1.text())*float(self.lbl_sayi1_btn2.text())
        elif(sender=="BÖLME"):
            result=float(self.lbl_sayi1_btn1.text())/float(self.lbl_sayi1_btn2.text())
            if (int(result)<1):
                result=float(self.lbl_sayi1_btn2.text())/float(self.lbl_sayi1_btn1.text())
        elif(sender=="ÇIKARTMA"):
            result=float(self.lbl_sayi1_btn1.text())-float(self.lbl_sayi1_btn2.text())
            if(result<0):
                result=result*-1
        self.lbl_sonuc_place.setText(str(result))






def window():
    app=QApplication(sys.argv)
    win=calculator()
    win.show()
    sys.exit(app.exec_())

window()

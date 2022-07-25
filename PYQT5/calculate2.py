from PyQt5 import QtWidgets
import sys
from mainwindow import Ui_UI_MainWindow

class myapp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_UI_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_toplama.clicked.connect(self.hesapma)
        self.ui.btn_carpma.clicked.connect(self.hesapma)
        self.ui.btn_bolme.clicked.connect(self.hesapma)
        self.ui.btn_cikarma.clicked.connect(self.hesapma)
    def hesapma(self):
        sender=self.sender()
        result=0.0
        sender=sender.text()
        if(sender=="toplama"):
            result=float(self.ui.txt_sayi1.text())+float(self.ui.txt_sayi2.text())
        elif(sender=="çarpma"):
            result=float(self.ui.txt_sayi1.text())*float(self.ui.txt_sayi2.text())
        elif(sender=="bölme"):
            result=float(self.ui.txt_sayi1.text())/float(self.ui.txt_sayi2.text())
            if (int(result)<1):
                result=float(self.ui.txt_sayi2.text())/float(self.ui.txt_sayi1.text())
        elif(sender=="çıkarma"):
            result=float(self.ui.txt_sayi1.text())-float(self.ui.txt_sayi2.text())
            if(result<0):
                result=result*-1
        self.ui.label_3.setText(str(result))




def window():
    app=QtWidgets.QApplication(sys.argv)
    win=myapp()
    win.show()
    sys.exit(app.exec_())

window()














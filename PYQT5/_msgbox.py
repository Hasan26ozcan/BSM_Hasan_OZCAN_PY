from email.policy import default
from re import A
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
import sys
from _messegaboxforms import Ui_MainWindow

class myapp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnexit.clicked.connect(self.closewindows)

    def closewindows(self):
        result=QMessageBox.question(self,"Close application","Are you sure ?",QMessageBox.Ok |QMessageBox.Cancel |QMessageBox.Ignore,QMessageBox.Cancel)
        if(result==QMessageBox.Ok):# bu butona tıklayıp tıklamadıgına bakıyoruz yani ordan dönen sayılar eşitmi
            print("yes clicked")
            QtWidgets.qApp.quit()
        else:
            print("no clicked")








    #     msg=QMessageBox()
    #     msg.setWindowTitle("Close application")
    #     msg.setText("Are you sure ?")
    #     msg.setIcon(QMessageBox.Question)
    #     msg.setStandardButtons(QMessageBox.Ok |QMessageBox.Cancel |QMessageBox.Ignore)
    #     msg.setDefaultButton(QMessageBox.Ok)
    #     msg.setDetailedText("details")
    #     msg.buttonClicked.connect(self.popup_buton)
    #     x=msg.exec_()# x burdan nasıl bir dönüt aldıgımızı söylüyor bize
    #     print(x)
    # def popup_buton(self,i):
    #     a=self.sender()
    #     print(a.text(),i.text())
    #     if(i.text()=="OK"):
    #         print("okey....")
    #         QtWidgets.qApp.quit()
    #     elif(i.text()=="Cancel"):
    #         print("cancel....")
    #     elif(i.text()=="Ignore"):
    #         print("ıgnore...")



def window():
    app=QApplication(sys.argv)
    win=myapp()
    win.show()
    sys.exit(app.exec_())     

window()   

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from _checkfrom import Ui_MainWindow


class myapp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()   
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cbsinema.stateChanged.connect(self.show_state)
        self.ui.cbkitapokumak.stateChanged.connect(self.show_state)
        self.ui.cbspor.stateChanged.connect(self.show_state)


        self.ui.pushButton.clicked.connect(self.hobiler)
        self.ui.pushButton_2.clicked.connect(self.groupdersler)
    

    def hobiler(self):
        item=self.ui.grouphobiler.findChildren(QtWidgets.QCheckBox)
        listem= []
        for i in item:
            if(i.isChecked()==True):
                print(i.text())
                listem.append(i.text())
        str=""
        for i in listem:
            str+=i+"\n"

        self.ui.lblresult.setText(str)

    def groupdersler(self):
        item=self.ui.grouphobiler_2.findChildren(QtWidgets.QCheckBox)
        listem= []
        for i in item:
            if(i.isChecked()==True):
                print(i.text())
                listem.append(i.text())
        str=""
        for i in listem:
            str+=i+"\n"

        self.ui.lblresult_2.setText(str)


    def show_state(self,value):
        cb=self.sender()
        print(value)
        print(cb.text())  
        print(cb.isChecked())
    

    # def show_state(self,value):
    #     print(value)
    #     print(self.ui.cbsinema.isChecked())# eger seçim olduysa bize true degeri seçim olmadıysa False degeri gelicek
    #     print(self.ui.cbsinema.text())

def window():
    apps=QApplication(sys.argv)
    win=myapp()
    win.show()
    sys.exit(apps.exec_())

window()    
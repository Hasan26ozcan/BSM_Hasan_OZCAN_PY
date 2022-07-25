from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QTableWidgetItem
from _tableproductsfrom import Ui_MainWindow
import sys

class myapp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadtable()
        self.ui.btnsave.clicked.connect(self.addtable)
        self.ui.tablepro.doubleClicked.connect(self.dobclick)
    def dobclick(self):
        for i in (self.ui.tablepro.selectedItems()):
            print(i.row(),i.column(),i.text())


    def addtable(self):
        name=self.ui.linename.text()
        price=self.ui.lineprice.text()
        a=self.ui.tablepro.rowCount()
        print(a)
        self.ui.tablepro.insertRow(a)
        self.ui.tablepro.setItem(a,0,QTableWidgetItem(str(name)))
        self.ui.tablepro.setItem(a,1,QTableWidgetItem(str(price)))
        



    def loadtable(self):

        prducts=[
            {"name":"samsung s50","price":"2000"},
            {"name":"samsung s60","price":"3000"},
            {"name":"samsung s70","price":"4000"},
            {"name":"samsung s80","price":"5000"},
            
        ]







        self.ui.tablepro.setRowCount(len(prducts))
        self.ui.tablepro.setColumnCount(2)
        #self.ui.tablepro.setVerticalHeaderLabels(("name","price"))
        self.ui.tablepro.setHorizontalHeaderLabels(("name","price"))
        self.ui.tablepro.setColumnWidth(0,120)
        self.ui.tablepro.setColumnWidth(1,500)
        rowindek=0
        for port in prducts:
            self.ui.tablepro.setItem(rowindek,0,QTableWidgetItem(port["name"]))
            self.ui.tablepro.setItem(rowindek,1,QTableWidgetItem(port["price"]))


            rowindek+=1



#         self.ui.tablepro.setItem(0,0,QTableWidgetItem("samsung s5"))
#         self.ui.tablepro.setItem(0,1,QTableWidgetItem("2000"))
#         self.ui.tablepro.setItem(1,0,QTableWidgetItem("samsung s6"))
#         self.ui.tablepro.setItem(1,1,QTableWidgetItem("2000"))
#         self.ui.tablepro.setItem(2,0,QTableWidgetItem("samsung s7"))
#         self.ui.tablepro.setItem(2,1,QTableWidgetItem("2000"))

def window():
    app=QApplication(sys.argv)
    win=myapp()
    win.show()
    sys.exit(app.exec_())

window()
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from _comboboxforms import Ui_MainWindow
class myapp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)


        # combo=self.ui.cbsehirler
        # combo.addItem("eskişehir")
        # combo.addItem("bursa")
        # combo.addItems(["adana","eskişehir","izmir"])

        self.ui.btnloaditem.clicked.connect(self.loaditems)
        self.ui.btngetitem.clicked.connect(self.getitem)
        self.ui.cbsehirler.currentIndexChanged.connect(self.selectedchangeindex)# burda eger biz birşey belirtmezsek indek bilgisi gelir
        self.ui.cbsehirler.currentIndexChanged[str].connect(self.selectedchangetext)# ama burda [str] yazdıgımızda o indeksin str degeri geliyor
        self.ui.btnclearitem.clicked.connect(self.deleteitem)
    def deleteitem(self):
        self.ui.cbsehirler.clear()
    def getitem(self):
        count=self.ui.cbsehirler.count()
        print(f"eleman sayısı {count} ")
        for i in range(count):
            print(self.ui.cbsehirler.itemText(i))
        print(self.ui.cbsehirler.currentText())
        print(self.ui.cbsehirler.currentIndex())


    def loaditems(self):
        self.ui.cbsehirler.addItems(["adıyaman","eskişehir","istanbul"])
    def selectedchangeindex(self,index):
        print(index)
    def selectedchangetext(self,text):
        print(text)





def window():
    app=QApplication(sys.argv)
    win=myapp()
    win.show()
    sys.exit(app.exec_())

window()

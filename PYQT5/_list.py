from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QInputDialog,QListView,QLineEdit,QMessageBox
import sys
from _listforms import Ui_MainWindow

class myapp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        #loadstudent
        self.loadStudents()
        
        # add student
        self.ui.btnadd.clicked.connect(self.addstudent)
        # edit student
        self.ui.btnedit.clicked.connect(self.editstudent)
        # delete student
        self.ui.btnremove.clicked.connect(self.removerstudent)
        # up 
        self.ui.btnup.clicked.connect(self.upstudent)
        # down
        self.ui.btndown.clicked.connect(self.downstudent)
        #sort student
        self.ui.btnsort.clicked.connect(self.sortstudent)
        #close
        self.ui.btnexit.clicked.connect(self.close)

    def addstudent(self):
        currentindex=self.ui.listItems.currentRow()# seçili olans atırın yerine kelmemizi saglıyor
        text, ok =QInputDialog.getText(self,"new student","student name")
        if (ok) and (text is not None):
            self.ui.listItems.insertItem(currentindex,text)
    def editstudent(self):
        currentindex=self.ui.listItems.currentRow()
        item=self.ui.listItems.item(currentindex)

        if item is not None:
            text, ok=QInputDialog.getText(self,"edit student","student name", QLineEdit.Normal, item.text())
            if ok and text is not None:
                item.setText(text)
    def removerstudent(self):
        currentindeks=self.ui.listItems.currentRow()
        item=self.ui.listItems.item(currentindeks)
        if item is None:
            return None
        else:
            x=QMessageBox.question(self,"remove student","do you want to student ?"+ item.text(),QMessageBox.Ok |QMessageBox.Cancel)
            if x == QMessageBox.Ok:
                item=self.ui.listItems.takeItem(currentindeks)
                del item
    def upstudent(self):
        currentindex=self.ui.listItems.currentRow()
        if currentindex==0:
            item=self.ui.listItems.takeItem(currentindex)
            a=self.ui.listItems.count()
            self.ui.listItems.insertItem(a,item)
            self.ui.listItems.setCurrentItem(item)
        else:
            item=self.ui.listItems.takeItem(currentindex)
            self.ui.listItems.insertItem(currentindex-1,item)
            self.ui.listItems.setCurrentItem(item)
    def downstudent(self):
        currentindex=self.ui.listItems.currentRow()
        if currentindex<self.ui.listItems.count()-1:
            item=self.ui.listItems.takeItem(currentindex)
            self.ui.listItems.insertItem(currentindex+1,item)
            self.ui.listItems.setCurrentItem(item)
        else:            
            item=self.ui.listItems.takeItem(currentindex)
            self.ui.listItems.insertItem(0,item)
            self.ui.listItems.setCurrentItem(item)


    def sortstudent(self):
        self.ui.listItems.sortItems()

    def close(self):
        QtWidgets.qApp.quit()




    def loadStudents(self):
        for i in ["ahmet","mehmet","çınar"]:
            self.ui.listItems.addItem(i)
        self.ui.listItems.setCurrentRow(1)



def window():
    app=QApplication(sys.argv)
    win=myapp()
    win.show()
    sys.exit(app.exec_())
window()


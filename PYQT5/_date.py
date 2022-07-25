from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
from _datetimeeditforms import Ui_MainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


class mypp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btncalculate.clicked.connect(self.calculate)
    def calculate(self):
        start=self.ui.datestart.date()
        end=self.ui.dateend.date()
        print(f"mounth {start.daysInMonth()} ")
        print(f'Days in year: {start.daysInYear()}')
        print(f"total days {start.daysTo(end)} ")

        now=QDate.currentDate()
        print(now)

        print(f"format date {start.daysTo(now)} ")

        print(start,end)

        


def window():
    app=QApplication(sys.argv)
    win=mypp()
    win.show()
    sys.exit(app.exec_())

window()
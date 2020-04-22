# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:06:56 2020

@author: USER
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QLabel, QCalendarWidget
from PyQt5.QtCore import QDate

class MyApp(QWidget):
    
    def __init__(self):
       super().__init__()
       self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)
        
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        
        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)
        
        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 200)
        self.show()
        
    def showDate(self, date):
        self.lbl.setText(date.toString())
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
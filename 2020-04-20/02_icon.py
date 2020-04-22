# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:35:26 2020

@author: USER
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('shop4.jpg'))
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
                      
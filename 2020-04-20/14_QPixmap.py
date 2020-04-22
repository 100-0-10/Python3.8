# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:38:03 2020

@author: USER
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    
     def __init__(self):
        super().__init__()
        self.initUI()
        
     def initUI(self):
        pixmap = QPixmap('landscape.jpg')
        
        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        lbl_size.setAlignment(Qt.AlignCenter)
        
        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        vbox.addWidget(lbl_size)
        self.setLayout(vbox)
        
        self.setWindowTitle('QPixmap')
        self.setGeometry(300, 300, 400, 200)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
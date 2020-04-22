# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:24:35 2020

@author: USER
"""

# QHBoxLayout, QVBoxLayout은 여러 위젯을 수평으로 정렬하는 레이아웃 클래스
# QHBoxLayout, QVBoxLayout 생성자는 수평, 수직의 박스를 하나 만드는데,
# 다른 레이아웃 박스를 넣을 수도 있고 위젯을 배치할 수도 있다.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)
        
        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        
        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
                      
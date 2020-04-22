# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:18:18 2020

@author: USER
"""

# QTextBrowser 클래스는 하이퍼텍스트 네비게이션을 포함하는 리치 텍스트(서식있는 텍스트)
# 브라우저를 제공
# 이 클래스는 읽기 전용

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout

class MyApp(QWidget):
    
    def __init__(self):
       super().__init__()
       self.initUI()
    
    def initUI(self):
        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text)
        
        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)
        
        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.clear_text)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.le, 0)
        vbox.addWidget(self.tb, 1)
        vbox.addWidget(self.clear_btn, 2)
        
        self.setLayout(vbox)
        
        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 300)
        self.show()
        
    def append_text(self):
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()
        
    def clear_text(self):
        self.tb.clear()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())                
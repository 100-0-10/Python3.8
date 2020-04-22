# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:25:17 2020

@author: USER
"""

# 라디오 버튼은 하나의 버튼만 클릭 가능
# text() = 버튼의 텍스트를 반환
# setText() = 라벨에 들어갈 텍스트를 설정
# setChecked() = 버튼의 선택 여부를 설정
# isChecked() = 버튼의 선택 여부를 반환
# toggle() = 버튼의 상태를 변경

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        rbtn1 = QRadioButton('First Button', self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)
        
        rbtn2 = QRadioButton(self)
        rbtn2.move(50,70)
        rbtn2.setText('Second Button')
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QRadioButton')
        self.show()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
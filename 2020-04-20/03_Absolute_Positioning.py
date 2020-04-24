# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:11:07 2020

@author: USER
"""

# 절대적 배치(Absolute positioning) 방식은 각 위젯의 위치와 크기를 픽셀 단위로 설정해서 배치합니다.
# 절대 배치 방식을 사용할 때는 다음의 제약을 이해하고 있어야 합니다.

# 단점
# 크기가 변화되었을 때 자동으로 크기가 변화되지 않음(완전히 새로 고쳐야 함)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)
        
        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)
        
        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
                      
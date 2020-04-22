# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:38:58 2020

@author: USER
"""

# 슬라이더의 틱(tick)의 간격을 조절하기 위해서 setTickInterval() 메서드,
# 틱(tick)의 위치를 조절하기 위해서는 setTickPosition()

# QSlider.NoTicks         0          틱을 표시하지 않습니다.
# QSlider.TicksAbove      1          틱을 (수평) 슬라이더 위쪽에 표시
# QSlider.TicksBelow      2          틱을 (수평) 슬라이더 아래쪽에 표시
# QSlider.TicksBothSides  3          틱을 (수평) 슬라이더 양쪽에 표시
# QSlider.TicksTicksLeft  TicksAbove 틱을 (수직) 슬라이더 왼쪽에 표시

# 시그널
# valueChanged() = 슬라이더의 값이 변할 때 발생
# sliderPressed() = 사용자가 슬라이더를 움직이기 시작할 때 발생
# sli


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSlider, QDial
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(30, 30)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2)
        
        self.dial = QDial(self)
        self.dial.move(30, 50)
        self.dial.setRange(0, 50)
        
        btn = QPushButton('Default', self)
        btn.move(35, 160)
        
        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        btn.clicked.connect(self.button_clicked)
        
        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()
        
    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:06:18 2020

@author: USER
"""

# OProgressBar 위젯은 수평,수직의 진행 표시줄을 제공
# setMinimum()과 setMaximum()메서드로 진행 표시줄의 최소값과 최대값을 설정
# 또는 segRange() 메서드로 한 번에 범위를 설정할 수도 있습니다.
# 기본값은 0 과 99
# setValue() 메서드로 진행 표시줄의 진행 상태를 특정 값으로 설정할 수 있고,
# reset() 메서드는 초기 상태로 되돌립니다.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        
        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)
        
        self.timer = QBasicTimer()
        self.step = 0
        
        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
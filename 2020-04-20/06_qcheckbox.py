# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:04:53 2020

@author: USER
"""

# QCheckBox 위젯은 on(체크됨)/off(체크안됨)의 두 상태를 갖는 버튼을 제공
# 이 위젯은 하나의 텍스트 라벨과 함께 체크 박스를 제공
# stateChanged()
# isChecked()      > 체크/체크안됨 boolean값 반환
# setTristate()    > 변경없음상태 정수값 반환
# text() = 체크박스의 라벨텍스트 반환
# setText() = 체크박스의 라벨텍스트 설정
# isChecked() = 체크박스의 상태 반환(True/False)
# checkState() = 체크박스의 상태 반환(2/1/10)
# toggle() = 체크박스의 상태 변경
# 시그널 (html 이벤트와 같음)
# pressed() = 체크박스를 누를때 신호발생
# released() = 체크박스를 뗄 때 신호 발생
# clicked() = 체크박스를 클릭할 때 신호발생
# stateChanged() = 체크박스의 상태가 바뀔 때 신호 발생

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        
        
        self.setWindowTitle('QCheckbox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:24:50 2020

@author: USER
"""

### Googletrans - 파이썬을 위한 구글 번역 API ###
'''
Googletrans는
구글 번역 API(Google Translate API)를 구현한 파이썬 라이브러리

파이썬과 Googletrans를 이용해서
무료로 그리고 무제한으로 구글의 번역 기능을 사용할 수 있다.
'''

# Googletrans 설치
'''
pip install googletrans
conda install -c conda-forge googletrans
명령 프롬프트에서 pip 또는 conda를 통해서 설치를 진행
'''


### Googletrans 기본 사용 ###
'''
Googletrans 라이브러리를 이용해서
간단한 문장을 특정 언어로 (구글) 번역하고,
언어를 자동 감지하는 기능을 사용
'''

# 1. 번역하기
# googletrans에서 Translator 를 불러오기

from googletrans import Translator

translator = Translator()

# translate() 에 번역할 문장을 입력해주면, 아래 같은 결과를 출력.
print(translator.translate('안녕하세요'))

'''
Translated(src = ko, dest = en, text = Hi, pronunciation = None, extra_data = "{'})
Translated 객체는 번역이 이루어진 결과를 나타내는 객체.
'''

# translator.translate('안녕하세요').text를 출력하면 번역된 문장이 출력
print(translator.translate('안녕하세요').text)



'''
src와 dest에 언어 코드를 입력해줌으로써
source 언어와 destination 언어를 설정할 수 있다.
'''
from googletrans import Translator

translator = Translator()
print(translator.translate('안녕하세요', src = 'ko', dest = 'ja'))
# Translated(src=ko, dest=ja, text=こんにちは, pronunciation=Kon'nichiwa, extra_data="{'translat...")

print(translator.translate('안녕하세요', src = 'ko', dest = 'ja').text)
# こんにちは

print(translator.translate('안녕하세요', src = 'ko', dest = 'ja').pronunciation)
# Kon'nichiwa







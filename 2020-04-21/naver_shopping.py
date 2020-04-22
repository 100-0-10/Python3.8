# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:40:46 2020

@author: USER
"""

import errno
from bs4 import BeautifulSoup

import requests, re, os
from urllib.request import urlretrieve #추가

# 저장 폴더를 생성
try:
    if not (os.path.isdir('health')):
        os.makedirs(os.path.join('health'))
        print("health 폴더 생성 성공!")
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패!")
        exit()
        
        
# 웹 페이지를 열고 소스코드를 읽어오는작업
html = requests.get("https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000008")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

# 요일별 웹툰영역 추출하기

data1_list = soup.findAll('ul', {'class' : 'type_normal'})
print(data1_list)

# 전체 웹툰 리스트
li_list = []

for data1 in data1_list:
    #제목 + 썸네일 영영 추출
    li_list.extend(data1.findAll('li'))
    # 해당 부분을 찾아 li_list와 병합
print(li_list)

# 각각 썸네일과 제목 추출하기

for div in li_list:
    img = div.find('img')
    img_src = img['data-original']
    title = img['alt']
    # print(title, img_src)
    # 해당 영역의 글자가 아닌 것은 ''로 치환시킨다.
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)
    # 주소, 파일경로 + 파일명 + 확장자
    urlretrieve(img_src, './health/' + title + '.jpg')
    
    


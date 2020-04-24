

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:33:02 2020

@author: USER
"""
import sqlite3
import errno
from bs4 import BeautifulSoup

import requests, re, os
from urllib.request import urlretrieve #추가


html = requests.get("https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000008")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()


# 요소 1개 찾기(find)
# 미세먼지 정보가 있는 div 요소만 추출
data1_list = soup.findAll('ul', {'class' : 'type_normal'})
print(data1_list)


# 전체 웹툰 리스트
li_list = []

for data1 in data1_list:
    #제목 + 썸네일 영영 추출
    li_list.extend(data1.findAll('li'))
    # 해당 부분을 찾아 li_list와 병합
print(li_list)

con = sqlite3.connect("c:/spyder_python/2020-04-21/health.db")
cursor = con.cursor()

# cursor.execute("CREATE TABLE price(title text, price int)")


for div in li_list:
    img = div.find('img')
    title = img['alt']
    price = div.find('span', {'class' : 'num'}).text
    cursor.execute ('insert into price values (?,?)', (title, price))
    
cursor.execute('select * from price')
div = cursor.fetchall()
con.commit
# con.close()

    
# 평균 /최대 /최소 4분위 값을 각각 구하시오.
# 읽어들인 데이터를 MatplotLib의 선형차트로 출력하시오.










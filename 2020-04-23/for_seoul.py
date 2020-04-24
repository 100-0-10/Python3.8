# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:13:21 2020

@author: USER
"""



import folium        # 지도 시각화 작업 모듈
import webbrowser    # 웹 브라우저 사용을 위한 모듈

from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import seaborn as sns
import platform
import pandas as pd
import numpy as np


CCTV_Seoul = pd.read_csv('./data/01. CCTV_result.csv', encoding = 'utf-8')
CCTV_Seoul = pd.pivot_table(CCTV_Seoul, index = '구별', aggfunc = np.sum)
CCTV_Seoul.head()

import json

geo_path = './data/02. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding = 'utf-8'))

map = folium.Map(location = [37.5502, 126.982], zoom_start = 8)

map.choropleth(geo_data=geo_str,
               data = CCTV_Seoul['외국인비율'],
               columns = [CCTV_Seoul.index, CCTV_Seoul['외국인비율']],
               fill_color = 'Blues',
               key_on = 'feature.id')


map
map.save('folium_kr5.html')
webbrowser.open_new("folium_kr5.html")    
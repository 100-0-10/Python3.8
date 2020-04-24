# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:27:32 2020

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


pop_Seoul = pd.read_csv('./folium_Korea/Total_People_2018.csv', encoding = 'utf-8')
pop_Seoul.head()

import json


geo_path = './folium_Korea/TL_SCCO_SIG_WGS84.json'
geo_str = json.load(open(geo_path, encoding = 'euc-kr'))

pop_Seoul = pd.pivot_table(pop_Seoul, index = 'Code', aggfunc = np.sum)

map = folium.Map(location = [37.5502, 126.982], zoom_start = 8)

map.choropleth(geo_data=geo_str,
               data = pop_Seoul['Population'],
               columns = [pop_Seoul.index, pop_Seoul['Population']],
               fill_color = 'Blues',
               key_on = 'feature.properties.SIG_CD')


map
map.save('folium_kr4.html')
webbrowser.open_new("folium_kr4.html")    
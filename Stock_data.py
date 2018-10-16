# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import datetime
import time
import pandas as pd




url = 'http://www.twse.com.tw/fund/BFI82U'
list_req = requests.get(url)
soup = BeautifulSoup(list_req.content, "html.parser")
getjson=json.loads(soup.text)

iilist=[]
# 判斷請求是否成功
if getjson['stat'] != 'no satisfied data!': 
    iilist=getjson['data'][3][1:]

# 判斷是否為空值
if len(iilist) != 0:
    count=0
    for i in iilist:
        count += int(i.replace(',',''))
    # 顯示結果
    print('日期 ＝ ' + getjson['title'])
    print('三大法人合計 ＝ ' + str(count))

else:
    print('Please check your stock ID')

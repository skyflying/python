# -*- coding: utf-8 -*-
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#設定爬蟲股票代號
sid = '0050'

#設定爬蟲時間
start = datetime.datetime.now() - datetime.timedelta(days=360)
end = datetime.date.today()


#導入pandas_datareader
from pandas_datareader import data

# 與yahoo請求，套件路徑因版本不同
pd.core.common.is_list_like = pd.api.types.is_list_like 

# 取得股票資料
stock_dr = data.get_data_yahoo(sid+'.TW', start, end)
stock_dr.tail(10)

#線型圖，收盤價、5日均線、20日均線、60日均線
plt.figure()
stock_dr['Adj Close'].plot(figsize=(16, 8))
stock_dr['Adj Close'].rolling(window=5).mean().plot(figsize=(16, 8), label='5_Day_Mean')
stock_dr['Adj Close'].rolling(window=20).mean().plot(figsize=(16, 8), label='20_Day_Mean')
stock_dr['Adj Close'].rolling(window=60).mean().plot(figsize=(16, 8), label='60_Day_Mean')

#顯示側標
plt.legend(loc='upper right', shadow=True, fontsize='x-large')

#顯示標題
plt.title(sid+'_datareader')




#導入fix_yahoo_finance
import fix_yahoo_finance as yf

#把資料抓到本機
yf.pdr_override() 

# 取得股票資料
stock_yf = yf.download(sid+'.TW', start, end)
stock_yf.tail(10)

#線型圖，收盤價、5日均線、20日均線、60日均線
plt.figure()
stock_yf['Adj Close'].plot(figsize=(16, 8))
stock_yf['Adj Close'].rolling(window=5).mean().plot(figsize=(16, 8), label='5_Day_Mean')
stock_yf['Adj Close'].rolling(window=20).mean().plot(figsize=(16, 8), label='20_Day_Mean')
stock_yf['Adj Close'].rolling(window=60).mean().plot(figsize=(16, 8), label='60_Day_Mean')

#顯示側標
plt.legend(loc='upper right', shadow=True, fontsize='x-large')

#顯示標題
plt.title(sid+'_yahoo_finance')
plt.show()






#導入twstock
import twstock

#用fetch_from抓取資料
data=twstock.Stock(sid)

#指定日期放入dataframe裡
stock_tw = pd.DataFrame(data.fetch_from(2017,1))
stock_tw.tail(10)

#設定index
stock_tw.set_index('date', inplace = True)
stock_tw.tail(10)

#線型圖，收盤價、5日均線、20日均線、60日均線
plt.figure()
stock_tw['close'].plot(figsize=(16, 8))
stock_tw['close'].rolling(window=5).mean().plot(figsize=(16, 8), label='5_Day_Mean')
stock_tw['close'].rolling(window=20).mean().plot(figsize=(16, 8), label='20_Day_Mean')
stock_tw['close'].rolling(window=60).mean().plot(figsize=(16, 8), label='60_Day_Mean')

#顯示側標
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.show()
#顯示標題
plt.title(sid+'_twstock')
plt.show()
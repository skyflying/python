import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from pandas_datareader import data, wb
from datetime import datetime
from yahoo_finance import Share






end=dateime.now()
start=datetime(end.year-1,end.month,end.day)
bitcoin=data.DataReader('BTCUSD=X','yahoo',start,end)

bitcoin['Adj Close'].plot(legend=True)
plt.show()
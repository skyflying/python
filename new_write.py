# -- coding: utf-8 --
import urllib2
from bs4 import BeautifulSoup
import pandas as pd
req = urllib2.Request('http://tw.yahoo.com')
response=urllib2.urlopen(req)
html = response.read()

print html


#讀表格
import urllib2
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.stockq.org/market/asia.php'
table = pd.read_html(url)[4]
print table
table1 = table.drop(table.columns[[0,1,2,3,4]],axis=0)
table1 = table.drop(table.columns[9:],axis=1)
print table1


#抓證券
#python3
import requests
from bs4 import BeautifulSoup
import pandas as pd

def getList():
    url = "http://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
    res = requests.get(url, verify = False)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    table = soup.find("table", {"class" : "h4"})
    c = 0
    for row in table.find_all("tr"):
        data = []
        for col in row.find_all('td'):
            col.attrs = {}
            data.append(col.text.strip().replace('\u3000', ''))
        
        if len(data) == 1:
            pass # title 股票, 上市認購(售)權證, ...
        else:
            print(data)

getList()
# -- coding: utf-8 --


import requests
from bs4 import BeautifulSoup


url="https://emap.pcsc.com.tw/EMapSDK.aspx"

form={
	"commandid": "SearchStore",
	"city": "台北市",
	"town": "大安區",
	"Roadname":"",
	"ID":"",
	"StoreName":"",
	"SpecialStore_Kind":"",
	"leftMenuChecked":"",
	"address":"",
	}
	
res=requests.post(url,data=form)
soup=BeautifulSoup(res.content,'xml')
data=soup.findAll('GeoPosition')




for row in data:
	name=row.find('POIName').text
	address=row.find('Address').text
	tel=row.find('Telno').text
	x=row.find('X').text
	y=row.find('Y').text
	print name,address,tel,x,y

# -*- coding: big5 -*-
import requests , select , sys, csv ,re
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('big5')

res = requests.get('https://www.ptt.cc/bbs/Gamesale/M.1491663975.A.EB7.html',verify=False)
soup =  BeautifulSoup(res.text,"html.parser")

f = open("E:/Gamesale_word.csv","w")
w = csv.writer(f)
w.writerow([u'作者', u'日期', u'標題', u'價格'])

main_content = soup.find(id="main-content")
metas = main_content.select('div.article-metaline')
#print metas #文章名稱和部分資訊
filtered = [ v for v in main_content.stripped_strings if v[0] not in [u'※',u'◆'] and  v[:2] not in [u'--'] ]
#print filtered #文章名稱和部分資訊

#filtered = [_f for _f in filtered if _f]
content = ' '.join(filtered)
content = re.sub(r'(\s)+', '', content )
#print(content)
number_start = content.index(u'價')
number_end = content.index(u'交')

author = metas[0].select('span.article-meta-value')[0].string
title = metas[1].select('span.article-meta-value')[0].string
date = metas[2].select('span.article-meta-value')[0].string
price = content[number_start+3 : number_end-2]

data = [ [author, date, title, price]] #要注意一下存的格()  []
w.writerows(data)

f.close()
print("End")



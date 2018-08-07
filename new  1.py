import numpy as np
import pandas as pd
import urllib  
import urllib2  
from bs4 import BeautifulSoup


request = urllib2.Request("http://tw.yahoo.com")
response = urllib2.urlopen(request)
print response.read()
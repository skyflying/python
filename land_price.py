
import os
import pandas as pd
import numpy


for f in os.listdir('lvrdata2'):
    path ='lvrdata2/{}/A_lvr_land_A2.csv'
    print path.format(f)
    

    df = pd.read_csv(path. format(f), encoding = 'big5')
    dflist. append(df)

dfall=pd.concat(dflist)
dfall.describe()
dfall.to_excel('lvr_data.xls')
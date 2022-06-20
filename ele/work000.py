#coding: utf-8 
import re
import os
from os import path
import pyautogui as pa
import time
import numpy as np
import pandas as pd

path = 'https://powergrid.chuden.co.jp/goannai/hatsuden_kouri/takuso_kyokyu/ryokin/imbalance/imbalancefile/'


ystart = 2019
mstart = 4
#end = '202203'
yend = 2019
mend = 12

if ystart < yend:
    fromytoy = [ystart, yend]
    frommtom = [mstart, mend]
else:
    year = ystart
    period_m = range(mstart, mend+1)
    period = []
    for m in period_m:
        if m < 10:
            period.append(str(year) + '0' +str(m))
        else:
            period.append(str(year) + str(m))
    print(period)

for p in period:
    root_csvname = path + '04_chubu_imbalance_confirmed_' + p + '.csv'
    print(root_csvname)
    df1 = pd.read_csv(root_csvname, header=2, encoding='shiftJIS')
    if p == period[0]:
        df = df1.copy()
    else:
        df = pd.concat([df, df1], axis=0)

df = df.dropna()
df.index = np.arange(len(df)).tolist()
df.columns = ['T', 'yyyymmdd', 'timeframe', 'HH:MM', 'to', 'unit price[yen/kWh]', 'inbalance[kWh]']
df = df.drop(['T', 'timeframe', 'to'], axis=1)
df['yyyymmdd'] = df['yyyymmdd'].astype('int')
df['yyyy'] = df['yyyymmdd'].astype(str).str[:4]
df['mm'] = df['yyyymmdd'].astype(str).str[4:6]
df['dd'] = df['yyyymmdd'].astype(str).str[-2:]
df['yyyymmdd'] = df['yyyy'].str.cat([df['mm'], df['dd']], sep='/')
df['timestamp'] = df['yyyymmdd'].str.cat(df['HH:MM'], sep=' ')
df = df.drop(['yyyy', 'mm', 'dd'], axis=1)

df.to_csv('./output/04_chubu_imbalance_confirmed_' + period[0] + '_' + period[-1] + '.csv', encoding="shift-jis")
print(df)

print('finish')

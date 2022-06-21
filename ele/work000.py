#coding: utf-8 
import re
import os
from os import path
import errno
import configparser
import json
import numpy as np
import pandas as pd

# -202202
PATH1 = 'https://powergrid.chuden.co.jp/goannai/hatsuden_kouri/takuso_kyokyu/ryokin/imbalance/imbalancefile'
# 202203-202206
PATH2 = 'https://www.imbalanceprices-cs.jp/public/price'

def read_config(param_file):
    print(param_file)
    if not os.path.exists(param_file):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), param_file)

    config_ini = configparser.ConfigParser() 
    config_ini.read(param_file, encoding='utf-8')
    read_default = config_ini['DEFAULT']
    ystart = int(read_default.get('StartYear'))
    mstart = int(read_default.get('StartMonth'))
    yend = int(read_default.get('EndYear'))
    mend = int(read_default.get('EndMonth'))
    return ystart, mstart, yend, mend

def to_strmonth(month):
    if month < 10:
        str_month = '0' +str(month)
    else:
        str_month =  str(month)
    return str_month

def get_path(year, month):
    str_year = str(year)
    str_month = to_strmonth(month)
    if year >= 2022 and month >= 3:
        path_flag = 2
        path = PATH2
        # rev. number must be get latest version for each month
        # but input rev. number directly in 20220621
        if month == 3:
            revnum = '11'
        elif month == 4:
            revnum = '08'
        elif month == 5:
            revnum = '10'
        elif month == 6:
            revnum = '01'
        else:
            # site_path : 'https://www.imbalanceprices-cs.jp/imbalance-price-list'
            print('User must add the latest version number refered from price-list site.')
        filename = str_year + '/' + str_month + '/' + str_year + str_month + '_imbalance-price_' + revnum
        header_num = 4
    else:
        path_flag = 1
        path = PATH1
        filename = '04_chubu_imbalance_confirmed_' + str_year + str_month
        header_num = 2
    return path, filename, path_flag, header_num

def drop_unit_df(df, path_flag):
    if path_flag == 1:
        df.columns = ['T', 'yyyy/mm/dd', 'timeframe', 'HH:MM', 'to', 'unit price for upper imbalance[yen/kWh]', 'imbalance[kWh]']
        df = df.drop('imbalance[kWh]', axis=1)
        df['unit price for lower imbalance[yen/kWh]'] = df['unit price for upper imbalance[yen/kWh]']
    elif path_flag == 2:
        area_list = ['Hokkaido', 'Hokkaido S', 'Tohoku', 'Tohoku S', 'Tokyo', 'Tokyo S', 'Chubu', 'Chubu S', 'Hokuriku', 'Hokuriku S', 'Kansai', 'Kansai S', 'Chugoku', 'Chugoku S', 'Shikoku', 'Shikoku S', 'Kyushu', 'Kyushu S']
        df.columns = ['T', 'yyyy/mm/dd', 'timeframe', 'HH:MM', 'to'] + ['upper ' + area for area in area_list] + ['lower ' + area for area in area_list]
        df = df[['T', 'yyyy/mm/dd', 'timeframe', 'HH:MM', 'to', 'upper Chubu', 'lower Chubu']]
        df.columns = ['T', 'yyyy/mm/dd', 'timeframe', 'HH:MM', 'to', 'unit price for upper imbalance[yen/kWh]', 'unit price for lower imbalance[yen/kWh]']
    return df

#start : '201904', end : '202203'
(ystart, mstart, yend, mend) = read_config('scraping_config.ini')

if mstart > 12 or mstart < 1 or mend > 12 or mend < 1:
    print('Error: mstart/mend is wrong.')
p_start = str(ystart) + to_strmonth(mstart)
p_end = str(yend) + to_strmonth(mend)
print('from: ', p_start)
print('to: ', p_end)

# make period list
if ystart < yend:
    period = []
    for year in range(ystart, yend+1):
        if year == ystart:
            p = [(year, month) for month in range(mstart, 13)]
        elif year == yend:
            p = [(year, month) for month in range(1, mend+1)]
        else:
            p = [(year, month) for month in range(1, 13)]
        period += p
elif ystart == yend:
    year = ystart
    period = [(year, month) for month in range(mstart, mend+1)]
else:
    print('Error: ystart > yend.')
print(period)

# get csvdata though scraping
for (year, month) in period:
    (path, filename, path_flag, header_num) = get_path(year, month)
    root_csvname = path + '/' + filename
    print(root_csvname)
    df1 = pd.read_csv(root_csvname + '.csv', header=header_num, encoding='shiftJIS')
    df1 = drop_unit_df(df1, path_flag)
    if year == ystart and month == mstart:
        df = df1.copy()
    else:
        df = pd.concat([df, df1], axis=0)

# drop concated dataframe
df = df.dropna()
df.index = np.arange(len(df)).tolist()
df = df.drop(['T', 'timeframe', 'to'], axis=1)
df['yyyy/mm/dd'] = df['yyyy/mm/dd'].astype('int')
df['yyyy'] = df['yyyy/mm/dd'].astype(str).str[:4]
df['mm'] = df['yyyy/mm/dd'].astype(str).str[4:6]
df['dd'] = df['yyyy/mm/dd'].astype(str).str[-2:]
df['yyyy/mm/dd'] = df['yyyy'].str.cat([df['mm'], df['dd']], sep='/')
df['timestamp'] = df['yyyy/mm/dd'].str.cat(df['HH:MM'], sep=' ')
df = df.drop(['yyyy', 'mm', 'dd'], axis=1)

df.to_csv('./output/chubu_imbalance_confirmed_' + p_start + '_' + p_end + '.csv', encoding="shift-jis")
print(df)

grouped = df.groupby('yyyy/mm/dd')
df1 = grouped.agg('mean')
df1['yyyy/mm/dd'] = df1.index
df1.index = np.arange(len(df1)).tolist()
df1.to_csv('./output/chubu_imbalance_confirmed_' + p_start + '_' + p_end + '_mean.csv', encoding="shift-jis")
print(df1)
print('mean: ', df['unit price for lower imbalance[yen/kWh]'].mean())

print('finish')
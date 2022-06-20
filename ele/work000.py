import numpy as np
import pandas as pd

path = 'https://powergrid.chuden.co.jp/goannai/hatsuden_kouri/takuso_kyokyu/ryokin/imbalance/imbalancefile/'
#https://www.imbalanceprices-cs.jp/imbalance-price-list

#fpath = 'https://raw.githubusercontent.com/computational-sediment-hyd/japaneseriverdb/master/data_pickup/8909090001kui.csv'

ystart = 2019
mstart = 4
#end = '202203'
yend = 2019
mend = 7

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
    df1 = pd.read_csv(root_csvname, encoding='shiftJIS')
    if p == period[0]:
        df = df1.copy()
    else:
        df = pd.concat([df, df1], axis=0)

df.to_csv('./output/04_chubu_imbalance_confirmed_' + period[0] + '_' + period[-1] + '.csv')

print(df)

print('finish')
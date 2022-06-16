#coding: utf-8 
import re
import os
from os import path
import errno
import configparser
import json
import traceback
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_config(param_file):
    def _read_period(ini_period):
        period = ini_period.split(', ')
        period = [period[0].split('[')[1], period[1].split(']')[0]]
        return period
    
    print(param_file)
    if not os.path.exists(param_file):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), param_file)

    config_ini = configparser.ConfigParser() 
    config_ini.read(param_file, encoding='utf-8')
    read_default = config_ini['DEFAULT']
    x_list = json.loads(read_default.get('XList'))
    tra_period = _read_period(read_default.get('TraPeriod'))
    pre_period = _read_period(read_default.get('PrePeriod'))
    modeling_mode = read_default.get('ModelingMode')
    return x_list, modeling_mode, tra_period, pre_period


def get_path():
    dir_base = os.path.abspath('..\\') 
    print(dir_base)
    return dir_base


def split_data(df, x_list, tra_period, test_period):
    def _list_check(list1, list2):
        return set(list1).issubset(list2)

    def _select_idx_dataframe(df, clm, txt):
        if _list_check(clm, np.arange(len(df.columns.tolist())).tolist()):
            df = pd.concat([df.iloc[:, 0], df.iloc[:, clm]], axis=1)
        else:
            df = 0
            print('input data does not contain' + txt + '.')
        return df

    def _select_clm_dataframe(df, period, txt):
        if _list_check(period, df.index.tolist()):
            df_ = df.loc[period[0]:period[1], :]
        else:
            df_ = 0
            print('input data does not contain' + txt + '.')
        return df_

    # x_select
    x_list = list(map(lambda x: x+1, x_list))
    df = _select_idx_dataframe(df, x_list, 'x_list')
    print('y = ', df.columns[0])
    print('x = ', df.columns[1:].tolist())

    # split
    print('training period: ', tra_period)
    print('predict period: ', test_period)
    df_tra = _select_clm_dataframe(df, tra_period, 'training period')
    df_test = _select_clm_dataframe(df, test_period, 'predict period')
    print('traning data')
    print(df_tra.shape)
    print(df_tra.head())
    print('validation data')
    print(df_test.shape)
    print(df_test.head())
    return df_tra, df_test


def fit_predict(df_tra, df_val, modeling_mode):
    from pkg import Model
    X_tra = df_tra.values[:, 1:]
    y_tra = df_tra.values[:, 0]
    X_val = df_val.values[:, 1:]
    y_val = df_val.values[:, 0]

    model = Model.Model(modeling_mode)
    model.fit(X_tra, y_tra)
    y_pre = model.predict(X_val)

    y_array = np.vstack([y_pre, y_val]).T
    df_y_pre = pd.DataFrame(y_array, 
                            index = df_val.index, 
                            columns=[df_val.columns[0]+'_pre', df_val.columns[0]+'_act'])
    print(df_y_pre.describe())
    print(df_y_pre.head())
    return df_y_pre

def draw_trend_chart(df, fig_file_name):
    fig = plt.figure(figsize=(6,4))
    fig.patch.set_facecolor('white')
    ax = fig.add_subplot(1,1,1)
    x = pd.to_datetime(df.index)
    print('from ', x[0])
    print('to ', x[-1])
    
    ax.plot(x, df.iloc[:, 0], "C1", label=df.columns[0], lw=0.5)
    ax.plot(x, df.iloc[:, 1], "C0", label=df.columns[1], lw=0.5)
    ax.set_xlabel('timestamp', fontsize=10)
    ax.set_ylabel('y predict/actual', fontsize=10)
    ax.legend(loc='center', bbox_to_anchor=(0.5, 1.1), ncol=2)
    ax.tick_params(direction = "in")

    labelss = ax.get_xticklabels()
    plt.setp(labelss, rotation=60)
    plt.tick_params(labelsize=8)
    plt.tight_layout()
    plt.savefig(fig_file_name, bbox_inches="tight")


def main():
    print('|--------------|')
    print('read config file')
    (x_list, modeling_mode, tra_period, pre_period) = read_config(os.getcwd() + '\\predict_config.ini')
    print('|--------------|')


    print('|--------------|')
    print('read input file')
    dir_base = get_path()
    df = pd.read_csv(dir_base + '\\input\\data_preprocessed.csv', index_col=0)
    print('|--------------|')


    print('|--------------|')
    print('select/split data')
    df_tra, df_val = split_data(df, x_list, tra_period, pre_period)
    df_tra.to_csv(dir_base + "\\output\\tra.csv")
    df_val.to_csv(dir_base + "\\output\\val.csv")
    print('|--------------|')


    print('|--------------|')
    print('fit/predict')
    df_y_pre = fit_predict(df_tra, df_val, modeling_mode)
    print('|--------------|')

    print('|--------------|')
    print('save output files')
    df_y_pre.to_csv(dir_base + "\\output\\predict.csv")
    print('|--------------|')

    print('|--------------|')
    print('draw trend chart')
    draw_trend_chart(df_y_pre, dir_base + "\\output\\predict.png")
    print('|--------------|')


try:
    main()

except Exception:
    print('error: dump error msg to log file.')
    new_dir_path = os.getcwd() + '\\log'
    os.mkdir(new_dir_path)
    f = open(new_dir_path + '\\log_dump.txt', 'w')
    f.write(traceback.format_exc())
    f.close()

print('finish')
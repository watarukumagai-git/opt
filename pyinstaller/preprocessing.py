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
from sklearn.preprocessing import LabelEncoder

def read_config(param_file):
    print(param_file)
    if not os.path.exists(param_file):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), param_file)

    config_ini = configparser.ConfigParser()
    config_ini.read(param_file, encoding='utf-8')
    read_default = config_ini['DEFAULT']
    flag_list = [read_default.get('SplitTimestamp'), read_default.get('EncodeLabel'), read_default.get('EncodeOnehot')]
    flag_list = list(map(lambda x: json.loads(x.lower()), flag_list))
    read_label = config_ini['ENCODELABEL']
    encode_label_list = json.loads(read_label.get('XList'))
    read_onehot = config_ini['ENCODEONEHOT']
    encode_onehot_list = json.loads(read_onehot.get('XList'))
    return flag_list, encode_label_list, encode_onehot_list


def get_path():
    dir_base = os.path.abspath('..\\')
    print(dir_base)
    return dir_base


def preprocessing(df, flag_list, encode_label_list, encode_onehot_list):
    def _add_timestamp_variable(df):
        def _check_timestamp(l):
            if '/' in l:
                type_ = '/'
            elif '-' in l:
                type_ = '-'
            else:
                type_ = 'error: timestamp column is wrong.'
                print(type_)
            return type_

        def _add_weekday(df, type_):
            format_ = '%Y' + type_ + '%m' + type_ + '%d'
            df['yyyy-mm-dd'] = pd.to_datetime(df['yyyy/mm/dd'], format=format_)
            df['weekday'] = df['yyyy-mm-dd'].dt.strftime('%a')
            df = df.drop(['yyyy-mm-dd'], axis=1)
            return df

        df_ = df.copy()
        df_['timestamp'] = df_.index
        df_temp = df_['timestamp'].str.split(' ', expand=True)
        df_temp.columns = ['yyyy/mm/dd', 'HH:MM']
        type_ = _check_timestamp(list(df_temp['yyyy/mm/dd'].tolist()[0]))
        df_temp = _add_weekday(df_temp, type_)
        df_temp2 = df_temp['yyyy/mm/dd'].str.split(type_, expand=True)
        df_temp2.columns = ['year', 'month', 'day']
        df_temp = df_temp.drop(['yyyy/mm/dd'], axis=1)
        df_ = pd.concat([df_temp2, df_temp], axis=1)
        return df_
    
    def _encode_label(df, clm):
        def _encode_label_unit(df, clm):
            le = LabelEncoder()
            le = le.fit(df[clm])
            df[clm] = le.transform(df[clm])
            return df

        if len(clm) > 1:
            for i in clm:
                df = _encode_label_unit(df, i)
        else:
            df = _encode_label_unit(df, clm)
        return df

    def _encode_onehot(df, clm):
        df = pd.get_dummies(df, prefix=clm, prefix_sep='-')
        return df
    
    def _get_clm(encode_list, df, split_timestamp, clm_time=[]):
        encode_list = list(map(lambda x: x+1, encode_list))
        encode_list = df.iloc[:, encode_list].columns.tolist()
        if flag_list[0] == True:
            if len(encode_list) == 0:
                clm = clm_time
            else:
                clm = encode_list + clm_time
        else:
            clm = encode_list
        return clm
    

    if flag_list[0] == True:
        df_time = _add_timestamp_variable(df)
        clm_time = df_time.columns.to_list()
        df = pd.concat([df, df_time], axis=1)
    else:
        clm_time = []

    if flag_list[1] == True:
        if (flag_list[0] == False) and (len(encode_label_list) == 0):
            print('skip label-encoding')
        else:
            clm = _get_clm(encode_label_list, df, flag_list[0], clm_time)
            df = _encode_label(df, clm)

    if flag_list[2] == True:
        if (flag_list[0] == False) and (len(encode_onehot_list) == 0):
            print('skip onehot-encoding')
        else:
            clm = _get_clm(encode_onehot_list, df, flag_list[0], clm_time)
            df = _encode_onehot(df, clm)
    return df

def filtering(df):
    df = df.dropna()
    return df

def main():
    print('|--------------|')
    print('read config file')
    (flag_list, encode_label_list, encode_onehot_list) = read_config(os.getcwd() + '\\preprocessing_config.ini')
    print('|--------------|')


    print('|--------------|')
    print('read input file')
    dir_base = get_path()
    df = pd.read_csv(dir_base + '\\input\\input.csv', index_col=0)
    print(df.describe())
    print('|--------------|')


    print('|--------------|')
    print('filtering')
    df = filtering(df)
    print('|--------------|')


    print('|--------------|')
    print('preprocessing')
    print(flag_list)
    df = preprocessing(df, flag_list, encode_label_list, encode_onehot_list)
    print(df.describe())
    print(df.head())
    print(df.tail())
    print('|--------------|')

    print('|--------------|')
    print('save output file')
    df.to_csv(dir_base + '\\input\\data_preprocessed.csv')
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
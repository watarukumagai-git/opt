# -*- coding: utf-8 -*-
import pathlib
import re
import glob
import os
from os import path
import numpy as np
import pandas as pd
import datetime

subs_month = {'January': '1', 'February': '2', 'March': '3', 'April': '4', 'May': '5', 'June': '6', 'July': '7', 'August': '8', 'September': '9', 'October': '10', 'November': '11', 'December': '12'}

def trans_word2(input):
    print('({})'.format('|'.join(map(re.escape, subs_month.keys()))))
    return re.sub('({})'.format('|'.join(map(re.escape, subs_month.keys()))), lambda m: subs_month[m.group()], input)

def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def get_file_dir_list(root_path, list_type):
    if list_type == 'dir':
        dir_list = [f for f in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, f))]
        return dir_list
    elif list_type == 'file':
        file_list = glob.glob(root_path + '*.csv')
        file_name_list = [one_file.rsplit('\\', 1)[1].split('.')[0] for one_file in file_list]
        #dir_path = pathlib.Path(work_path)
        #file_list = dir_path.glob('*.csv')
        return file_list, file_name_list

def replace_str_inlist(l, frm, to):
    l = [clm.replace(frm, to) if frm in clm else clm for clm in l]
    return l

def split_str_inlist(l, tt, axis):
    if axis == 'left':
        l = [clm.split(tt, 1)[0] if tt in clm else clm for clm in l]
    else:
        l = [clm.split(tt, 1)[1] if tt in clm else clm for clm in l]
    return l

def replace_list(l, dict):
    for (bfr, aft) in dict.items():
        l = replace_str_inlist(l, bfr, aft)
    return l

def unit_convert(df, unit_clm):
    dict = {'µ': 'mu', 
            '°C': 'deg C',
            ' N': '',
            ' Cl2': '',
            'dimensionless': '-'}
    df[unit_clm] = replace_list(df[unit_clm].tolist(), dict)
    #d_tagid = df.to_dict()
    print(df[unit_clm].tolist())
    return df

def tagid_convert(df):
    dict = {'-': '_', 
            'LasVirgenes/UF/': '', 
            '/Val': '', 
            '_CVOut': '', 
            'Status': 'RO_Status', 
            'Grab_Sample': 'sample', 
            'Feed_Total': 'RO_Feed_Total', 
            'Product_Total': 'RO_Product_Total', 
            'Reject_Total': 'RO_Reject_Total'}
    df.columns = replace_list(df.columns.tolist(), dict)
    return df

def tagid_edit(l):
    new_l = []
    l = replace_list(l, {' ': '_',})
    for clm in l:
        # delete '(unit)'
        matchObj = re.search(r'(?<=\().+?(?=\))', clm)
        if matchObj:
            clm = re.sub('\(' + matchObj.group() + '\)', '', clm)
        # extract '(tagid)' and replace tagid
        matchObj = re.search(r'(?<=\[).+?(?=\])', clm)
        if matchObj:
            clm = matchObj.group()
            #clm = re.sub('\[' + tagid + '\]', '', clm) + '_' + tagid
        # replace 'Duty ' to '_duty'
        matchObj = re.search(r'Duty_*', clm)
        if matchObj:
            clm = re.sub(matchObj.group(), '', clm)
            clm = clm + 'duty'
        # replace 'Reference ' to '_reference'
        matchObj = re.search(r'Reference_*', clm)
        if matchObj:
            clm = re.sub(matchObj.group(), '', clm)
            clm = clm + 'reference'
        # replace end '_' to ''
        if clm.endswith('_'):
            clm = clm.rstrip('_')
        new_l.append(clm)
    return new_l


def main():
    dir_base = path.dirname( path.abspath(__file__) )
    df_tagid = pd.read_csv(dir_base + '\\input\\Taglist\\Taglist_LVMWD.csv')
    df_tagid = df_tagid[['TagID','Description','Measurement Units']]
    df_tagid = unit_convert(df_tagid, 'Measurement Units')

    root_path = dir_base + '\\output'
    work_path = root_path + '\\master'
    save_path = root_path + '\\master_edit'
    my_makedirs(save_path)
    (file_list, file_name_list) = get_file_dir_list(work_path + '\\', list_type='file')
    print('file all = ', file_name_list)

    for i, one_file in enumerate(file_list):
        print('file name = ', file_name_list[i])
        df = pd.read_csv(one_file, index_col=0)
        # tagid more simple
        if 'day' in file_name_list[i]:
            # extract unit and tagid
            df.columns = tagid_edit(df.columns.tolist())
        df = tagid_convert(df)
        
        # add description and unit row
        df.loc['unit'] = 0
        df.loc['description'] = 0

        # get description and unit row from tagid list
        for tagid in df.columns:
            BOOL = df_tagid['TagID'].str.contains(tagid)            
            if BOOL.any():
                idx = df_tagid.index[BOOL].tolist()[0]
                df.loc['description', tagid] = df_tagid.loc[idx, 'Description']
                df.loc['unit', tagid] = df_tagid.loc[idx, 'Measurement Units']

        df.to_csv(save_path + '\\' + file_name_list[i] + '.csv')
    print('finish')
    
if __name__ == "__main__":
    main()

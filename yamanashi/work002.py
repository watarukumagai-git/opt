#coding: utf-8 
import glob
import os
from os import path
import shutil
import pandas as pd
import pypdf
import pdfplumber

def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def get_dir(dir_base):
    input_dir = dir_base + '\\input2'
    output_dir = dir_base + '\\output2'
    my_makedirs(input_dir)
    my_makedirs(output_dir)
    return input_dir, output_dir

def get_file_list(dir):
    file_list = glob.glob(dir)
    for i, file in enumerate(file_list):
        file_list[i] = file.rsplit('\\', 1)[1]
    print(file_list)
    return file_list

def pdf_to_text(pdf_path, export_dir):
    # PDFファイルを開く
    with pdfplumber.open(pdf_path) as pdf:
        # 最初のページを取得
        first_page = pdf.pages[0]
        # テキストを抽出
        text = first_page.extract_text()
        print(text)
    return text


def split_pdf_pages(src_path, dst_basepath):
    src_pdf = pypdf.PdfReader(src_path)
    filelist = []
    for i, page in enumerate(src_pdf.pages):
        dst_pdf = pypdf.PdfWriter()
        dst_pdf.add_page(page)
        filename = f'{dst_basepath}_{i}.pdf'
        dst_pdf.write(filename)        
        filelist.append(filename.split('\\')[-1])
    return filelist

def pullout_pdf_pages(src_path, s, e):
    reader = pypdf.PdfReader(src_path)
    writer = pypdf.PdfWriter()
    writer.add_page(reader.pages([s, e]))
    filename = src_path + '.pdf'
    writer.write(filename)

dir_base = path.dirname( path.abspath(__file__) )
inout_dir = get_dir(dir_base)
filelist = get_file_list(inout_dir[0] + '\\*')
for file in filelist:
    pullout_pdf_pages(inout_dir[0] + '\\' + file, 1, -1)

#src_path = inout_dir[0] + '\\cover_v.pdf'
#dst_basepath = inout_dir[1] + '\\cover_v'
#pdf_list = split_pdf_pages(src_path, dst_basepath)

src_path = inout_dir[0] + '\\' + 'cover_h.pdf'
dst_basepath = inout_dir[1] + '\\cover_h'
pdf_list2 = split_pdf_pages(src_path, dst_basepath)
pdf_list = pdf_list + pdf_list2

#file_list = get_file_list(inout_dir[1] + '\\*')
for filename in pdf_list:
    loadfile = inout_dir[1] + '\\' + filename
    export_dir = inout_dir[1]
    pdfname = pdf_to_text(loadfile, export_dir)
    shutil.move(loadfile, inout_dir[1] + '\\' + pdfname + '_表紙.pdf')

#(df_master, head_HHMM, tail_HHMM) = get_df_master(inout_dir, file_list)
#d_order = {'morning': 0, 'afternoon': 1, 'evening': 2, 'night': 3}

#clm_list = [('HH:MM', '30min'), ('timezone', 'timezone')]
#period_list = [('yyyy/mm', '%Y-%m', 'month', 'M'), ('yyyy', '%Y', 'year', 'Y')]
#file_head = inout_dir[1] + '\\spot_price_' + head_HHMM + '-' + tail_HHMM

#for strftime1, strftime2, period, resample in period_list:
#    # all average
#    df_all = df_master.resample(resample, label='left').mean()
#    df_all.to_csv(file_head + '_' + period + '.csv')
#
#for clm, name in clm_list:
#    # all average in each time
#    df_all_30min = df_master.groupby(clm).mean()
#    if clm == 'timezone':
#        df_all_30min = df_all_30min.reindex(index=['night', 'morning', 'afternoon', 'evening'])
#    df_all_30min.to_csv(file_head + '_' + name + '_all.csv')
#
#    for strftime1, strftime2, period, resample in period_list:
#        # all average in each month, year
#        df_period = df_master.copy()
#        df_period['timestamp'] = df_period.index
#        df_period[strftime1] = df_period['timestamp'].dt.strftime(strftime2)
#        #if clm == 'timezone' and strftime1 == 'yyyy/mm':
#        #    df_period['yyyy'] = df_period['timestamp'].dt.strftime('%Y')
#        df_period = df_period.groupby(by=[strftime1, clm], sort=False).mean()
#        #if clm == 'timezone':
#        #    if strftime1 == 'yyyy/mm':
#        #        df_period = df_period.sort_values(by=['yyyy', strftime1, clm], key=lambda col: col.map(d_order))
#        #    else:
#        #        df_period = df_period.sort_values(by=[strftime1, clm], key=lambda col: col.map(d_order))
#        df_period.to_csv(file_head + '_' + name + '_' + period + '.csv')

print('finish')
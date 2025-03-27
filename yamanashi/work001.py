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
    input_dir = dir_base + '\\input'
    output_dir = dir_base + '\\output'
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
        text = first_page.extract_text().replace(' ', '')
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

dir_base = path.dirname( path.abspath(__file__) )
inout_dir = get_dir(dir_base)

prefix_list = ['cover_v', 'cover_h']
pdf_list = []
for prefix in prefix_list:
    src_path = inout_dir[0] + '\\' + prefix + '.pdf'
    dst_basepath = inout_dir[1] + '\\' + prefix
    pdf_list = pdf_list + split_pdf_pages(src_path, dst_basepath)

#file_list = get_file_list(inout_dir[1] + '\\*')
for filename in pdf_list:
    loadfile = inout_dir[1] + '\\' + filename
    export_dir = inout_dir[1]
    pdfname = pdf_to_text(loadfile, export_dir)
    shutil.move(loadfile, inout_dir[1] + '\\' + pdfname + '_表紙.pdf')


print('finish')
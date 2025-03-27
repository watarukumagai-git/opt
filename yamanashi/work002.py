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
    for i in range(s, len(reader.pages)):
        writer.add_page(reader.pages[i])
    writer.write(src_path)

dir_base = path.dirname( path.abspath(__file__) )
inout_dir = get_dir(dir_base)
filelist = get_file_list(inout_dir[0] + '\\*')
for file in filelist:
    pullout_pdf_pages(inout_dir[0] + '\\' + file, 1, -1)

print('finish')
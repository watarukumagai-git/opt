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
    input_dir = dir_base + '\\input3'
    output_dir = dir_base + '\\output3'
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

def change_password(
    src_path, dst_path, src_password, dst_user_password=None, dst_owner_password=None
):
    src_pdf = pypdf.PdfReader(src_path)
    src_pdf.decrypt(src_password)

    dst_pdf = pypdf.PdfWriter()
    dst_pdf.clone_reader_document_root(src_pdf)

    d = {key: src_pdf.metadata[key] for key in src_pdf.metadata.keys()}
    dst_pdf.add_metadata(d)

    if dst_user_password is not None:
        dst_pdf.encrypt(dst_user_password, dst_owner_password)

    dst_pdf.write(dst_path)

def merge_pdf(filename, dir1, dir2, outdir):
    writer = pypdf.PdfWriter()
    prefix = filename.split('.')[0]
    # 表紙
    writer.append(dir2 + '\\' + prefix + '_表紙.pdf')
    # 本体
    pdf_pass = pypdf.PdfReader(dir1 + '\\' + filename)
    src_password = 'alliance'
    change_password(dir1 + '\\' + filename, dir1 + '\\' + filename, src_password)
    writer.append(dir1 + '\\' + filename)
    writer.write(outdir + '\\' + filename)

dir_base = path.dirname( path.abspath(__file__) )
inout_dir = get_dir(dir_base)
filelist = get_file_list(inout_dir[0] + '\\*')
for file in filelist:
    merge_pdf(file, inout_dir[0], dir_base + '\\output', inout_dir[1])

print('finish')
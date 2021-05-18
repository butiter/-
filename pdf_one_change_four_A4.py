import os
import sys, fitz
import datetime
import pdf2image
import pdfplumber
#外部库（暂未用到）：fitz,pdf2image
#外部库：PyMuPDF pdfplumber

ls_file_all = os.listdir()
ls_file_pdf = []
for i in ls_file_all:
    if i[-4:] == ".pdf":
        ls_file_pdf.append(i)
#已经将本文件夹下的所有pdf文件放入列表ls_file_pdf
 

def get_pdf_page(pdf_path):#获取pdf页数
    print("获取pdf页数中")
    f = pdfplumber.open(pdf_path)
    print("pdf页数获取成功")
    page = len(f.pages)
    return page


def pdf_to_png(pdffile):
    print("进入函数pdf转图片")
    doc = fitz.open(pdffile)
    print("文件打开成功")
    num = 1
    step = False
    for i in range(get_pdf_page(pdffile)):
        print("第"+str(i+1)+"张图片开始转换")
        page = doc.loadPage(i)  # PDF页数
        pix = page.getPixmap()
        if step:
            file_name = str(num) + "back"
            num += 1
        else:
            file_name = str(num)
        step = not step
        output ="../png/" + file_name + ".png"
        pix.writePNG(output)    #保存
        print("第"+str(i+1)+"张图片转换成功")

pdf_to_png("demo.pdf")

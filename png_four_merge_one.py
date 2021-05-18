import os
import sys, fitz
import datetime
import pdf2image
import pdfplumber
from os import listdir
from PIL import Image

#外部库（暂未用到）：fitz,pdf2image
#外部库：PyMuPDF pdfplumber

ls_file_all = os.listdir()
ls_file_png = []
for i in ls_file_all:
    if i[-4:] == ".png":#1234 2143
        ls_file_png.append(i)
#已经将本文件夹下的所有png文件放入列表ls_file_png

def pinjie(im_list,outname):
  
 # 图片转化为相同的尺寸
    ims = []
    for i in im_list:
        new_img = i.resize((1000, 1414), Image.ANTIALIAS)
        ims.append(new_img)
  
 # 单幅图像尺寸
    width, height = ims[0].size
  
 # 创建空白长图
    result = Image.new(ims[0].mode, (2480, 3508),color = (255, 255, 255))
  
 # 拼接图片
 #result.paste(im, box=(120, 170))
    result.paste(ims[0], box=(120, 170,120+1000,170+1414))
    result.paste(ims[1], box=(1240, 170,1240+1000,170+1414))
    result.paste(ims[2], box=(120, 1754,120+1000,1754+1414))
    result.paste(ims[3], box=(1240, 1754,1240+1000,1754+1414))
  
 # 保存图片
    result.save(outname)




#主函数  
im_list = [Image.open(fn) for fn in listdir() if fn.endswith('.png')]
#获取所有png图片


temp = 0

i = 0
while i < len(im_list):
    ls_print = []
    ls_print_back = []
    for j in range(4):
        name = str(j+1 + ( i // 8 ) * 4) + ".png"
        name_back = str(j+1 + ( i // 8 ) * 4) + "back.png"
        for k in im_list:
            if k.filename == name:
                ls_print.append(k)
            if k.filename == name_back:
                ls_print_back.append(k)
        name ="../ans/" + str(j+1 + ( i // 8 ) * 4 - 3) + "-" + name
        name_back ="../ans/" +  str(j+1 + ( i // 8 ) * 4 - 3) + "-" + name_back
    for m in ls_print:
        print(m.filename,"加入合并队列")
    pinjie(ls_print,name)
    print(str(j+1 + ( i // 8 ) * 4 - 3)+"-"+str(j+1 + ( i // 8 ) * 4)+"合并完成")
    pinjie(ls_print_back,name_back)
    print(str(j+1 + ( i // 8 ) * 4 - 3)+"-"+str(j+1 + ( i // 8 ) * 4)+"反面合并完成")
    i += 8

#print(im_list[0].filename)


#1 10 11 11back 
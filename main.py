#作者：袁丽欢
#Version 0.9  Beta
#CopyRight： V0.9 版本基于MIT协议开源

#coding=utf-8
import time
import datetime
import tkinter
import PIL
import os
from tkinter import * 
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from PIL import Image
from os import listdir

#选择读取图片的地址
def select_in_Path():
    path_in = askdirectory()
    in_path.set(path_in)

#选择输出图片的地址
def select_out_Path():
    path_out = askdirectory()
    out_path.set(path_out)
    
#图片拼接功能实现
def function():
    ui.withdraw()
    cut_pictures = in_path.get()
    result_path_target =  out_path.get()
    date_time = datetime.datetime.now()
    filename = datetime.datetime.strftime(date_time,'%H%M%S')

    ims = [Image.open(cut_pictures+'/'+fn)for fn in listdir(cut_pictures)  if fn.endswith(".png") or fn.endswith(".jpg") or fn.endswith(".jpeg")]    
    width,height = ims[0].size 
    print(ims)
    result = Image.new(ims[0].mode,(width,height*len(ims)))
    for j , im in enumerate(ims):
        result.paste(im,box=(0,j*height))
        k=j+1
        print("第%2d 张图片已经处理"%k)
        time.sleep(2)
    result.save(result_path_target+'/'+'%s.png'%filename)
    messagebox.showinfo(title='提示！', message='请打开 %s 目录查看拼接好的图片' %result_path_target)
    ui.deiconify()
    

#界面初始化
ui = Tk()
in_path = StringVar()
out_path = StringVar()
ui.title("选择读取/存放图片的位置")
Label(ui,text = "选定读取路径:").grid(row = 0, column = 0)
Entry(ui, textvariable = in_path).grid(row = 0, column = 1)
Button(ui, text = "选择文件夹", command = select_in_Path).grid(row = 0, column = 2)
Label(ui,text = "选定存放路径:").grid(row = 0, column = 4)
Entry(ui, textvariable = out_path).grid(row = 0, column = 5)
Button(ui, text = "选择文件夹", command = select_out_Path).grid(row = 0, column = 6)
Button(ui, text = "开始拼图", command = function).grid(row = 1, column = 3)
Label(ui,text = "版权所有：雨悦灵动（成都）运营中心  V 0.9版本基于MIT协议开源").grid(row = 3, column = 3)
messagebox.showwarning(title='用户须知!', message='为保证拼图质量，请确保用于拼接的图片，扩展名都是“ PNG、JPG、JPEG ”！')
ui.mainloop()

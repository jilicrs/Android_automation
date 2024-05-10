#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/2/28 9:34
# @Author    :risheng.chen@lango-tech.com
# @File      :pagesize.py
__version__ = '1.0.0'

# from PIL import Image
# import os
#
# file_path = r"C:\Users\lg\Desktop\11111\touxiang1.jpg"    # 原始图像路径
#
# raw_files = os.walk(file_path)  # 遍历所有图像
#
# width, height = 390, 567                    # 修改后的图像尺寸大小
#
# save_path = r"C:\Users\lg\Desktop\11111\xiugai"  # 修改后图像存储的路径
# if not os.path.exists(save_path):           # 如果没有这个文件夹，就新建
#     os.makedirs(save_path)
#
# for root, dirs, files in raw_files:
#     for file in files:                      # 展现各文件
#         picture_path = os.path.join(root, file)    # 得到图像的绝对路径
#         pic_org = Image.open(picture_path)               # 打开图像
#
#         pic_new = pic_org.resize((width, height), Image.ANTIALIAS)   # 图像尺寸修改
#         _, sub_folder = os.path.split(root)              # 得到子文件夹名字
#         pic_new_path = os.path.join(save_path, sub_folder)
#         if not os.path.exists(pic_new_path):
#             os.makedirs(pic_new_path)                    # 建立子文件夹
#         pic_new_path = os.path.join(pic_new_path, file)  # 新图像存储绝对路径
#         pic_new.save(pic_new_path)					     # 存储文件
#         print("%s have been resized!" % pic_new_path)


# import Cv2_Video
# # 原始图像读取
# image = Cv2_Video.imread("C:\\Users\\lg\\Desktop\\11111\\touxiang2.jpg")
# # 获取原始图像宽高
# height, width = image.shape[0], image.shape[1]
# print(width, height)
# # 输入你想要resize的图像高
# sizi1 = 390
# size = 567
# # 等比例缩放尺度
# # scale = height/size
# # print("等比例缩放的尺度：",scale)
# # # 获得相应等比例的图像宽度
# # width_size = int(width/scale)
# # print("等比例缩放后的宽：",width_size)
# image_resize = Cv2_Video.resize(image, (sizi1, size))
# # 这里image_resize用来盛放修改后的结果，
#
# # 将image_resize写入jpg格式的文件
# import os
# Cv2_Video.imwrite('C:\\Users\\lg\\Desktop\\11111\\xiugai\\xiugai1.jpg', image_resize)


# import os
# from PIL import Image
# from PIL import ImageFile
#
# ImageFile.LOAD_TRUNCATED_IMAGES = True
#
# # 文件夹路径
# path = r'C:\Users\lg\Desktop\11111'
#
#
# def pilConvertJPG(path):
#     for a, _, c in os.walk(path):
#         for n in c:
#             if '.jpg' in n or '.png' in n or '.jpeg' in n:
#                 img = Image.open(os.path.join(a, n))
#                 rgb_im = img.convert('RGB')
#                 error_img_path = os.path.join(a, n)
#                 os.remove(error_img_path)
#                 n = ''.join(filter(lambda n: ord(n) < 256, n))
#                 jpg_img_path = os.path.splitext(os.path.join(a, n).replace('\\', '/'))[0]
#                 jpg_img_path += '.jpg'
#                 print(jpg_img_path)
#                 rgb_im.save(jpg_img_path)
#
#
# pilConvertJPG(path)


import Cv2_Video
import matplotlib.pyplot as plt
import os
import re
import sys
from PIL import Image
import string
import numpy as np

PATH = r'C:\Users\lg\Desktop\11111'


def resizeImage(file, NoResize):
    image = Cv2_Video.imread(file, Cv2_Video.IMREAD_COLOR)
    # print(type(image))

    # 如果type(image) == 'NoneType',会报错,导致程序中断,所以这里先跳过这些图片,
    # 并记录下来,结束程序后手动修改(删除)

    if image is None:
        NoResize += [str(file)]
    else:
        resizeImg = Cv2_Video.resize(image, (512, 384))
        Cv2_Video.imwrite(file, resizeImg)
        Cv2_Video.waitKey(100)


def resizeAll(root):
    # 待修改文件夹
    fileList = os.listdir(root)
    # 输出文件夹中包含的文件
    # print("修改前："+str(fileList))
    # 得到进程当前工作目录
    currentpath = os.getcwd()
    # 将当前工作目录修改为待修改文件夹的位置
    os.chdir(root)

    NoResize = []  # 记录没被修改的图片

    for file in fileList:  # 遍历文件夹中所有文件
        file = str(file)
        resizeImage(file, NoResize)

    print("---------------------------------------------------")

    os.chdir(currentpath)  # 改回程序运行前的工作目录

    sys.stdin.flush()  # 刷新

    if len(NoResize) != 0:
        print('没被修改的图片: ', root, '\t', NoResize)


def convertToJPG(dirName, childPATH):
    li = os.listdir(dirName)
    for filename in li:
        newname = filename
        newname = newname.split(".")
        if newname[-1] == "jpeg":
            newname[-1] = "jpg"
            newname = str.join(".", newname)
            filename = dirName + filename
            newname = dirName + newname
            os.rename(filename, newname)
        elif newname[-1] == 'png':
            newname[-1] = "jpg"
            newname = str.join(".", newname)
            filename = dirName + filename
            newname = dirName + newname
            os.rename(filename, newname)
        savePATH = childPATH + '/' + filename
        print(savePATH)
        # img = Image.open(savePATH).convert('RGB')
        # img.save(savePATH)

    print('convert To JPG is over!')
    print('Now resize images')


def renameall(root, NewFileName):
    # 待修改文件夹
    fileList = os.listdir(root)
    # 输出文件夹中包含的文件
    print("修改前：" + str(fileList))
    # 得到进程当前工作目录
    currentpath = os.getcwd()
    # 将当前工作目录修改为待修改文件夹的位置
    os.chdir(root)
    num = 1  # 名称变量

    for fileName in fileList:  # 遍历文件夹中所有文件

        preName, _ = fileName.split('_', 1)

        if preName != NewFileName:
            pat = ".+\.(jpg|png|pgm|jpeg|JPG)"  # 匹配文件名正则表达式
            pattern = re.findall(pat, fileName)  # 进行匹配
            os.rename(fileName, (str(NewFileName) + '_' + str(num) + '.' + pattern[0]))  # 文件重新命名
            num = num + 1  # 改变编号，继续下一项
    print("---------------------------------------------------")
    os.chdir(currentpath)  # 改回程序运行前的工作目录
    sys.stdin.flush()  # 刷新
    # print("修改后："+str(os.listdir(root)))       #输出修改后文件夹中包含的文件


# 两层文件夹
if __name__ == "__main__":
    # 含图片的文件夹叫做fileName,dir1的上层文件夹的路径为PATH
    for fileName in os.listdir(PATH):
        # 子文件夹路径
        dirName = PATH + '/' + fileName + '//'
        childPATH = PATH + '/' + fileName
        print(childPATH)
        renameall(childPATH, fileName)
        print(childPATH, 'rename is over')
        convertToJPG(dirName, fileName)
        print(childPATH, 'convertToJPG is over')
        resizeAll(childPATH)
        print(childPATH, 'resizeAll is over')

# 一层文件夹
# if __name__=="__main__":

#     #含图片的文件夹叫做fileName,dir1的上层文件夹的路径为PATH
#     dirName =  PATH +  '//' +fileName
#     childPATH = PATH + '/'+ fileName
#     print(childPATH)
#     renameall(childPATH,fileName)
#     print(childPATH,'rename is over')
#     convertToJPG(dirName,fileName)
#     print(childPATH,'convertToJPG is over')
#     resizeAll(childPATH)
#     print(childPATH,'resizeAll is over')



































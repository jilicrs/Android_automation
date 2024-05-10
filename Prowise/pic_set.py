"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2023/12/2 16:59
@Author    :risheng.chen@lango-tech.cn
@File      :pic_set.py
__version__ = '1.0.0'
"""

from PIL import Image

# 'D:\\Img\\ball.png'

im = Image.open("D:\\Img\\ball.png")
try:
    #放大图片
    image=im.resize((50, 50))
    #将新图像保存至桌面
    image.save("D:\\Img\\123.png")
    print("查看新图像的尺寸",image.size)
except IOError:
    print("缩小图像失败")















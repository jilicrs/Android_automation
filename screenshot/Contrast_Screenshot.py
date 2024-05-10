#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/11/14 9:50
# @Author    :risheng.chen@lango-tech.com
# @File      :Contrast_Screenshot.py
__version__ = '1.0.0'

from functools import reduce
import math
import operator
from PIL import Image
import imagehash

def compare(pic1, pic2):
    """
    :param pic1: 图片1路径
    :param pic2: 图片2路径
    :return: 返回对比结果
    """
    image1 = Image.open(pic1)
    image2 = Image.open(pic2)

    histogram1 = image1.histogram()
    histogram2 = image2.histogram()

    # histogram得到一个列表结果
    # histogram1[i] - histogram2[i] 相减的结果平⽅的新的列表
    differ = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a-b)**2, histogram1, histogram2)))/len(histogram1))

    if differ > 5000:
        print('比较值:{},图片对比结果不一致'.format(differ))
        return False
    else:
        print('比较值:{},图片对比结果一致'.format(differ))
        return True
    #  differ越接近0，图片越相似
    # return differ



def HashContrast(path1=input('图片1路径：'), path2=input('图片2路径：')):
    """
    HashContrast:感知哈希对比
    :param path1:
    :param path2:
    :return:True or False
    """
    image1 = Image.open(path1)
    image2 = Image.open(path2)

    # 转换为灰度图
    gray_image1 = image1.convert("L")
    gray_image2 = image2.convert("L")

    # 感知哈希对比
    hash1 = imagehash.phash(gray_image1)
    hash2 = imagehash.phash(gray_image2)

    hash_diff = hash1 - hash2
    if hash_diff == 0:
        print(f'图片对比结果一致,hash值差异{hash_diff}')
        return True
    else:
        print(f"图片对比结果不一致，hash值差异{hash_diff}")
        return False

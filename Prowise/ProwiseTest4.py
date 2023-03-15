#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/11/19 10:56
# @Author    :risheng.chen@lango-tech.com
# @File      :ProwiseTest4.py
__version__ = '1.0.0'
import time
from functools import reduce
from PIL import Image
import math
import operator


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

    if differ > 500:
        print('比较值:{},图片对比结果不一致'.format(differ))
        return False
    else:
        print('比较值:{},图片对比结果一致'.format(differ))
        return True
    #  differ越接近0，图片越相似
    # return differ


if __name__ == '__main__':
    test1 = input("输入图片需要对比图片路径：").replace('\\', '/', 100)
    # D:\screenshots\screen.png
    test2 = input("输入对比图片的路径：").replace('\\', '/', 100)
    # D:\screen.png
    print(compare(test1, test2))
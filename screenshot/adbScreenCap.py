#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/8/4 11:06
# @Author    :risheng.chen@lango-tech.com
# @File      :adbScreenCap.py
__version__ = '2.0.0'

import os
import time
import cv2
import datetime


def get_screen_shout():
    # adb截图
    get_png = 'adb shell system/bin/screencap -p /sdcard/screen.png'

    # 将截图上传到指定目录
    put_png = 'adb pull /sdcard/screen.png D:/screenshots/'

    # 获取当前时间
    now_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

    os.system(get_png)
    time.sleep(1)
    os.system(put_png)
    # 重命名文件名并添加上时间戳
    os.renames("D:\\screenshots\\screen.png", "D:\\screenshots\\%s.png" % str(now_time))

    # 文件夹路径
    file_path = 'D:\\screenshots\\'
    # 以列表的形式列出文件夹内所有文件
    lists = os.listdir(path=file_path)
    # 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
    file_new = os.path.join(file_path, lists[-1])
    print(file_new)

    # 选择图片
    img = cv2.imread('%s' % file_new)

    if img is None:
        print('图片打开失败')
        exit()
    else:
        # 创建窗口
        cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('screen', 700, 400)
        # 显示图片
        cv2.imshow('screen', img)
        # 暂停运行，防止图片一闪而过
        cv2.waitKey(0)
    return img


def test():
    os.system('adb shell screencap -p sdcard/1.png')
    time.sleep(1)
    os.system('adb pull sdcard/1.png D:\\logs\\{}1.png'.format(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_')))

def Filter_the_latest_documents():
    """
    Filter_the_latest_documents:排列指定文件夹目录下的文件，并筛选出最新的文件
    :return: file_new
    """
    file_path = 'D:\\logs\\'
    lists = os.listdir(path=file_path)
    print("未经处理的文件夹列表：\n %s \n" % lists)

    # 按照key的关键字进行生序排列，lambda入参x作为lists列表的元素，获取文件最后的修改日期，
    # 最后对lists以文件时间从小到大排序
    lists.sort(key=lambda x: os.path.getmtime((file_path + "\\" + x)))

    # 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
    file_new = os.path.join(file_path, lists[-1])
    print("时间排序后的的文件夹列表：\n %s \n" % lists)

    print("最新文件路径:\n%s" % file_new)

if __name__ == '__main__':
    Filter_the_latest_documents()

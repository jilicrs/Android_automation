#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/8/4 11:06
# @Author    :risheng.chen@lango-tech.com
# @File      :adbScreenCap.py
__version__ = '1.0.0'

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
    os.renames("D:\\screenshots\\screen.png", "D:\\screenshots\\screenshots %s.png" % str(now_time))

    img = cv2.imread('D:\\screenshots\\logo.png', 0)

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


if __name__ == '__main__':
    get_screen_shout()

"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2023/10/13 14:20
@Author    :risheng.chen@lango-tech.cn
@File      :guitest_functional_interface.py
__version__ = '1.0.0'
"""

import os
import time
import datetime


def guitest_adb_screen_cap(value1, value2):
    """
    guitest_adb_screen_cap: adb截图功能接口
    :param value1: 保存图片文件夹路径
    :param value2: 时间戳
    :return: 在目标路径以时间戳命名的截图文件
    """
    os.system('adb -s {} shell screencap -p /sdcard/1.png'.format(value1))
    time.sleep(1)
    now_time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_')
    os.system('adb -s {} pull /sdcard/1.png {}\\{}.png'.format(value1, value2, now_time))

















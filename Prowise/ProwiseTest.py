#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/8/29 19:40
# @Author    :risheng.chen@lango-tech.com
# @File      :ProwiseTest.py
__version__ = '1.0.0'

import os
import datetime
import uiautomator2 as u2

d = u2.connect_adb_wifi('192.168.5.197')
StartTest = int(input("输入开始测试次数:"))

while True:
    os.system('adb connect 192.168.5.197')
    NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    os.system('adb -s 192.168.5.197 shell input tap 132 636')
    print('%s:第{}次点击'.format(StartTest) % NowTime)
    StartTest += 1



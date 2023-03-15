#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/11/9 11:03
# @Author    :risheng.chen@lango-tech.com
# @File      :ProwiseTest2.py
__version__ = '1.0.0'

import os
import time
import datetime


StartTest = int(input("输入开始测试次数:"))
MaxTest = int(input("请输入最大测试次数："))

while True:
    if StartTest < MaxTest:
        ThisTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        print('第{}次测试'.format(StartTest))
        os.system('adb connect 192.168.5.197')

        
        # print('1.%s:打开信号源列表' % ThisTime)
        # os.system('adb shell input tap 3723 977')
        # time.sleep(1)
        # ThisTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        # print('2.%s:切换PC通道' % ThisTime)
        # os.system('adb shell input tap 3575 971')
        # time.sleep(20)
        # ThisTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        # print('3.%s:点击home键返回Android' % ThisTime)
        # os.system('adb shell input tap 3816 1078')
        # time.sleep(3)
        StartTest = StartTest + 1
    elif StartTest > MaxTest:
        ThisTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        print('%s:测试完成，退出程序' % ThisTime)
        break

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/8/29 19:40
# @Author    :risheng.chen@lango-tech.com
# @File      :ProwiseTest.py
__version__ = '1.0.0'

import subprocess
import time


log = 'D:\\logs\\test.log'

connect = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE,
                           universal_newlines=True, encoding='utf-8')
d = connect.stdout.read()

if '192.168.123.155' in d:
    print(d)
else:
    print('连接失败')






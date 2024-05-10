#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/5/25 14:22
# @Author    :risheng.chen@lango-tech.com
# @File      :reboottest.py
__version__ = '1.0.0'


import subprocess
import time


def monkey_test(start=True, ip=input('设备IP：')):
    while start:
        run = subprocess.Popen(f'adb -s {ip} shell monkey 5000', shell=True,
                         stdout=subprocess.PIPE)
        result = run.stdout.read()
        print(result)
        time.sleep(1)
        continue


if __name__ == '__main__':
    monkey_test()
    input('=============回车退出================')
"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/2/22 19:52
@Author    :risheng.chen@lango-tech.cn
@File      :AiDemo.py
__version__ = '1.0.0'
"""

import datetime
import time
import multiprocessing

def test1():
    for i in range(10):
        Now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        print(f'线程1执行:{Now}\n')
        time.sleep(1)

def test2():
    for i in range(10):
        Now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        print(f'线程2执行:{Now}\n')
        time.sleep(1)


def test3():
    for i in range(10):
        Now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        print(f'线程3执行:{Now}\n')
        time.sleep(1)



if __name__ == '__main__':
    t1 = multiprocessing.Process(target=test1)
    t2 = multiprocessing.Process(target=test2)
    t3 = multiprocessing.Process(target=test3)

    t1.start()
    t2.start()
    t3.start()









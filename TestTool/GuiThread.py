#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/4/6 15:14
# @Author    :risheng.chen@lango-tech.com
# @File      :GuiThread.py
__version__ = '1.0.0'

import threading
import time

from TestTool.guitestpage import check_adb_status


class MyThread(threading.Thread):
    def __init__(self, target=None, arges=()):
        super(MyThread, self).__init__()
        self.result = None
        self.func = target
        self.arges = arges

    def run(self):
        self.result = self.func(*self.arges)

    def get_result(self):
        try:
            return self.result
        except Exception as e:
            print(e)
            return None


if __name__ == '__main__':
    while True:
        t1 = MyThread(target=check_adb_status)
        t1.start()
        t1.join()
        s = t1.get_result()
        print(s)
        time.sleep(0.5)

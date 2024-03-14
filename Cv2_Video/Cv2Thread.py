"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/3/14 16:00
@Author    :risheng.chen@lango-tech.cn
@File      :Cv2Thread.py
__version__ = '1.0.0'
"""


import threading


class MyThread(threading.Thread):
    def __init__(self, target=None, arges=(), name=None, kwargs=None):
        super(MyThread, self).__init__()
        self.result = None
        self.func = target
        self.arges = arges
        self.name = str(name)
        self.kwargs = kwargs

    def run(self):
        self.result = self.func(*self.arges)

    def get_result(self):
        try:
            return self.result
        except Exception as e:
            print(e)
            return None























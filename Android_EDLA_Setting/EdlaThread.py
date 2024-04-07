"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/2/24 10:42
@Author    :risheng.chen@lango-tech.cn
@File      :EdlaThread.py
__version__ = '1.0.0'
"""
import threading


class TestThread(threading.Thread):
    def __init__(self, target=None, arges=()):
        super(TestThread, self).__init__()
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
















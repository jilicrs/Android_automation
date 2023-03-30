#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/3/18 10:24
# @Author    :risheng.chen@lango-tech.com
# @File      :Thread.py
__version__ = '1.0.0'

import threading
from ProwiseSourceTouch.MonitorMouse import listen_mouse_click
from ProwiseSourceTouch.MonitorUSB import monitor_disk


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
    t1 = MyThread(target=listen_mouse_click)
    t2 = MyThread(target=monitor_disk)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    result = t1.get_result()
    res2 = t2.get_result()
    print("mouse click", result)
    print("u disk", res2)

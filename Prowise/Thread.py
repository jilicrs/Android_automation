#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/10/14 11:29
# @Author    :risheng.chen@lango-tech.com
# @File      :Thread.py
__version__ = '1.0.0'

import threading
import time
condtion = threading.Condition()
sheep = ['1件产品', '1件产品', '1件产品', '1件产品', '1件产品']


class Producer(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
        pass

    def run(self):
        global condtion, sheep
        while True:
            time.sleep(0.1)
            condtion.acquire()
            if len(sheep) < 10:
                print(self.name + "生产了1件产品")
                sheep.append('1件产品')
                condtion.notifyAll()
                pass
            else:
                print("仓库满了，停止生产!")
                condtion.wait()
                pass
            condtion.release()
        pass
    pass


class Customer(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
        pass

    def run(self):
        global condtion, sheep
        while True:
            time.sleep(0.1)
            condtion.acquire()
            if len(sheep) > 0:
                meat = sheep.pop()
                print(self.name + "购买了" + meat + "还剩多少" + str(len(sheep)) + "件")
                condtion.notifyAll()
                pass
            else:
                print("买光了，等待")
                condtion.wait()
                pass
            condtion.release()
        pass
    pass


if __name__ == "__main__":
    p1 = Producer("1号生产车间")
    p2 = Producer("2号生产车间")
    p3 = Producer("3号生产车间")
    p4 = Producer("4号生产车间")
    p5 = Producer("5号生产车间")
    p6 = Producer("6号生产车间")
    p1.start()
    p2.start()
    p4.start()
    p5.start()
    p6.start()
    c1 = Customer('小王')
    c2 = Customer('小李')
    c3 = Customer('小贾')
    c4 = Customer('小沈')
    c5 = Customer('小刘')
    c1.start()
    c2.start()
    c3.start()
    c4.start()
    c5.start()





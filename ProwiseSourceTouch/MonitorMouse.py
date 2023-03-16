#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/3/16 10:16
# @Author    :risheng.chen@lango-tech.com
# @File      :MonitorMouse.py
__version__ = '1.0.0'

import pynput
import pynput.mouse
import threading
import time


def waite():
    msg = '等待事件：'
    for times in range(20, -1, -1):
        print("\r{} {}seconds ".format(msg, times), end='')
        time.sleep(1)


def listen_mouse_click():
    """
    listen_mouse_click: 检测Windows是否识别到触摸
    :return: True or False
    events.get(20):鼠标事件检测超时时间
    """
    while 1:
        with pynput.mouse.Events() as events:
            event = events.get(20)
            if event is None:
                print('False')
                return False
            if event:
                if isinstance(event, pynput.mouse.Events.Move):
                    print("Move({} at {})".format(event.x, event.y))
                elif isinstance(event, pynput.mouse.Events.Click):
                    print("Click({} at {})".format(event.x, event.y), event.button, event.pressed)
                    if event.button:
                        print('PASS')
                        return True
                elif isinstance(event, pynput.mouse.Events.Scroll):
                    print('Scrolled {0} at {1}'.format(
                        'down' if event.dy < 0 else 'up',
                        (event.x, event.y)))
                    print(str(event.dy) + '   ' + str(event.dx))


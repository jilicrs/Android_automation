#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/3/7 14:56
# @Author    :risheng.chen@lango-tech.com
# @File      :ProwiseSourceTouchTest.py
__version__ = '1.0.0'

import os
import sys
import datetime
import time
import pynput
import pynput.mouse
from BasePage.Rs232_Connect import serial_sent_hex
from ProwiseSourceTouch.MonitorUSB import monitor_disk


def waite():
    msg = 'Simulated click detection in progress：'
    for times in range(11, -1, -1):
        Test = sys.stdout.write("\r{} {}seconds ".format(msg, times))
        time.sleep(1)
        sys.stdout.flush()
        return Test


def listen_mouse_click():
    """
    listen_mouse_click: 检测Windows是否识别到触摸，10S内未检测到返回False，反之True
    :return:
    """
    while 1:
        with pynput.mouse.Events() as events:
            event = events.get(10)
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


if __name__ == '__main__':
    # 测试设备ip：
    adb_connect = input('①Input device adb ip to open Autoclick property:')
    os.system('adb connect {}'.format(adb_connect))

    # 初始测试次数：
    start_test = int(1)
    # 最大测试次数：
    end_test = int(input('②Number of test end:'))

    print('输入测试外部通道，大写：')  # 输入测试外部通道，大写：列如：USB_C
    Source = input('③Test change source:')

    time.sleep(1)
    os.system('adb -s {} shell setprop sys.xbh.sourcetouchautosend.start true'.format(adb_connect))

    while start_test < end_test:
        print('{}:start {} test'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), start_test))
        time.sleep(2)
        print('************1.{}:change {} source************'.format(datetime.datetime.now().
                                                                     strftime('%Y-%m-%d %H:%M:%S'),
                                                                     Source))
        # USB_C
        command_hex1 = serial_sent_hex(Source)
        time.sleep(2)
        print('************2.{}:Click test************'.format(datetime.datetime.now().strftime
                                                               ('%Y-%m-%d %H:%M:%S')))
        time.sleep(1)
        # mouse.position(400, 300)
        test = listen_mouse_click()
        if test:
            time.sleep(2)
            # 检测U盘是否满足4个
            # if monitor_disk(USB_Disk=4):
            print('==============================================================================================')
            print('Test Result：{}:The {} test pass'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                           start_test), test)
            print('==============================================================================================')
            start_test = start_test + 1
            time.sleep(2)
            print('3.{}:change android'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            command_hex2 = serial_sent_hex(command='ANDROID')
            time.sleep(3)
            continue
            # else:
            #     print('{}: The {} test times Error:USB device identification error!!!'.format
            #           (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), start_test))
            #     input('============Press Enter to Exit============')
            #     break
        elif start_test > end_test:
            print('{}:Test PASS, test {} times'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                       end_test))
            input('============Press Enter to Exit============')
            break
        else:
            print('{}: The {} test times Error:Coordinates not clicked!!!'.format(datetime.datetime.now().strftime
                                                               ('%Y-%m-%d %H:%M:%S'), start_test))
            input('============Press Enter to Exit============')
            break

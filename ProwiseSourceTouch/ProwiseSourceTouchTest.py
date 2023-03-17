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
import threading
from BasePage.Rs232_Connect import serial_sent_hex
from ProwiseSourceTouch.MonitorUSB import monitor_disk
from ProwiseSourceTouch.MonitorMouse import listen_mouse_click


def waite():
    msg = 'Simulated click detection in progress：'
    for times in range(21, -1, -1):
        Test = sys.stdout.write("\r{} {}seconds ".format(msg, times))
        time.sleep(1)
        sys.stdout.flush()
        return Test


if __name__ == '__main__':
    # 测试设备ip：
    adb_connect = input('①Input device adb ip to open Autoclick property:')
    os.system('adb connect {}'.format(adb_connect))

    # 初始测试次数：
    start_test = int(1)
    # 最大测试次数：
    end_test = int(input('②Number of test end:'))

    pass_test = 0
    false_test = 0

    print('输入测试外部通道，大写：')  # 输入测试外部通道，大写：列如：USB_C
    Source = input('③Test change source:')

    time.sleep(1)
    os.system('adb -s {} shell setprop sys.xbh.sourcetouchautosend.start true'.format(adb_connect))

    while start_test < end_test:
        print('{}:start {} test'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), start_test))
        print('Total test：{}，PASS:{},False:{}'.format(start_test, pass_test, false_test))
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
        mouse_click_thread = threading.Thread(target=listen_mouse_click)
        usb_device_thread = threading.Thread(target=monitor_disk)
        mouse_click_thread.start()
        usb_device_thread.start()
        if mouse_click_thread and usb_device_thread:
            time.sleep(2)
            print('==============================================================================================')
            print('Test Result：{}:The {} test pass'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                           start_test), mouse_click_thread, usb_device_thread)
            print('==============================================================================================')
            pass_test += 1
            start_test = start_test + 1
            time.sleep(2)
            print('3.{}:change android'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            command_hex2 = serial_sent_hex(command='ANDROID')
            time.sleep(3)
            continue
        elif not mouse_click_thread:
            time.sleep(2)
            print('{}: The {} test times Error:Coordinates not clicked!!!'.format(datetime.datetime.now().strftime
                                                                                  ('%Y-%m-%d %H:%M:%S'), start_test))
            false_test += 1
            continue
        elif not usb_device_thread:
            print('{}: The {} test times Error:USB device identification error!!!'.format
                  (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), start_test))
            false_test += 1
            continue
        elif start_test > end_test:
            print('{}:Test PASS, test {} times'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                       end_test))
            input('============Press Enter to Exit============')
            break

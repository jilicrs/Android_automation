#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/3/13 16:05
# @Author    :risheng.chen@lango-tech.com
# @File      :MonitorUSB.py
__version__ = '1.0.0'

import threading
import time
import psutil
import datetime
import ctypes
import inspect

# 获得cpu的个数
cpu = psutil.cpu_count()

# cpu的总体使用情况。要是看每个cpu的情况加上参数percpu=True即可
cpu1 = psutil.cpu_times_percent()


# usb = psutil.disk_partitions()
def monitor_disk(USB_Disk=4):
    """
    monitor_disk: 检测Windows系统识别到的可移动U盘方法
    :param USB_Disk: 预期找到U盘数量
    :return:
    """
    driver = []
    flag = 21
    disk = 0
    while True:
        if flag > disk:
            time.sleep(1)
            flag -= 1
            for usb in psutil.disk_partitions():
                print('\r正在检测USB设备:{}S'.format(flag), end='')
                if 'removable' in usb.opts:
                    driver.append(usb.device)
                    continue
                else:
                    continue
        elif flag == disk:
            break

    count = len(driver)
    new_list = []
    if count == 0:
        print('{}:Not find USB device'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        return False
    elif flag == disk:
        for i in driver:
            if i not in new_list:
                new_list.append(i)
        print(new_list)
        count_new = len(new_list)
        if count_new == USB_Disk:
            print('{}:Succeed to find {} USB device:'.format(
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), count_new), new_list)
            return True
        elif count_new < USB_Disk:
            print('{}:The expected USB devices are lost, {} USB total found!'.format(
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), count_new), new_list)
            return False
        elif count_new > USB_Disk:
            print('{}:The expected USB devices are excessive, {} USB total found!'.format(
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), count_new), new_list)
            return False











#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/3/25 9:44
# @Author    :risheng.chen@lango-tech.com
# @File      :MonitorMicarray.py
__version__ = '1.0.0'

import sounddevice
import datetime
import time


def monitor_micarray():
    """
    monitor_micarray: 检测Windows麦克风设备来判断整机切换外部通道时是否识别到预期设备
    sounddevice.query_devices(): 获取设备声音输入输出
    :return: True or False
    """
    flag = 21
    timeout = 0
    while True:
        if flag > timeout:
            time.sleep(1)
            flag -= 1
            mic = sounddevice.query_devices(1)
            print(mic)
            print('\r正在检测Mic设备:{}S'.format(flag), end='')
            # 判断是否存在预期的录音设备
            if '麦克风阵列' in mic['name']:
                print('\r{}:Mic device matching succeeded'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                      mic['name'])
                return True
            else:
                continue
        elif flag == timeout:
            mic = sounddevice.query_devices(1)
            print('\r{}:检测超时，Mic设备识别与预期不符:'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                  mic['name'])
            return False


if __name__ == '__main__':
    print(monitor_micarray())

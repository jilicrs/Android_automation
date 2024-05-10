"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2023/11/14 19:23
@Author    :risheng.chen@lango-tech.cn
@File      :AI_test.py
__version__ = '1.0.0'
"""


import serial.tools.list_ports


def get_serial_comport():
    ports_list = list(serial.tools.list_ports.comports())
    if len(ports_list) <= 0:
        return False
    else:
        for comport in ports_list:
            return list(comport)



if __name__ == '__main__':
    get_serial_comport()


































































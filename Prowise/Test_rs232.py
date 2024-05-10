#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/3/29 16:41
# @Author    :risheng.chen@lango-tech.com
# @File      :Test_rs232.py
__version__ = '1.0.0'

import time
import serial
import serial.tools.list_ports
from Prowise.KTC_232_Gather import RS232_Connect


def get_serial_comport():
    ports_list = list(serial.tools.list_ports.comports())
    if len(ports_list) <= 0:
        return False
    else:
        for comport in ports_list:
            return list(comport)[0]


ser = serial.Serial(port=get_serial_comport(), baudrate=9600, timeout=0.3)


def close_serial_comport():
    """
    close_serial_comport: 关闭串口函数
    :return: True or False
    """
    ser.close()
    if ser.isOpen():
        return False
    else:
        return True


def serial_sent_hex(command):
    var = bytes.fromhex(RS232_Connect['%s' % command])
    ser.write(var)
    time.sleep(0.3)
    data = ser.read_all()
    if data:
        rtc = data.decode('utf-8')
        return rtc
    else:
        return None


if __name__ == '__main__':
    flag = 50
    start = 1
    while True:
        if flag > start:
            print('开始{}'.format(start))
            serial_sent_hex('HDMI1')
            time.sleep(20)
            serial_sent_hex('USB_C_F')
            start += 1
            time.sleep(20)
            continue
        elif flag < start:
            print('结束')
            break




#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/3/27 19:22
# @Author    :risheng.chen@lango-tech.com
# @File      :test232.py
__version__ = '1.0.0'

import binascii
import time
import serial

br = serial.Serial.baudrate
print(br)
serial = serial.Serial('COM3', 9600)

print(serial)
print(serial.portstr)
print(serial.baudrate)

var = bytes.fromhex("F6 03 02 00 FB 6F")
serial.write(var)
time.sleep(0.3)
print('===')
data = serial.read_all()
rtc = data.decode('utf-8')

n = serial.inWaiting()
if n:
    abc = str(binascii.b2a_hex(serial.read(n)))[2:-1]
    print(abc)

print(rtc)
serial.close()
print("==")


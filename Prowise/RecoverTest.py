#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/11/16 21:48
# @Author    :risheng.chen@lango-tech.com
# @File      :RecoverTest.py
__version__ = '1.0.0'

import os
import time
import serial
import datetime
import serial.tools.list_ports


RS232_Connect = {
    'Recover': 'F6 03 06 00 FF 6F',
    'HDMI3': 'F6 30 01 13 3A 6F',
    'HDMI1': 'AA BB CC 02 06 00 08 DD EE FF',
}


def get_serial_comport():
    ports_list = list(serial.tools.list_ports.comports())
    if len(ports_list) <= 0:
        print('No available serial port found')
    else:
        print('Find the following available serial port devices:')
    for comport in ports_list:
        print(list(comport)[0], list(comport)[1])
        return list(comport)[0]


def serial_sent_hex(command):
    ser = serial.Serial(get_serial_comport(), 9600, timeout=3)
    var = bytes.fromhex(RS232_Connect["%s" % command])
    ser.write(var)
    data = ser.read(10)
    data = str(data, encoding="utf-8")
    return data


if __name__ == '__main__':
    StartTest = int(input("start:"))
    MaxTest = int(input("max:"))

    while True:
        if StartTest <= MaxTest:
            print('Start control {} Level Test'.format(StartTest))
            os.system('adb connect 192.168.5.133')
            NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            command_hex2 = serial_sent_hex('HDMI3')
            print('%s:Instruction completion' % NowTime, command_hex2)
            time.sleep(5)
            if command_hex2 == 'S':
                StartTest = StartTest + 1
                time.sleep(1)
                print("normal")
                os.system('adb -s 192.168.5.133 reboot')
                time.sleep(60)
                continue
            else:
                print('abnormal!!!!!!! Fetching log..........')
                os.system('adb shell logcat -v time > D:\\SidebarError.log')
        elif StartTest > MaxTest:
            ThisTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            print('%s:The test is complete, exit the program' % ThisTime)
            input('================================Press enter to Exit================================')
            break

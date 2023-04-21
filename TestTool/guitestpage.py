#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/2/3 13:32
# @Author    :risheng.chen@lango-tech.com
# @File      :guitestpage.py
__version__ = '1.0.0'

import os
import serial
import serial.tools.list_ports
import subprocess

RS232_Connect = {
    'Power_Off': 'AA BB CC 01 01 00 02 DD EE FF',  # 关机
    'Power_On': 'AA BB CC 01 00 00 01 DD EE FF',  # 开机
    'Source': 'F6 4D 01 00 44 6F',  # 获取当前通道信号状态，01表示有信号，00无信号
}

TestManageSystem = '测试管理系统'
User = '用户名'
PassWord = '密码'
Login = '登录'
Send = '发送'
ExitSystem = '退出'
Cancel = '取消'
Getport = '端口号:'
open_comport = '打开串口'
open_down = '关闭串口'
adb_connect = '连接ADB'
choose_instruct = '选择发送指令：'


def adb_connect_ip(adb_ip):
    adb = os.system('adb connect {}'.format(adb_ip))
    return adb


def check_adb_status(device_id):
    out, info = subprocess.getstatusoutput("adb -s "+device_id+" get-state")
    print(out, info)
    if out == 0:
        if 'device' in info:
            print('[info] ADB device {} is online'.format(device_id))
            return True
        elif 'offline' in info:
            print('[WARNING] ADB device {} is offline'.format(device_id))
            return False
        else:
            print('[WARNING] ADB is abnormal' + info)
    elif out == 1:
        print('[WARNING]' + info)
        return False


class ComPort(object):
    def __init__(self):
        self.ports_list = None

    def get_serial_comport(self):
        self.ports_list = list(serial.tools.list_ports.comports())
        if len(self.ports_list) <= 0:
            print('No available serial port found')
        else:
            print('Find the following available serial port devices:', self.ports_list)
            for comport in self.ports_list:
                print(list(comport)[0], list(comport)[1])
                return list(comport)[0]

    def open_serial_comport(self):
        # 默认波特率9600
        ser = serial.Serial(port=self.get_serial_comport(), baudrate=9600, timeout=3)
        return ser

    def close_serial_comport(self):
        return self.open_serial_comport().close()

    def serial_sent_hex(self, command):
        var = bytes.fromhex(RS232_Connect["%s" % command])
        self.open_serial_comport().write(var)
        data = self.open_serial_comport().read(10)
        data = str(data, encoding="utf-16")
        return data


"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/3/29 11:26
@Author    :risheng.chen@lango-tech.cn
@File      :UsbSwitch.py
__version__ = '1.0.0'
"""
import time

import serial
import serial.tools.list_ports


RS232_List = {
    'HDMI1' : 'F6 30 01 09 30 6F',
    'HDMI2' : 'F6 30 01 0A 31 6F',
    'DP' : 'F6 30 01 14 3B 6F',
    'get_source' : 'F6 30 02 00 28 6F',
}


def GetComport():
    """
    get_serial_comport: 获取设备管理器COM口
    :return: list(comport)[0]
    """
    ports_list = list(serial.tools.list_ports.comports())
    if len(ports_list) <= 0:
        return False
    else:
        for comport in ports_list:
            return list(comport)[0]


ser = serial.Serial(port=GetComport(), baudrate=115200, timeout=3)




def CloseComport():
    """
    close_serial_comport: 关闭串口函数
    :return: True or False
    """
    ser.close()
    if ser.is_open:
        return False
    else:
        return True



def SentHex(command):
    """
    serial_sent_hex:
    bytes.fromhex()使用这个函数进行数据转换，可以把16进制的数值转换字节数据
    (即比特流，字符串与比特流间还可以用encode（）和decode（）进行编解码)字符串与比特流间还可以用encode
    :param command: RS232
    :return: data: 获取指令的返回值，并且进行类型转换，转换为字符串后便可以进行字符串对比，因而便可以根据返回值进行判断是否执行特定功能
    """
    var = bytes.fromhex(RS232_List["%s" % command])
    ser.write(var)
    data = ser.read(10).hex()
    data = str(data)
    result = data.upper()
    CloseComport()
    return result


def SwitchDP():
    print('切换DP')
    return SentHex('DP')


def SwitchHDMI2():
    print('切换HDMI2')
    return SentHex('HDMI2')



def GetSource():
    print('获取信号源通道')
    return SentHex('get_source')














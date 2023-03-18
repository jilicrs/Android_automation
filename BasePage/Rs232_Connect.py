#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/10/25 10:46
# @Author    :risheng.chen@lango-tech.com
# @File      :Rs232_Connect.py
__version__ = '1.0.0'

import serial
import serial.tools.list_ports

RS232_Connect = {
    'power_off': 'AA BB CC 01 01 00 02 DD EE FF',  # 关机
    'power_on': 'AA BB CC 01 00 00 01 DD EE FF',  # 开机
    'Ktc_source': 'F6 4D 01 00 44 6F',  # 获取当前通道信号状态，01表示有信号，00无信号
    'Ktc_HDMI3': 'F6 30 01 13 3A 6F',
    'Ktc_TYPE_C': 'F6 30 01 0C 33 6F',
    'HDMI1': 'AA BB CC 02 06 00 08 DD EE FF',
    'HDMI2': 'AA BB CC 02 07 00 09 DD EE FF',
    'HDMI3': 'AA BB CC 02 05 00 07 DD EE FF',
    'HDMI4': 'AA BB CC 02 0C 00 0E DD EE FF',
    'OPS': 'AA BB CC 02 08 00 0A DD EE FF',
    'ANDROID': 'AA BB CC 02 0A 00 0C DD EE FF',
    'VGA': 'AA BB CC 02 03 00 05 DD EE FF',
    'AV': 'AA BB CC 02 02 00 04 DD EE FF',
    'USB_C_F': 'AA BB CC 02 0B 00 0D DD EE FF',
    'USB_C': 'AA BB CC 02 09 00 0B DD EE FF',
    'volume 50': 'AA BB CC 03 00 32 35 DD EE FF',
    'mute': 'AA BB CC 03 01 00 04 DD EE FF',
    'UnMute': 'AA BB CC 03 01 01 05 DD EE FF',
    'touch_off': 'AA BB CC 38 07 00 3F DD EE FF',
    'touch_on': 'AA BB CC 38 07 01 40 DD EE FF',
    'Freeze/Unfreeze': 'AA BB CC 07 1C 00 23 DD EE FF',
    'Input': 'AA BB CC 07 07 00 0E DD EE FF',
    'home': 'AA BB CC 07 48 00 4F DD EE FF',
    'Menu': 'AA BB CC 07 0D 00 14 DD EE FF',
    'Blank screen': 'AA BB CC 07 4E 00 55 DD EE FF',
    'up': 'AA BB CC 07 47 00 4E DD EE FF',
    'down': 'AA BB CC 07 4D 00 54 DD EE FF',
    'Right': 'AA BB CC 07 4B 00 52 DD EE FF',
    'Left': 'AA BB CC 07 49 00 50 DD EE FF',
    'Enter': 'AA BB CC 07 4A 00 51 DD EE FF',
    'Back/Escape': 'AA BB CC 07 0A 00 11 DD EE FF',
    'vol+': 'AA BB CC 07 03 00 0A DD EE FF',
    'vol-': 'AA BB CC 07 41 00 48 DD EE FF'
}


def get_serial_comport():
    """
    get_serial_comport: 获取设备管理器COM口
    :return: list(comport)[0]
    """
    ports_list = list(serial.tools.list_ports.comports())
    if len(ports_list) <= 0:
        return False
    else:
        for comport in ports_list:
            print(list(comport)[0], list(comport)[1])
            return list(comport)[0]


def open_serial_comport():
    """
    open_serial_comport: 打开串口函数
    :return: ser
    """
    ser = serial.Serial(port=get_serial_comport(), baudrate=9600, timeout=3)
    if ser.isOpen():
        return ser
    else:
        return False


def close_serial_comport():
    """
    close_serial_comport: 关闭串口函数
    :return: True or False
    """
    open_serial_comport().close()
    if open_serial_comport().isOpen():
        return False
    else:
        return True


def serial_sent_hex(command):
    """
    serial_sent_hex:
    bytes.fromhex()使用这个函数进行数据转换，可以把16进制的数值转换字节数据
    (即比特流，字符串与比特流间还可以用encode（）和decode（）进行编解码)字符串与比特流间还可以用encode
    :param command: RS232
    :return: data: 获取指令的返回值，并且进行类型转换，转换为字符串后便可以进行字符串对比，因而便可以根据返回值进行判断是否执行特定功能
    """
    var = bytes.fromhex(RS232_Connect["%s" % command])
    open_serial_comport().write(var)
    data = open_serial_comport().read(10)
    data = str(data, encoding="utf-8")
    return data




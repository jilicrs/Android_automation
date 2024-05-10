#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/3/27 19:48
# @Author    :risheng.chen@lango-tech.com
# @File      :KTC_232_Gather.py
__version__ = '1.0.0'

import serial
import serial.tools.list_ports

RS232_Connect = {
        'Get Mute ON/OFF status': 'F6 02 02 00 FA 6F',  # hex码：OK,ON:返回01,OFF:00
        'Mute_On': 'F6 02 00 01 F9 6F',  # hex码：OK,返回53  ASCII码：返回S
        'Mute Off': 'F6 02 00 00 F8 6F',  # hex码：OK,返回53  ASCII码：返回S
        'Get_Firmware_Version_Scaler': 'F6 03 01 00 FA 6F',  # ASCII码：OK,返回1.0.49
        'Get Firmware Version Touch': 'F6 03 02 00 FB 6F',  # ASCII码：OK,返回V.4806(0x8713)
        # 00数据位，替换密码，ASCII转16进制，12345678的ASCII码转16进制就是31 32 33 34 35 36 37 38，替换oo在计算校验位
        # 例如：F6 5D 03 31 32 33 34 35 36 37 38 FA 6F 设置密码12345678
        'Set WIFI Hotspot Password': 'F6 5D 03 00 56 6F',
        'HDMI1': 'AA BB CC 02 06 00 08 DD EE FF',
        'Input': 'AA BB CC 07 07 00 0E DD EE FF',
        'Ktc_HDMI3': 'F6 30 01 13 3A 6F',
        'OPS': 'AA BB CC 02 08 00 0A DD EE FF',
        'ANDROID': 'AA BB CC 02 0A 00 0C DD EE FF',
        'HDMI2': 'AA BB CC 02 07 00 09 DD EE FF',
        'USB_C_F': 'AA BB CC 02 0B 00 0D DD EE FF',
        'iiyama_poweroff' : 'A6 01 00 00 00 04 01 18 01 BB',
        'iiyama_poweron' : 'A6 01 00 00 00 04 01 18 02 B8',
        'reboot' : '36 E5 E3 1D'
}

def get_serial_comport():
    ports_list = list(serial.tools.list_ports.comports())
    if len(ports_list) <= 0:
        return False
    else:
        for comport in ports_list:
            print(list(comport)[0])
            return list(comport)[0]


def serial_sent_hex(command):
    ser = serial.Serial(get_serial_comport(), 9600, timeout=3)
    var = bytes.fromhex(RS232_Connect["%s" % command])
    ser.write(var)
    data = ser.read(10)
    data = str(data, encoding="utf-8")
    return data


if __name__ == '__main__':
    serial_sent_hex('reboot')


























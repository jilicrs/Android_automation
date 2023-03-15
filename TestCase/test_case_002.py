#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/8/10 11:38
# @Author    :risheng.chen@lango-tech.com
# @File      :test_case_002.py
__version__ = '1.0.0'

import time
import serial.tools.list_ports


ports_list = list(serial.tools.list_ports.comports())
if len(ports_list) <= 0:
    print('没有找到可用串口设备')
else:
    print('找到以下可用串口设备:')
    for comport in ports_list:
        print(list(comport)[0], list(comport)[1])

time.sleep(1)
# 打开COM6，波特率为9600，其余参数使用默认值
ser = serial.Serial(port='COM6',
                    baudrate=9600,
                    # 数据位
                    bytesize=serial.SEVENBITS,
                    parity=serial.PARITY_NONE,
                    # 停止位
                    stopbits=serial.STOPBITS_TWO,
                    timeout=2)
# 判断串口是否成功打开
if ser.isOpen():
    print('打开串口成功！！')
    print(ser.name)
    # write_len = ser.write('AA E1 12 01 A7 FF'.encode('utf-8'))
    # print('串口发动{}个字节'.format(write_len))
    # receive = ser.read(write_len)
    # print('接收{}个字节'.format(receive))
else:
    print('打开串口失败,请检查串口是否被占用')

rs232 = {
    'HDMI1': 'AA BB CC 02 06 00 08 DD EE FF',
}


def comport(command):
    var = bytes.fromhex(rs232['%s' % command])
    ser.write(var)
    data = ser.read(10)
    # 获取指令的返回值，并且进行类型转换，转换为字符串后便可以进行字符串对比，因而便可以根据返回值进行判断是否执行特定功能
    data = str(data, encoding="utf-8")
    return data


if __name__ == '__main__':
    hex1 = comport('HDMI1')
    print(hex1)


# time.sleep(2)
# # 关闭串口
# ser.close()
# # 判断串口是否关闭
# if ser.isOpen():
#     print('串口未关闭')
# else:
#     print('串口已关闭')



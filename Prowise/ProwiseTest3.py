#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/11/12 18:20
# @Author    :risheng.chen@lango-tech.com
# @File      :ProwiseTest3.py
__version__ = '1.0.0'

import tkinter as tk
import time
import serial
import datetime
import serial.tools.list_ports


RS232_Connect = {
    # 'OPS': 'F6 30 01 12 39 6F',
    # 'HDMI_1': 'F6 30 01 09 30 6F',
    # 'HDMI_2': 'F6 30 01 0A 31 6F',
    # 'HDMI_3': 'F6 30 01 13 3A 6F',
    # 'VGA': 'F6 30 01 08 2F 6F',
    # 'TYPE_C': 'F6 30 01 0C 33 6F',
    # 'TYPE_C_FRONT': 'F6 30 01 15 3C 6F',
    # 'ANDROID': 'F6 30 01 0B 32 6F',
    # 'AV': 'F6 30 01 02 29 6F ',
    # 'source': 'F6 4D 01 00 44 6F',
    'power_off': 'AA BB CC 01 01 00 02 DD EE FF',  # 关机
    'power_on': 'AA BB CC 01 00 00 01 DD EE FF',  # 开机
    'HDMI1': 'AA BB CC 02 06 00 08 DD EE FF',
    'HDMI2': 'AA BB CC 02 07 00 09 DD EE FF',
    'HDMI3': 'AA BB CC 02 05 00 07 DD EE FF',
    'HDMI4': 'AA BB CC 02 0C 00 0E DD EE FF',
    'OPS': 'AA BB CC 02 08 00 0A DD EE FF',
    'Central': 'AA BB CC 02 0A 00 0C DD EE FF',
    'VGA': 'AA BB CC 02 03 00 05 DD EE FF',
    'AV': 'AA BB CC 02 02 00 04 DD EE FF',
    'USBC Front': 'AA BB CC 02 0B 00 0D DD EE FF',
    'USBC mainboard': 'AA BB CC 02 09 00 0B DD EE FF',
    'volume 50': 'AA BB CC 03 00 32 35 DD EE FF',
    'mute': 'AA BB CC 03 01 00 04 DD EE FF',
    'unmute': 'AA BB CC 03 01 01 05 DD EE FF',
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
    ports_list = list(serial.tools.list_ports.comports())
    if len(ports_list) <= 0:
        print('没有找到可用的串口')
    else:
        print('找到以下可用串口设备:')
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


def main():
    StartTest = int(input("输入开始测试次数:"))
    MaxTest = int(input("请输入最大测试次数："))

    # command = serial_sent_hex('source')
    # print(command)

    while True:
        if StartTest <= MaxTest:
            print('开始执行第{}次测试'.format(StartTest))
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex1 = serial_sent_hex('HDMI1')
            # print('%s:切换HDMI1' % NowTime, command_hex1)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex2 = serial_sent_hex('HDMI2')
            # print('%s:切换HDMI2' % NowTime, command_hex2)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex3 = serial_sent_hex('HDMI3')
            # print('%s:切换HDMI3' % NowTime, command_hex3)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex4 = serial_sent_hex('HDMI4')
            # print('%s:切换HDMI4' % NowTime, command_hex4)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex5 = serial_sent_hex('OPS')
            # print('%s:切换OPS' % NowTime, command_hex5)
            # time.sleep(5)
            NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            command_hex6 = serial_sent_hex('Central')
            print('%s:切换android' % NowTime, command_hex6)
            time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex7 = serial_sent_hex('VGA')
            # print('%s:切换vga' % NowTime, command_hex7)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex8 = serial_sent_hex('AV')
            # print('%s:切换AV' % NowTime, command_hex8)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex9 = serial_sent_hex('USBC Front')
            # print('%s:切换usbc front' % NowTime, command_hex9)
            # time.sleep(15)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex10 = serial_sent_hex('USBC mainboard')
            # print('%s:切换usbc mainboard' % NowTime, command_hex10)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex11 = serial_sent_hex('volume 50')
            # print('%s:设置音量50' % NowTime, command_hex11)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex13 = serial_sent_hex('mute')
            # print('%s:静音' % NowTime, command_hex13)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex14 = serial_sent_hex('unmute')
            # print('%s:取消静音' % NowTime, command_hex14)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex15 = serial_sent_hex('touch_off')
            # print('%s:禁用触摸' % NowTime, command_hex15)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex16 = serial_sent_hex('touch_on')
            # print('%s:启用触摸' % NowTime, command_hex16)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex17 = serial_sent_hex('Freeze/Unfreeze')
            # print('%s:冻屏' % NowTime, command_hex17)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex18 = serial_sent_hex('Freeze/Unfreeze')
            # print('%s:取消冻屏' % NowTime, command_hex18)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex19 = serial_sent_hex('Input')
            # print('%s:信号源' % NowTime, command_hex19)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex20 = serial_sent_hex('home')
            # print('%s:主页' % NowTime, command_hex20)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex21 = serial_sent_hex('Menu')
            # print('%s:静音' % NowTime, command_hex21)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex22 = serial_sent_hex('Blank screen')
            # print('%s:息屏' % NowTime, command_hex22)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex23 = serial_sent_hex('Blank screen')
            # print('%s:取消息屏' % NowTime, command_hex23)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex24 = serial_sent_hex('up')
            # print('%s:上' % NowTime, command_hex24)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex25 = serial_sent_hex('down')
            # print('%s:下' % NowTime, command_hex25)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex26 = serial_sent_hex('Right')
            # print('%s:右' % NowTime, command_hex26)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex27 = serial_sent_hex('Left')
            # print('%s:左' % NowTime, command_hex27)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex28 = serial_sent_hex('Enter')
            # print('%s:确定' % NowTime, command_hex28)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex29 = serial_sent_hex('Back/Escape')
            # print('%s:退出' % NowTime, command_hex29)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex30 = serial_sent_hex('vol+')
            # print('%s:音量+' % NowTime, command_hex30)
            # time.sleep(5)
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex31 = serial_sent_hex('vol-')
            # print('%s:音量-' % NowTime, command_hex31)
            # time.sleep(5)

            # command_hex1 = serial_sent_hex('OPS')
            # print('%s:关机' % NowTime, command_hex1)
            # if command_hex1 == 'S':
            #     print('%s:切换OPS' % NowTime, command_hex1)
            #     time.sleep(10)
            # else:
            #     print('%s:指令发送异常，请检查日志信息' % NowTime)
            #     break
            # NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # command_hex7 = serial_sent_hex('TYPE_C_FRONT')
            # if command_hex7 == "S":
            #     print('%s:切换TYPE_C_FRONT' % NowTime, command_hex7)
            #     time.sleep(10)
            # else:
            #     print('%s:指令发送异常，请检查日志信息' % NowTime)
            #     break
            StartTest = StartTest + 1
        elif StartTest > MaxTest:
            ThisTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            print('%s:测试完成，退出程序' % ThisTime)
            break


if __name__ == '__main__':
    main()

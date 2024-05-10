#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/9/7 17:27
# @Author    :risheng.chen@lango-tech.cn
# @File      :change_panel.py
__version__ = '1.0.0'

import time
import datetime
import serial
import serial.tools.list_ports

change_panel_rs232 = {
    'get_panel': '89 60 29 ED',
    'panel0': 'A9 60 26 00 D0',
    'panel1': 'A9 60 26 01 CF',
    'panel2': 'A9 60 26 02 CE',
    'panel3': 'A9 60 26 03 CD',
    'panel4': 'A9 60 26 04 CC',
    'panel6': 'AA 0A E5 01 00 00 00 06 D7 4B',
}

def waite():
    msg = '等待事件：'
    for times in range(20, -1, -1):
        print("\r{} {}seconds ".format(msg, times), end='')
        time.sleep(1)


def get_serial_comport():
    ports_list = list(serial.tools.list_ports.comports())
    if len(ports_list) <= 0:
        return False
    else:
        for comport in ports_list:
            print(list(comport)[0], list(comport)[1])
            return list(comport)[0]


ser = serial.Serial(port=get_serial_comport(), baudrate=115200, timeout=1)


def close_serial_comport():
    ser.close()
    if ser.is_open:
        return False
    else:
        return True


def get_data():
    while True:
        data = ser.readline().decode('utf-8').strip()
        if data:
            print('Received data:', data)
            if 'Enter main loop at' in data:
                return True
        time.sleep(0.1)


def serial_sent_hex(command):
    var = bytes.fromhex(change_panel_rs232["%s" % command])
    ser.write(var)
    data = ser.read(12)
    data = str(data, encoding="utf-8")
    print(data)
    return data

def main():
    success_count = 0
    fail_count = 0
    max_test = 5000
    start_test = 1
    while True:
        if start_test < max_test:
            print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                  '开始执行{}次测试，测试成功{}次，失败{}次'.format(start_test, success_count, fail_count))
            if ser.isOpen():
                pass
            else:
                ser.open()
            get_panel_1 = serial_sent_hex('get_panel')
            ser.close()
            print(get_panel_1)
            if '61_11_29_02' in  get_panel_1:
                print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') + '当前屏参：02，即将切换03')
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                serial_sent_hex('panel3')
                ser.close()
                if ser.isOpen():
                   pass
                else:
                    ser.open()
                get_data()
                ser.close()
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                get_panel_2 = serial_sent_hex('get_panel')
                ser.close()
                if '61_11_29_03' in get_panel_2:
                    success_count += 1
                    start_test += 1
                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                        '屏参切换03正常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    continue
                else:
                    fail_count += 1
                    start_test += 1
                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                        '屏参切换03异常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    continue
            elif '61_11_29_03' in  get_panel_1:
                print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') + '当前屏参：03，即将切换04')
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                serial_sent_hex('panel4')
                ser.close()
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                get_data()
                ser.close()
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                get_panel_3 = serial_sent_hex('get_panel')
                ser.close()
                if '61_11_29_04' in get_panel_3:
                    success_count += 1
                    start_test += 1
                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                        '屏参切换04正常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    continue
                else:
                    fail_count += 1
                    start_test += 1
                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                        '屏参切换04异常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    continue
            elif '61_11_29_04' in  get_panel_1:
                print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') + '当前屏参：04，即将切换02')
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                serial_sent_hex('panel2')
                ser.close()
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                get_data()
                ser.close()
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                get_panel_4 = serial_sent_hex('get_panel')
                ser.close()
                if '61_11_29_02' in get_panel_4:
                    success_count += 1
                    start_test += 1
                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                          '屏参切换02正常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    continue
                else:
                    fail_count += 1
                    start_test += 1
                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                          '屏参切换02异常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    continue
        elif start_test == max_test:
            print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                  '测试{}次完成，测试成功{}次，失败{}次')
            break



if __name__ == '__main__':
   main()




























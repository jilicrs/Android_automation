#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/9/14 10:51
# @Author    :risheng.chen@lango-tech.cn
# @File      :change_panel_311D2K.py
__version__ = '1.0.0'

import time
import datetime
import serial
import serial.tools.list_ports
import binascii

change_panel_rs232 = {
    # 激活串口
    'start_comport': 'AA 06 10 01 A7 EF',
    # 获取屏参
    'get_panel': 'AA 06 E5 00 5B FA',
    # 43寸屏参
    'panel0': 'AA 0A E5 01 00 00 00 00 B7 8D',
    # 50寸屏参
    'panel1': 'AA 0A E5 01 00 00 00 01 A7 AC',
    # 55寸屏参
    'panel2': 'AA 0A E5 01 00 00 00 02 97 CF',
    # 65寸屏参
    'panel3': 'AA 0A E5 01 00 00 00 03 87 EE',
    # 75寸屏参
    'panel4': 'AA 0A E5 01 00 00 00 04 F7 09',
    # 86寸屏参
    'panel5': 'AA 0A E5 01 00 00 00 05 E7 28',
    # 98寸屏参
    'panel6': 'AA 0A E5 01 00 00 00 06 D7 4B',
}


def get_serial_comport():
    ports_list = list(serial.tools.list_ports.comports())
    if len(ports_list) <= 0:
        return False
    else:
        for comport in ports_list:
            print(list(comport)[0], list(comport)[1])
            return list(comport)[0]


ser = serial.Serial(port=get_serial_comport(), baudrate=115200, timeout=3)


def close_serial_comport():
    ser.close()
    if ser.isOpen():
        return False
    else:
        return True


def get_data():
    while True:
        data = ser.readline().hex().strip()
        if data:
            print('Received data:', data)
            if '4e4f544943453a20203258204f5450312043524320504153530d0a' in data:
                ser.close()
                print('已开机')
                break
        time.sleep(0.1)


def serial_sent_hex(command):
    var = bytes.fromhex(change_panel_rs232["%s" % command])
    ser.write(var)
    data = ser.read(20)
    deco = binascii.b2a_hex(data)
    deco_str = str(deco)
    print(deco_str)
    return deco_str

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
            if '0000000000' in  get_panel_1:
                print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') + '当前屏参：00，即将切换01')
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                serial_sent_hex('panel1')
                ser.close()
                if ser.isOpen():
                   pass
                else:
                    ser.open()
                get_data()
                ser.close()
                time.sleep(20)
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                serial_sent_hex('start_comport')
                ser.close()
                time.sleep(1)
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                get_panel_2 = serial_sent_hex('get_panel')
                ser.close()
                if '0000000001' in get_panel_2:
                    success_count += 1
                    start_test += 1
                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                        '屏参切换01正常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    continue
                else:
                    fail_count += 1
                    start_test += 1
                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                        '屏参切换01异常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    continue
            elif '0000000001' in  get_panel_1:
                print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') + '当前屏参：01，即将切换02')
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
                time.sleep(20)
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                serial_sent_hex('start_comport')
                ser.close()
                time.sleep(1)
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                get_panel_3 = serial_sent_hex('get_panel')
                ser.close()
                if '0000000002' in get_panel_3:
                    success_count += 1
                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                        '屏参切换02正常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    start_test += 1
                    continue
                else:
                    fail_count += 1
                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                        '屏参切换02异常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    start_test += 1
                    continue
            elif '0000000002' in  get_panel_1:
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
                time.sleep(20)
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                serial_sent_hex('start_comport')
                ser.close()
                time.sleep(1)
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                get_panel_4 = serial_sent_hex('get_panel')
                ser.close()
                if '0000000003' in get_panel_4:
                    success_count += 1

                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                          '屏参切换03正常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    start_test += 1
                    continue
                else:
                    fail_count += 1

                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                          '屏参切换03异常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    start_test += 1
                    continue
            elif '0000000003' in  get_panel_1:
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
                time.sleep(20)
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                serial_sent_hex('start_comport')
                ser.close()
                time.sleep(1)
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                get_panel_4 = serial_sent_hex('get_panel')
                ser.close()
                if '0000000004' in get_panel_4:
                    success_count += 1

                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                          '屏参切换04正常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    start_test += 1
                    continue
                else:
                    fail_count += 1

                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                          '屏参切换04异常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    start_test += 1
                    continue
            elif '0000000004' in  get_panel_1:
                print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') + '当前屏参：04，即将切换05')
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                serial_sent_hex('panel5')
                ser.close()
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                get_data()
                ser.close()
                time.sleep(20)
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                serial_sent_hex('start_comport')
                ser.close()
                time.sleep(1)
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                get_panel_4 = serial_sent_hex('get_panel')
                ser.close()
                if '0000000005' in get_panel_4:
                    success_count += 1
                    start_test += 1
                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                          '屏参切换05正常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    continue
                else:
                    fail_count += 1

                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                          '屏参切换05异常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    start_test += 1
                    continue
            elif '0000000005' in  get_panel_1:
                print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') + '当前屏参：05，即将切换06')
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                serial_sent_hex('panel6')
                ser.close()
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                get_data()
                ser.close()
                time.sleep(20)
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                serial_sent_hex('start_comport')
                ser.close()
                time.sleep(1)
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                get_panel_4 = serial_sent_hex('get_panel')
                ser.close()
                if '0000000006' in get_panel_4:
                    success_count += 1

                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                          '屏参切换06正常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    start_test += 1
                    continue
                else:
                    fail_count += 1

                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                          '屏参切换06异常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    start_test += 1
                    continue
            elif '0000000006' in  get_panel_1:
                print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') + '当前屏参：06，即将切换00')
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                serial_sent_hex('panel0')
                ser.close()
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                get_data()
                ser.close()
                time.sleep(20)
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                serial_sent_hex('start_comport')
                ser.close()
                time.sleep(1)
                if ser.isOpen():
                    pass
                else:
                    ser.open()
                get_panel_4 = serial_sent_hex('get_panel')
                ser.close()
                if '0000000000' in get_panel_4:
                    success_count += 1

                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                          '屏参切换00正常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    start_test += 1
                    continue
                else:
                    fail_count += 1

                    print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                          '屏参切换00异常，第{}次测试完成，成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                    start_test += 1
                    continue

        elif start_test == max_test:
            print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                  '测试{}次完成，测试成功{}次，失败{}次')
            break

if __name__ == '__main__':
    main()
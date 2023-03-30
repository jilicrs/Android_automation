#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/3/7 14:56
# @Author    :risheng.chen@lango-tech.com
# @File      :ProwiseSourceTouchTest.py
__version__ = '1.0.0'

import sys
import datetime
import time
from ProwiseSourceTouch.MonitorMicarray import monitor_micarray
from BasePage.Rs232_Connect import serial_sent_hex
from ProwiseSourceTouch.MonitorUSB import monitor_disk
from ProwiseSourceTouch.MonitorMouse import listen_mouse_click
from ProwiseSourceTouch.Thread import MyThread


def waite():
    msg = 'Simulated click detection in progress：'
    for times in range(21, -1, -1):
        Test = sys.stdout.write("\r{} {}seconds ".format(msg, times))
        time.sleep(1)
        sys.stdout.flush()
        return Test


if __name__ == '__main__':
    # 初始测试次数：
    start_test = 1
    # 测试成功次数
    pass_test = 0
    # 测试失败次数
    false_test = 0
    # USB识别失败次数
    usb_test_false = 0
    # Mic识别错误次数
    mic_test_false = 0
    # 鼠标点击失败次数
    mouse_test_click_false = 0

    while True:
        # 最大测试次数：
        end_test = input('①Number of test end:')
        if end_test.isdigit():
            end_test = int(end_test)
            print('输入测试外部通道，大写：')  # 输入测试外部通道，大写：列如：USB_C
            Source = input('②Test change source:')
            if Source == 'HDMI1' or Source == 'HDMI2' or Source == 'HDMI3' or Source == 'HDMI4' or Source == 'OPS' \
                    or Source == 'USB_C' or Source == 'USB_C_F' or Source == 'ANDROID' or Source == 'VGA' \
                    or Source == 'AV':
                while start_test < end_test:
                    print('{}:start {} test'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), start_test))
                    print('PASS:{}，False:{}'.format(pass_test, false_test))
                    time.sleep(2)
                    print('************1.{}:change {} source************'.format(datetime.datetime.now().
                                                                                 strftime('%Y-%m-%d %H:%M:%S'),
                                                                                 Source))
                    # USB_C
                    command_hex1 = serial_sent_hex(Source)
                    time.sleep(2)
                    print('************2.{}:Click test************'.format(datetime.datetime.now().strftime
                                                                           ('%Y-%m-%d %H:%M:%S')))
                    time.sleep(1)
                    # 创建mouse_click_thread、mic_device_thread 和 usb_device_thread 线程对象
                    mouse_click_thread = MyThread(target=listen_mouse_click)
                    usb_device_thread = MyThread(target=monitor_disk)
                    mic_device_thread = MyThread(target=monitor_micarray)

                    # 启动mouse_click_thread 和 usb_device_thread 线程
                    mouse_click_thread.start()
                    usb_device_thread.start()
                    mic_device_thread.start()

                    # join() 等待线程执行完毕在进行下一步
                    mouse_click_thread.join()
                    usb_device_thread.join()
                    mic_device_thread.join()

                    # 获取鼠标事件与USB检测事件结果：True or False
                    mouse_result = mouse_click_thread.get_result()
                    usb_result = usb_device_thread.get_result()
                    mic_result = mic_device_thread.get_result()

                    print(mouse_result, usb_result, mic_result)

                    if mouse_result == True and usb_result == True and mic_result == True:
                        time.sleep(2)
                        print('==========================================================================='
                              '===================')
                        print('Test Result：{}:The {} test pass'.format(datetime.datetime.now().strftime
                              ('%Y-%m-%d %H:%M:%S'), start_test), mouse_click_thread, usb_device_thread,
                              mic_device_thread)
                        print('=========================================================================='
                              '====================')
                        pass_test += 1
                        start_test = start_test + 1
                        time.sleep(2)
                        print('3.{}:change android'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                        # command_hex2 = serial_sent_hex(command='ANDROID')
                        time.sleep(3)
                        continue
                    elif not mouse_result:
                        time.sleep(2)
                        print('{}: The {} test times Error:Coordinates not clicked!!!'.format
                              (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), start_test))
                        false_test += 1
                        mouse_test_click_false += 1
                        start_test += 1
                        continue
                    elif not usb_result:
                        print('{}: The {} test times Error:USB device identification error!!!'.format
                              (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), start_test))
                        false_test += 1
                        usb_test_false += 1
                        start_test += 1
                        continue
                    elif not mic_result:
                        print('{}: The {} test times Error:Mic device identification error!!!'.format
                              (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), start_test))
                        false_test += 1
                        mic_test_false += 1
                        start_test += 1
                        continue
                    elif start_test > end_test:
                        print('{}:Total test {} times; Test PASS {} times, test False {} times'.format
                              (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), end_test, pass_test, false_test))
                        print('mouse click test fail {} times, USB device test fail {} times, Mic device test fail'
                              '{} times'.format(mouse_test_click_false, usb_test_false, mic_test_false))
                        input('============Press Enter to Exit============')
                        break
            else:
                print(r'\\\\\\\\\\\\\\\\\\\The channel is not supported or the input is incorrect//////////////////')
                continue
        else:
            print(r'\\\\\\\\\\\\\\\\\\\\\\\\\Need to enter integer/////////////////////////////')
            continue

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/9/14 19:16
# @Author    :risheng.chen@lango-tech.cn
# @File      :Mic_test.py
__version__ = '1.0.0'

import os
import uiautomator2 as u2
import datetime
from screenshot.Contrast_Screenshot import compare
import time


# ip = "an4009059505841601b13"

ip = input('输入整机IP:')

device = u2.connect_usb(ip)


def open_record_app():
    """
    open_record_app:此函数为打开record app函数
    :return: True or False
    """
    try:
        device.app_start('com.digipom.easyvoicerecorder.pro')
    except RuntimeError as e:
        print('app start error:', e)
        input('press enter to exit')
        raise e
    time.sleep(1)
    get_app = os.popen('adb -s {} shell dumpsys window | findstr mCurrentFocus'.format(ip)).read()
    if 'com.digipom.easyvoicerecorder.pro' in get_app:
        print('1.打开录音应用成功！')
        return True
    else:
        print('1.录音应用打开失败！')
        return False

def click_reocrd():
    """
    click_reocrd:开始录音
    :return: True or False
    """
    # device(resourceId="android:id/button1").click_exists(timeout=3)
    return device(resourceId="com.digipom.easyvoicerecorder.pro:id/record_pause_button").click_exists(timeout=3)




def main():
    """
    main:主函数
    :return: True or False
    """
    max_test = 5000
    start_test = 1
    success_count = 0
    fail_count = 0


    while True:
        if start_test <= max_test:
            print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                  '开始执行{}次测试，测试成功{}次，失败{}次'.format(start_test, success_count, fail_count))
            open_record_app()
            time.sleep(2)
            click_reocrd()
            time.sleep(5)
            click_reocrd()
            os.system('adb -s {} shell screencap -p /sdcard/1.png'.format(ip))
            now_time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_')
            os.system('adb -s {} pull sdcard/1.png D:\\screenshots\\{}1.png'.format(ip, now_time))
            device(resourceId="com.digipom.easyvoicerecorder.pro:id/cancel_button").click_exists(timeout=3)
            device(resourceId="android:id/button1").click_exists(timeout=3)

            file_path = 'D:\\screenshots\\'
            lists = os.listdir(path=file_path)
            lists.sort(key=lambda x: os.path.getmtime((file_path + "\\" + x)))
            file_new = os.path.join(file_path, lists[-1])

            #截图的图片路径
            picscreenshot = file_new.replace('\\', '/', 100)
            #保存的图片路径
            picnorecord =  rb"D:\screenshots\2.png"

            if compare(picscreenshot, picnorecord):
                success_count += 1
                print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                         '第{}次测试完成，测试成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                start_test += 1
                os.system('adb reboot')
                time.sleep(45)
                continue
            else:
                fail_count += 1
                print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                         '第{}次测试完成，测试成功{}次，失败{}次'.format(start_test, success_count, fail_count))
                start_test += 1
                os.system('adb -s {} shell logcat -v time > D:\\logs\\logcat.txt'.format(ip))
                input('press the enter to exit:')
                break
        elif start_test > max_test:
            print(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                         '第{}次测试完成，测试成功{}次，失败{}次'.format(max_test, success_count, fail_count))
            input('press the enter to exit:')
            break


if __name__ == '__main__':
    main()
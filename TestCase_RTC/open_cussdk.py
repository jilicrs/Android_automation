"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2023/11/22 19:34
@Author    :risheng.chen@lango-tech.cn
@File      :open_cussdk.py
__version__ = '1.0.0'
"""

import uiautomator2 as u2

ip = 'hht12345678'

d = u2.connect_usb()



def open_sdk():
    """
    open_sdk:打开中间件测试工具
    :return: true or false
    """
    try:
        d.app_start('com.xbh.sdk.demo')
        return True
    except Exception as e:
        print('app start error', e)
        return False



def isCorrectIp():
    """
    isCorrectIp:此函数判断设备为OTG或IP
    :return:true为网络adb,false为OTG
    """
    if 13 <= len(ip) < 15:
        if ip[3] == '.' and ip[7] == '.':
            if ip[0].isnumeric() and ip[1].isnumeric() and ip[2].isnumeric()\
                    and ip[4].isnumeric() and ip[5].isnumeric() and ip[6].isnumeric()\
                    and ip[8].isnumeric() and ip[-1].isnumeric() and ip[-2].isnumeric()\
                    and ip[-3].isnumeric():
                print('网络adb', ip)
                return True
            else:
                print(type(ip))
                print('非法ip')
                return False
        else:
            print('OTG')
            return False
    else:
        print('OTG')
        return False




if __name__ == '__main__':

    isCorrectIp()

























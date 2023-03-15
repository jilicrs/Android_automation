#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/7/14 21:24
# @Author    :risheng.chen@lango-tech.com
# @File      :globals.py
__version__ = '1.0.0'

import datetime
import platform
import re
import uiautomator2 as u2
import os
import time
from Logger.getlogger import Logging

device = str(input('输入测试设备IP：'))


class AdbConnect(object):
    """
    ADB_connect:此方法用于连接整机设备
    """
    d = u2.connect_adb_wifi(device)
    print(d.info)
    print(d.device_info)

    os.system('adb --version')
    os.system('adb devices')
    devices = os.popen('adb devices').read()

    def __init__(self, devices_id=''):
        self.__devices_id = devices_id
        self.system = platform.system()
        self.__find = ''
        self._command = ''
        self.__get__find()

    def __get__find(self):
        """判断系统类型：windows使用findstr
        Linux使用grep"""
        if self.system == "Windows":
            self.__find = 'findstr'
        else:
            self.__find = 'grep'

    def connection_devices(self):
        """连接指定设备"""
        if self.__devices_id == device:
            return
        self.__devices_id = "-s %s" % self.__devices_id
        print(self.d.device_info())


class BasePage(object):
    def __init__(self):
        self.device = AdbConnect().d

    def app_current(self):
        """
        app_current:方法用于获取当前前台应用 packageName, activity, pid
        :return:
        """
        current = self.device.app_current()
        Logging().getloger().info(current)
        return current

    def app_start(self, packages_name):
        """
        app_start:方法用于打开应用，通过包名打开指定launcher应用
        :param packages_name:
        :return:
        """
        start = self.device.app_start(packages_name)
        Logging().getloger().info('{} app is start'.format(packages_name))
        return start

    def app_stop(self, packages_name):
        """
        app_stop:方法用于关闭app，通过指定报名前关闭应用
        :param packages_name:
        :return:
        """
        stop = self.device.app_stop(packages_name)
        Logging().getloger().info('{} app is stop'.format(packages_name))
        return stop

    def app_clear(self, packages_name):
        """
        app_clear:方法用于清除app数据缓存，清理后台数据，通过指定报名前去清除app数据
        :return:
        """
        clear = self.device.app_clear(packages_name)
        Logging().getlogger().info('{} app is clear'.format(packages_name))
        return clear

    def app_wait(self, packages_name):
        """
        app_wait:方法用于默认等待app启动时间
        :return:
        """
        wait = self.device.app_wait(packages_name)
        return wait

    def GetErrorLog(self):
        """
        GetErrorLog:方法用于测试过程中出现异常时自动到处log到指定目录
        :return:
        """
        log_time = time.strftime("%Y-%m-%d %H:%m:%S", time.localtime(),)
        log_file = 'debug_log' + log_time + '.log'
        log = r'adb logcat > D:\Android automation\Logger\{}'.format(log_file)
        return log

    def now_time(self):
        """
        now_time:方法用于获取当前时间戳
        :return:
        """
        return time.asctime()

    def time(self):
        """
        time:显示当前时间年月日分秒
        :return:
        """
        Now_Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return Now_Time

    def click(self, element):
        """
        click:点击方法
        :return:
        """
        if str(element).startswith("com"):
            return self.device(resourceId=element).click()
        elif re.findall("//", str(element)):
            return self.device.xpath(element).click()
        else:
            return self.device(discription=element).click()

    def click_on_point(self, x, y):
        """点击坐标点"""
        Logging().getloger().save_log('auto_d:{}x={}, y={}'.format("点击坐标：", x, y))
        test = self.device.click(x, y)
        return test




























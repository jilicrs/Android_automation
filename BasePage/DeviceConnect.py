"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/1/2 11:26
@Author    :risheng.chen@lango-tech.cn
@File      :DeviceConnect.py
__version__ = '1.0.0'
"""
import platform
import uiautomator2 as u2



class DeviceConnect(object):

    def __init__(self, devices_id='192.168.14.39'):
        self.__devices_id = devices_id
        self.system = platform.system()
        self.__find = ''
        self._command = ''
        self.__get__find()

    def ConnectDeviceForWifi(self):
        """
        ADB_connect:此方法用于连接整机设备
        """
        device = self.__devices_id
        d = u2.connect_adb_wifi(device)
        return d

    def __get__find(self):
        """判断系统类型：windows使用findstr
        Linux使用grep"""
        if self.system == "Windows":
            self.__find = 'findstr'
        else:
            self.__find = 'grep'


    def DeviceInformation(self):
        """连接指定设备,打印设备信息"""
        if self.__devices_id == self.__devices_id:
            return
        self.__devices_id = "-s %s" % self.__devices_id
        print(self.ConnectDeviceForWifi().device_info())





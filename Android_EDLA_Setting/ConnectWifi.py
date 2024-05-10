"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/2/27 20:21
@Author    :risheng.chen@lango-tech.cn
@File      :ConnectWifi.py
__version__ = '1.0.0'
"""
import sys
import time
import os
import uiautomator2 as u2
from Android_EDLA_Setting.BootWizard import devices


class ConnectWifiForIPV4(object):

    def __init__(self, IP = devices):
        self.ip = IP
        self.d = u2.connect_usb(self.ip)


    def swipe_up(self):
        """
        swipe_up:上滑
        :return:
        """
        w, h = self.d.window_size()
        self.d.swipe(w // 2, h // 2, w // 2, h * 1 // 5)
        time.sleep(1)


    def swipe_down(self):
        """
        swipe_down：下滑
        :return:
        """
        w, h = self.d.window_size()
        self.d.swipe(w // 2, h // 2, w // 2, h * 4 // 5)
        time.sleep(1)


    def find_text(self, text:str, swipe=True) -> bool:
        """
        查找页面元素
        :param text:需要找的元素名称
        :param swipe:true
        :return:
        """
        print("查找元素【{}】".format(text))
        page = self.d.dump_hierarchy()
        if text in page:
            return True
        elif swipe:
            while swipe:
                page = self.d.dump_hierarchy()
                print("向下滑动一次")
                ConnectWifiForIPV4().swipe_down()
                newpage = self.d.dump_hierarchy()
                if text in newpage:
                    return True
                if newpage == page:
                    print("继续上滑")
                    while swipe:
                        page = self.d.dump_hierarchy()
                        print("向上滑动一次")
                        ConnectWifiForIPV4().swipe_up()
                        newpage = self.d.dump_hierarchy()
                        if text in newpage:
                            return True
                        if newpage == page:
                            while swipe:
                                page = self.d.dump_hierarchy()
                                print("向下滑动一次")
                                ConnectWifiForIPV4().swipe_down()
                                newpage = self.d.dump_hierarchy()
                                if text in newpage:
                                    return True
                                if newpage == page:
                                    print("没有找到元素")
                                    return False
        else:
            return False


    def set_connect_wifi(self) -> bool:
        """
        set_connect_wifi:连接无线网络
        :return: True or False
        """
        try:
            MonitorSettingApp = os.popen('adb -s {} shell dumpsys window | findstr mCurrentFocus'.format(self.ip)).read()
            if 'com.android.settings/com.android.settings.Settings' in MonitorSettingApp:
                pass
            else:
                self.d.app_start('com.android.settings')
                print('start setting')
                time.sleep(2)

            while True:
                if self.d.xpath('//*[@text="Wi‑Fi, hotspot"]').exists:
                    self.d(resourceId="android:id/title", text="Network & internet").click_exists(timeout=3)
                    print('-->进入Network & internet')
                    time.sleep(2)
                    continue
                elif self.d.xpath("//*[@text='Airplane mode']").exists:
                    self.d(resourceId="android:id/title", text="Internet").click_exists(timeout=3)
                    print('-->进入Internet')
                    time.sleep(2)
                    continue
                elif self.d.xpath('//*[@content-desc="Fix connectivity"]').exists:
                    while True:

                        WifiButtonSwitch = self.d(resourceId="android:id/switch_widget").info['checked']
                        if WifiButtonSwitch:
                            time.sleep(6)

                            while True:
                                FindWifi = self.d.xpath('//*[@text="LANGO-IPV4-GMS"]').exists
                                if FindWifi:
                                    time.sleep(1)
                                    self.d(resourceId="android:id/title", text="LANGO-IPV4-GMS").click()
                                    print('-->找到WiFi（LANGO-IPV4-GMS）')
                                    time.sleep(2)
                                    InputPassword = self.d.xpath('//*[@text="Password"]').exists
                                    if InputPassword:
                                        os.system(f'adb -s {self.ip} shell input text LGWORK21')
                                        time.sleep(2)
                                        self.d(resourceId="android:id/button1", text='CONNECT').click_exists(timeout=5)
                                        time.sleep(2)
                                        for success in range(61):
                                            WifiConnection = self.d.xpath('//*[@resource-id="android:id/summary"]').get_text()
                                            if 'Connected' in WifiConnection:
                                                print('-->WiFi连接成功，退出setting')
                                                self.d.app_clear('com.android.settings')
                                                return True
                                            elif success == 60:
                                                print('-->WiFi连接失败')
                                                return False
                                            else:
                                                sys.stdout.write('\r' + f'正在检测WiFi是否连接成功 {success}')
                                                sys.stdout.flush()
                                                time.sleep(1)
                                                continue
                                    else:
                                        print('Password is not find')
                                        break
                                elif not FindWifi:
                                    if ConnectWifiForIPV4().find_text(text='LANGO-IPV4-GMS'):
                                        continue
                                else:
                                    break

                        elif not WifiButtonSwitch:
                            self.d(resourceId="android:id/switch_widget").click_exists(timeout=3)
                            print('***打开WiFi')
                            time.sleep(1)
                            continue
                else:
                    print('-->未检测到WiFi界面')
                    break
        except Exception as UiObjectNotFoundError:
            print(f'-->WiFi连接异常{UiObjectNotFoundError}')











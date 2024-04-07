#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/8/28 15:56
# @Author    :risheng.chen@lango-tech.cn
# @File      :edla_buttom.py
__version__ = '1.0.0'

import uiautomator2 as u2

ip = input('IP：')

d = u2.connect_usb(ip)


class SettingsFunction(object):
        def __init__(self):
            self.device = d

        def click_security(self):
            return self.device(resourceId="android:id/title", text="Security").click_exists(timeout=1)

        def click_screen_look(self):
            return self.device(resourceId="android:id/title", text="Screen lock").click_exists(timeout=1)

        def find_display(self):
            return self.device(resourceId="android:id/title", text="Display").click_exists(timeout=1)

        def find_screen_timeout(self):
            return self.device(resourceId="android:id/title", text="Screen timeout").click_exists(timeout=1)

        def set_screen_timeout_30min(self):
            return self.device(resourceId="android:id/title", text="30 minutes").click_exists(timeout=1)

        def find_system(self):
            return self.device(resourceId="android:id/title", text="System").click_exists(timeout=1)

        def stay_awake(self):
            return self.device(resourceId="android:id/title", text="Stay awake").click_exists(timeout=1)

        def developer_options(self):
            return self.device(resourceId="android:id/title", text="Developer options").click_exists(timeout=1)

        def choose_none(self):
            return self.device(resourceId="android:id/title", text="None").click_exists(timeout=1)

        def find_network_setting(self):
            return self.device(resourceId="android:id/title", text="Network & internet").click_exists(timeout=1)

        def find_internet(self):
            return self.device(resourceId="android:id/title", text="Internet").click_exists(timeout=1)

        def wifi_choose_IPV4(self):
            return self.device(resourceId="android:id/title", text="LANGO-IPV4-GMS").click_exists(timeout=5)

        def click_enter(self):
            return self.device.xpath(
                        '//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_ime_action"]/android.'
                        'widget.FrameLayout[1]/android.widget.ImageView[1]').click()

        def click_reset_options(self):
            return self.device(resourceId="android:id/title", text="Reset options").click_exists(timeout=1)

        def click_factory_reset(self):
            return self.device(resourceId="android:id/title", text="Erase all data (factory reset)").\
                click_exists(timeout=1)

        def enter_reset(self):
            return self.device(text="Erase all data").click_exists(timeout=1)





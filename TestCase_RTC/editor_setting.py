"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2023/11/22 19:42
@Author    :risheng.chen@lango-tech.cn
@File      :editor_setting.py
__version__ = '1.0.0'
"""

from TestCase_RTC.open_cussdk import d


def open_setting():
    """
    open_setting:打开系统设置
    :return: true or false
    """
    try:
        d.app_start('com.android.settings')
        return True
    except Exception as e:
        print('setting app start error', e)
        return False


def click_system():
    """
    click_system:点击系统选项，前提需要打开设置
    :return: true or false
    """
    try:
        system = d(resourceId="android:id/title", text="系统").click_exists(timeout=3)
        if system:
            print('click system true')
            return True
        else:
            d.swipe_ext('up')
            system_try = d(resourceId="android:id/title", text="系统").click_exists(timeout=3)
            if system_try:
                print('click system true')
                return True
            else:
                print('click system fail')
                return False
    except Exception as e:
        print('click system fail', e)
        return False


def click_datetime():
    """
    click_datetime:打开日期与时间，前提需要进入系统选项
    :return: true or false
    """
    try:
        date_time = d(resourceId="android:id/title", text="日期和时间").click_exists(timeout=3)
        if date_time:
            print('date time click true')
            return True
        else:
            d.swipe_ext('up')
            date_time_try = d(resourceId="android:id/title", text="日期和时间").click_exists(timeout=3)
            if date_time_try:
                print('date time click true')
                return True
            else:
                print('date time click fail')
                return False
    except Exception as e:
        print('date time click fail', e)
        return False


def close_time_for_notwork():
    """
    close_time_for_notwork:判断使用网络时间是否为开启状态并设置为关闭
    :return:
    """
    try:
        flag = d(resourceId='android:id/switch_widget').info['checked']
        if flag:
            d(resourceId='android:id/switch_widget').click()
            flag_try = d(resourceId='android:id/switch_widget').info['checked']
            if not flag_try:
                print('close time for notwork true')
                return True
            else:
                print('close time for notwork fail')
                return False
        else:
            print('close time for notwork true')
            return True
    except Exception as e:
        print('close time for notwork fail', e)
        return False




























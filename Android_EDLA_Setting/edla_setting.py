# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/8/25 17:54
# @Author    :risheng.chen@lango-tech.cn
# @File      :edla_setting.py
"""此程序为设置EDLA相关设置项，前提需要打开usb debugger
    * open_setting: 打开运行设置应用
    * stop_setting: 停止运行设置应用
    * set_display_30minutes: 设置屏幕显示时间为30minutes
    * set_screen_look_NONE: 设置屏幕锁为NONE
    * set_stay_awake_true: 设置stay awake状态为True
    * set_connect_wifi: 连接指定WiFi网络（LANGO-IPV4-GMS）
    * set_factory_reset: 恢复出厂设置
"""
__version__ = '2.1.4'

import time
import os
# from Android_EDLA_Setting.edla_buttom import SettingsFunction
# from Android_EDLA_Setting.edla_buttom import ip
# from Android_EDLA_Setting.edla_buttom import d
import uiautomator2 as u2

# option = SettingsFunction()


def open_setting(ip, d):
    """
    open_setting:此函数为打开setting函数
    :return: True or False
    """
    try:
        get_app_now = os.popen('adb -s {} shell dumpsys window | findstr mCurrentFocus'.format(ip)).read()
        if 'com.android.settings/com.android.settings.Settings' in get_app_now:
            d.app_stop(package_name='com.android.settings')
            time.sleep(0.5)
            d.app_start(package_name='com.android.settings')
        else:
            os.system('adb -s {} shell am start com.android.settings'.format(ip))
        time.sleep(0.5)
    except Exception as e:
        print('app start error:', e)
        raise e
    get_app = os.popen('adb -s {} shell dumpsys window | findstr mCurrentFocus'.format(ip)).read()
    if 'com.android.settings/com.android.settings.Settings' in get_app:
        print('1.打开设置应用成功！')
        return True
    else:
        print('1.设置应用打开失败！')
        return False

def stop_setting(ip, d):
    """
    stop_setting:关闭setting函数
    :return:True or False
    """
    d.app_stop(package_name='com.android.settings')
    d.press('home')
    os.system('adb -s {} shell dumpsys window | findstr mCurrentFocus'.format(ip))
    get_activity = os.popen('adb -s {} shell dumpsys window | findstr mCurrentFocus'.format(ip)).read()
    if 'com.android.searchlauncher.SearchLauncher' in get_activity:
        print('退出应用返回launcher')
        return True
    else:
        print('退出应用失败')
        return False

def set_display_30minutes(d):
    """
    display_setting:设置screen timeout为30minutes
    :return: True or False
    """
    try:
        # find_display = option.find_display()
        find_display = d(resourceId="android:id/title", text="Display").click_exists(timeout=1)
        if not find_display:




            # find_display2 = option.find_display()
            find_display2 = d(resourceId="android:id/title", text="Display").click_exists(timeout=1)
            if find_display2:
                pass
            else:
                d.swipe_ext('up')
                # find_display3 = option.find_display()
                find_display3 = d(resourceId="android:id/title", text="Display").click_exists(timeout=1)
                if find_display3:
                    pass
                else:
                    print('2.进入display失败!')
            time.sleep(1)
        else:
            pass

        text = d(resourceId='android:id/title').get_text()
        if text in 'Brightness':
            print('2.进入display!')
            # find_screen_timeout = option.find_screen_timeout()
            find_screen_timeout = d(resourceId="android:id/title", text="Screen timeout").click_exists(timeout=1)
            if not find_screen_timeout:
                d.swipe_ext('up')
                # find_screen_timeout2 = option.find_screen_timeout()
                find_screen_timeout2 = d(resourceId="android:id/title", text="Screen timeout").click_exists(timeout=1)
                if find_screen_timeout2:
                    print('3.进入screen timeout!')
                    # set_screen_timeout_30min = option.set_screen_timeout_30min()
                    set_screen_timeout_30min = d(resourceId="android:id/title", text="30 minutes").click_exists(timeout=1)
                    if not set_screen_timeout_30min:
                        d.swipe_ext('up')
                        # set_screen_timeout_30min2 = option.set_screen_timeout_30min()
                        set_screen_timeout_30min2 = d(resourceId="android:id/title", text="30 minutes").click_exists(timeout=1)
                        if set_screen_timeout_30min2:
                            print('4.设置screen timeout 30minute成功!')
                            return True
                        else:
                            print('4.设置screen timeout 30minutes失败!')
                            return False
                    else:
                        print('4.设置screen timeout 30minute成功!')
                        return True
                else:
                    print('3.进入screen timeout失败!')
                    return False
            else:
                print('3.进入screen timeout!')
                # set_screen_timeout_30min_1 = option.set_screen_timeout_30min()
                set_screen_timeout_30min_1 = d(resourceId="android:id/title", text="30 minutes").click_exists(timeout=1)
                if set_screen_timeout_30min_1:
                    print('4.设置screen timeout 30minute成功!')
                    return True
                else:
                    d.swipe_ext('up')
                    # set_screen_timeout_30min_3 = option.set_screen_timeout_30min()
                    set_screen_timeout_30min_3 = d(resourceId="android:id/title", text="30 minutes").click_exists(timeout=1)
                    if set_screen_timeout_30min_3:
                        print('4.设置screen timeout 30minute成功!')
                        return True
                    else:
                        print('4.设置screen timeout 30minutes失败!')
                        return False
        else:
            print('2.进入display失败!')
            return False
    except OSError as e:
        print('2.没有找到这个元素:', e)
        raise e

def set_screen_look_NONE(d):
    """
    set_screen_look_NONE:设置screen look模式为NONE
    :return:
    """
    try:
        # click_security = option.click_security()
        click_security = d(resourceId="android:id/title", text="Security").click_exists(timeout=1)
        if click_security:
            print('4.进入security!')
            get_start = d(resourceId='android:id/title').get_text()
            if 'Google Play Protect' in get_start:
                # click_screen_look = option.click_screen_look()
                click_screen_look = d(resourceId="android:id/title", text="Screen lock").click_exists(timeout=1)
                if click_screen_look:
                    print('5.进入screen look!')
                    # choose_NONE = option.choose_none()
                    choose_NONE = d(resourceId="android:id/title", text="None").click_exists(timeout=1)
                    if choose_NONE:
                        print('6.选择NONE')
                        return True
                    else:
                        print('6.选择NONE失败')
                        return False
                else:
                    d.swipe_ext('up')
                    # click_screen_look2 = option.click_screen_look()
                    click_screen_look2 = d(resourceId="android:id/title", text="Screen lock").click_exists(timeout=1)
                    if click_screen_look2:
                        print('5.进入screen look!')
                        # choose_NONE = option.choose_none()
                        choose_NONE = d(resourceId="android:id/title", text="None").click_exists(timeout=1)
                        if choose_NONE:
                            print('6.选择NONE')
                            return True
                        else:
                            print('123 6.选择NONE失败')
                            return False
                    else:
                        print('5.进入screen look失败!')
                        return False
            else:
                print('security界面异常')
                return False
        else:
            d.swipe_ext('up')
            # click_security2 = option.click_security()
            click_security2 = d(resourceId="android:id/title", text="Security").click_exists(timeout=1)
            if click_security2:
                # click_screen_look2 = option.click_screen_look()
                click_screen_look2 = d(resourceId="android:id/title", text="Screen lock").click_exists(timeout=1)
                if click_screen_look2:
                    print('5.进入screen look!')
                    # choose_NONE = option.choose_none()
                    choose_NONE = d(resourceId="android:id/title", text="None").click_exists(timeout=1)
                    if choose_NONE:
                        print('6.选择NONE')
                        return True
                    else:
                        print('456 6.选择NONE失败')
                        return False
                else:
                    print('5.进入screen look失败!')
                    return False
            else:
                print('5.进入screen look失败!')
                return False
    except Exception as e:
        print('4.设置security异常', e)
        raise e

def set_stay_awake_true(d):
    """
    set_stay_awake_true:设置awake为开启状态
    :return: True or False
    """
    try:
        # find_system = option.find_system()
        find_system = d(resourceId="android:id/title", text="System").click_exists(timeout=1)
        if not find_system:
            d.swipe_ext('up')
            # find_system2 = option.find_system()
            find_system2 = d(resourceId="android:id/title", text="System").click_exists(timeout=1)
            if not find_system2:
                d.swipe_ext('up')
                # find_system3 = option.find_system()
                find_system3 = d(resourceId="android:id/title", text="System").click_exists(timeout=1)
                if find_system3:
                    print('7.进入system!')
                    get_text = d(resourceId='android:id/title').get_text()
                    if 'Languages' in get_text:
                        pass
                    else:
                        print('进入system异常')
                        return False
                else:
                    print('进入system异常')
                    return False
            else:
                pass
        else:
            pass
        # input_developer = option.developer_options()
        input_developer = d(resourceId="android:id/title", text="Developer options").click_exists(timeout=1)
        if input_developer:
            print('8.进入Developer options!')
            # choose_true = option.stay_awake()
            choose_true = d(resourceId="android:id/title", text="Stay awake").click_exists(timeout=1)
            if choose_true:
                print('9.设置stay awake为true!')
                return True
            else:
                d.swipe_ext('up')
                # choose_true2 = option.stay_awake()
                choose_true2 = d(resourceId="android:id/title", text="Stay awake").click_exists(timeout=1)
                if choose_true2:
                    print('9.设置stay awake为true!')
                    return True
                else:
                    print('9.设置stay awake失败!')
                    return False
        else:
            print('8.进入Developer options失败!')
            return False
    except Exception as e:
        print('7.进入system异常', e)
        raise e

def swipe_up(d):
    """
    swipe_up:上滑
    :param d:
    :return:
    """
    w, h = d.window_size()
    d.swipe(w // 2, h // 2, w // 2, h * 1 // 5)
    time.sleep(1)

def swipe_down(d):
    """
    swipe_down：下滑
    :param d:
    :return:
    """
    w, h = d.window_size()
    d.swipe(w // 2, h // 2, w // 2, h * 4 // 5)
    time.sleep(1)


def find_text(d, text, swipe=True):
    """
    查找页面元素
    :param text:
    :param swipe:
    :return:
    """
    print("查找元素【{}】".format(text))
    page = d.dump_hierarchy()
    if text in page:
        return True
    elif swipe:
        while swipe:
            page = d.dump_hierarchy()
            print("向下滑动一次")
            swipe_down(d)
            newpage = d.dump_hierarchy()
            if text in newpage:
                return True
            if newpage == page:
                print("继续上滑")
                while swipe:
                    page = d.dump_hierarchy()
                    print("向上滑动一次")
                    swipe_up(d)
                    newpage = d.dump_hierarchy()
                    if text in newpage:
                        return True
                    if newpage == page:
                        while swipe:
                            page = d.dump_hierarchy()
                            print("向下滑动一次")
                            swipe_down(d)
                            newpage = d.dump_hierarchy()
                            if text in newpage:
                                return True
                            if newpage == page:
                                print("没有找到元素")
                                return False
    else:
        return False


def set_connect_wifi(ip, d):
    """
    set_connect_wifi:连接无线网络
    :return: True or False
    """
    try:
        MonitorSettingApp = os.popen('adb -s {} shell dumpsys window | findstr mCurrentFocus'.format(ip)).read()
        if 'com.android.settings/com.android.settings.Settings' in MonitorSettingApp:
            pass
        else:
            d.app_start('com.android.settings')
            print('start setting')
            time.sleep(2)

        while True:
            if d.xpath('//*[@text="Wi‑Fi, hotspot"]').exists:
                d(resourceId="android:id/title", text="Network & internet").click_exists(timeout=3)
                print('-->进入Network & internet')
                time.sleep(2)
                continue
            elif d.xpath("//*[@text='Airplane mode']").exists:
                d(resourceId="android:id/title", text="Internet").click_exists(timeout=3)
                print('-->进入Internet')
                time.sleep(2)
                continue
            elif d.xpath('//*[@content-desc="Fix connectivity"]').exists:
                while True:

                    WifiButtonSwitch = d(resourceId="android:id/switch_widget").info['checked']
                    if WifiButtonSwitch:
                        time.sleep(6)

                        while True:
                            FindWifi = d.xpath('//*[@text="LANGO-IPV4-GMS"]').exists
                            if FindWifi:
                                time.sleep(1)
                                d(resourceId="android:id/title", text="LANGO-IPV4-GMS").click()
                                print('-->找到WiFi（LANGO-IPV4-GMS）')
                                time.sleep(2)
                                InputPassword = d.xpath('//*[@text="Password"]').exists
                                if InputPassword:
                                    os.system(f'adb -s {ip} shell input text LGWORK21')
                                    time.sleep(2)
                                    d(resourceId="android:id/button1", text='CONNECT').click_exists(timeout=5)
                                    time.sleep(6)
                                    WifiConnection = d.xpath('//*[@resource-id="android:id/summary"]').get_text()
                                    if 'Connected' in WifiConnection:
                                        print('-->WiFi连接成功，退出setting')
                                        d.app_clear('com.android.settings')
                                        return True
                                    else:
                                        print('-->WiFi连接失败')
                                        return False
                                else:
                                    print('Password is not find')
                                    break
                            elif not FindWifi:
                                if find_text(d=d, text='LANGO-IPV4-GMS'):
                                    continue
                            else:
                                break

                    elif not WifiButtonSwitch:
                        d(resourceId="android:id/switch_widget").click_exists(timeout=3)
                        print('***打开WiFi')
                        time.sleep(1)
                        continue
            else:
                print('-->未检测到WiFi界面')
                break
    except Exception as UiObjectNotFoundError:
        print(f'-->WiFi连接异常{UiObjectNotFoundError}')



def set_factory_reset(d):
    """
    set_factory_reset:恢复出厂设置
    :return:True or False
    """
    try:
        d.swipe_ext('up')
        time.sleep(0.5)
        d.swipe_ext('up')
        # click_system = option.find_system()
        click_system = d(resourceId="android:id/title", text="System").click_exists(timeout=1)
        if click_system:
            d.swipe_ext('up')
            # click_reset_options = option.click_reset_options()
            click_reset_options = d(resourceId="android:id/title", text="Reset options").click_exists(timeout=1)
            if click_reset_options:
                # factory_reset = option.click_factory_reset()
                factory_reset = (d(resourceId="android:id/title", text="Erase all data (factory reset)").
                                 click_exists(timeout=1))
                if factory_reset:
                    # option.enter_reset()
                    d(text="Erase all data").click_exists(timeout=1)
                    # reset = option.enter_reset()
                    reset = d(text="Erase all data").click_exists(timeout=1)
                    if reset:
                        print('设置恢复出厂设置成功')
                        return True
                    else:
                        print('设置恢复出厂设置失败')
                        return False
                else:
                    print('没有找到Erase all data (factory reset)')
            else:
                print('没有找到reset options')
                return False
        else:
            print('没有找到system')
            return False
    except Exception as e:
        print('设置恢复出厂设置失败', e)
        raise e


def main(ip):
    """
    main:主函数
    :return: True or False
    """
    d = u2.connect_usb(ip)
    open_setting(ip=ip, d=d)
    if set_display_30minutes(d=d):
        time.sleep(0.5)
        stop_setting(ip=ip, d=d)
        open_setting(ip=ip, d=d)
        if set_screen_look_NONE(d=d):
            time.sleep(0.5)
            stop_setting(ip=ip, d=d)
            open_setting(ip=ip, d=d)
            if set_stay_awake_true(d=d):
                time.sleep(0.5)
                stop_setting(ip=ip, d=d)
                open_setting(ip=ip, d=d)
                if set_connect_wifi(ip=ip, d=d):
                    time.sleep(0.5)
                    stop_setting(ip=ip,d=d)
                    open_setting(ip=ip, d=d)
                    if set_factory_reset(d=d):
                        print('设置完成，退出程序')
                        return True
                    else:
                        print('set factory reset fail')
                        return False
                else:
                    print('connect ipv4 wifi fail')
                    return False
            else:
                print('set stay awake ture fail')
                return False
        else:
            print('set screen look none fail')
            return False
    else:
        print('set display 30minutes fail')
        return False




if __name__ == '__main__':
    set_connect_wifi(ip='benq9', d=u2.connect_usb('benq9'))




















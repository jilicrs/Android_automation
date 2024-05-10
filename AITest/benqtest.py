"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/3/9 14:38
@Author    :risheng.chen@lango-tech.cn
@File      :benqtest.py
__version__ = '1.0.0'
"""
import datetime
import uiautomator2 as u2
import time
import os
import sys
import subprocess

ip = 'benq9'
d = u2.connect_usb(ip)


def WaitForDevices():
    while True:
        connect = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE,
                                   universal_newlines=True, encoding='utf-8')
        d = connect.stdout.read()

        if ip in d:
            print(d)
            time.sleep(1)
            break
        else:
            print('连接失败')
            time.sleep(3)
            continue
def BootWizard():
    while True:
        if d.xpath("//*[@text='START']").exists:
            print('执行开机向导第一步')
            d(resourceId="com.google.android.setupwizard:id/start", text='START').click_exists(timeout=10)
            time.sleep(3)
            continue
        elif d.xpath("//*[@text='Set up offline']").exists:
            print('执行开机向导第二步')
            d(text="Set up offline").click_exists(timeout=10)
            time.sleep(3)
            continue
        elif d.xpath("//*[@text='Continue']").exists:
            print('执行开机向导第三步')
            d(resourceId="android:id/button1", text='Continue').click_exists(timeout=10)
            time.sleep(3)
            continue
        elif d.xpath("//*[@text='Date & time']").exists:
            print('执行开机向导第四步')
            d(text="Next").click_exists(timeout=10)
            time.sleep(3)
            continue
        elif d.xpath("//*[@text='Accept']").exists:
            print('执行开机向导第五步')
            d(text="Accept").click_exists(timeout=10)
            time.sleep(3)
            continue
        elif d.xpath("//*[@text='Skip']").exists:
            print('执行开机向导第六步')
            d(text="Skip").click_exists(timeout=10)
            time.sleep(3)
            continue
        elif d.xpath("//*[@text='Skip anyway']").exists:
            print('执行开机向导第七步')
            d(resourceId="android:id/button1", text='Skip anyway').click_exists(timeout=10)
            time.sleep(3)
            return True
        else:
            print('开机向导异常')
            break

def FactoryReset(d=d):
    """
    set_factory_reset:恢复出厂设置
    :return:True or False
    """
    try:
        d.app_start('com.android.settings')
        time.sleep(2)
        d.swipe_ext('up')
        time.sleep(0.5)
        d.swipe_ext('up')
        # click_system = option.find_system()
        click_system = d(resourceId="android:id/title", text="System").click_exists(timeout=3)
        time.sleep(3)
        if click_system:
            d.swipe_ext('up')
            # click_reset_options = option.click_reset_options()
            click_reset_options = d(resourceId="android:id/title", text="Reset options").click_exists(timeout=3)
            time.sleep(2)
            if click_reset_options:
                # factory_reset = option.click_factory_reset()
                factory_reset = (d(resourceId="android:id/title", text="Erase all data (factory reset)").
                                 click_exists(timeout=3))
                time.sleep(2)
                if factory_reset:
                    # option.enter_reset()
                    d(text="Erase all data").click_exists(timeout=3)
                    time.sleep(2)
                    # reset = option.enter_reset()
                    reset = d(text="Erase all data").click_exists(timeout=3)
                    time.sleep(2)
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

def swipe_up(d=d):
    """
    swipe_up:上滑
    :param d:
    :return:
    """
    w, h = d.window_size()
    d.swipe(w // 2, h // 2, w // 2, h * 1 // 5)
    time.sleep(1)

def swipe_down(d=d):
    """
    swipe_down：下滑
    :param d:d
    :return:
    """
    w, h = d.window_size()
    d.swipe(w // 2, h // 2, w // 2, h * 4 // 5)
    time.sleep(1)

def find_text(d, text, swipe=True):
    """
    查找页面元素
    :param text:需要找的元素名称
    :param swipe:true
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

def set_connect_wifi(ip=ip, d=d):
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
                                    for network in range(101):
                                        WifiConnection = d.xpath('//*[@resource-id="android:id/summary"]').get_text()
                                        if 'Connected' in WifiConnection:
                                            print('-->WiFi连接成功，退出setting')
                                            d.app_clear('com.android.settings')
                                            time.sleep(1)
                                            return True
                                        elif network == 100:
                                            print('-->WiFi连接失败')
                                            time.sleep(1)
                                            return False
                                        else:
                                            sys.stdout.write('\r' + f'-->正在检测WiFi是否连接成功,计时{network}秒')
                                            sys.stdout.flush()
                                            time.sleep(1)
                                            continue
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


def LogInGoogleAccount(start=True):
    try:
        d.app_start('com.android.settings')
        time.sleep(1)
        while start:

            swipe_up(d)
            time.sleep(1)
            swipe_up(d)
            time.sleep(1)
            d(resourceId="android:id/title", text="Google").click_exists(timeout=3)
            print('进入Google')
            time.sleep(5)
            d(resourceId="com.google.android.gms:id/clp_button").click()
            print('进入登录界面')
            time.sleep(1)
            for login in range(1001):

                if d.xpath('//*[@text="Create account"]').exists:
                    time.sleep(8)
                    d.xpath('//*[@resource-id="yDmH0d"]/android.view.View[2]/'
                             'android.view.View[1]/android.view.View[1]/android.widget.TextView[2]').click()
                    print('点击输入user')
                    time.sleep(3)
                    os.system(f'adb -s {ip} shell input text feilonghong85')
                    print('输入user')
                    time.sleep(3)
                    d(text="Next").click_exists(timeout=3)
                    print('下一步')
                    for timeout in range(1001):
                        if d.xpath('//*[@resource-id="selectionc1"]').exists:
                            time.sleep(5)
                            os.system(f'adb -s {ip} shell input text hspHSPzxc123')
                            print('输入密码')
                            time.sleep(3)
                            d(text="Next").click_exists(timeout=3)
                            print('下一步')
                            time.sleep(10)
                            d(text="I agree").click()
                            print('同意')
                            time.sleep(2)
                            for loginsuccess in range(1001):
                                if d.xpath('d(text="You’re signed in")').exists:
                                    print('-->登录Google account成功')
                                    time.sleep(3)
                                    d.app_clear('com.android.settings')
                                    return True
                                elif d.xpath('//*[@text="Backup & storage"]').exists:
                                    time.sleep(1)
                                    d(text="Accept").click()
                                    print('-->登录Google account成功')
                                    time.sleep(3)
                                    d.app_clear('com.android.settings')
                                    return True
                                elif loginsuccess == 1000:
                                    print('-->登录Google account超时')
                                    time.sleep(2)
                                    return False
                                else:
                                    sys.stdout.write('\r' + f'-->正在检测Google account登录状态，计时{loginsuccess}秒')
                                    time.sleep(1)
                                    continue
                        elif timeout == 1000:
                            print(f'-->等待输入密码界面超时，计时{timeout}秒')
                            time.sleep(1)
                            return False
                        else:
                            sys.stdout.write('\r' + f'-->等待输入密码界面加载，计时{timeout}秒')
                            sys.stdout.flush()
                            time.sleep(1)
                            continue
                elif login == 1000:
                    print(f'-->输入用户名界面加载超时，计时{login}秒')
                    time.sleep(1)
                    return False
                else:
                    sys.stdout.write('\r' + f'-->等待输入用户名界面加载，计时{login}秒')
                    sys.stdout.flush()
                    time.sleep(1)
                    continue

    except Exception as LOGINERROR:
        print(f'登录Google 账号失败：{LOGINERROR}')


def MonitorTemperature():
    os.system(f'adb -s {ip} shell input keyevent 3')
    time.sleep(3)
    # weather = d.xpath('//*[@resource-id="com.google.android.googlequicksearchbox:id/title_weather_text"]').get_text()
    for i in range(1201):
        # if '°F' in weather:
        if d.xpath('//*[@resource-id="com.google.android.googlequicksearchbox:id/title_weather_text"]').exists:
            print('-->图标显示正常，正在保存截图')
            time.sleep(1)
            file = os.listdir('D:\\')
            time.sleep(1)
            if 'testreport' in file:
                os.system(f'adb -s {ip} shell screencap -p sdcard/1.png')
                time.sleep(1)
                nowtime = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
                os.system(f'adb -s {ip} pull sdcard/1.png D:\\testreport\\'
                          f'{nowtime}.png')

                return True
            else:
                os.mkdir('D:\\testreport')
                time.sleep(1)

                os.system(f'adb -s {ip} shell screencap -p sdcard/1.png')
                time.sleep(1)
                nowtime = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
                os.system(f'adb -s {ip} pull sdcard/1.png D:\\testreport\\'
                          f'{nowtime}.png')

                return True
        elif i < 1200:
            sys.stdout.write('\r' + f'-->正在检测天气图标，计时{i}秒')
            sys.stdout.flush()
            time.sleep(1)
            continue
        else:
            print('error，正在保存异常截图')
            time.sleep(1)
            file = os.listdir('D:\\')
            time.sleep(1)
            if 'testreport' in file:
                os.system(f'adb -s {ip} shell screencap -p sdcard/1.png')
                time.sleep(1)
                nowtime = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
                os.system(f'adb -s {ip} pull sdcard/1.png D:\\testreport\\'
                          f'{nowtime}_error.png')
                return False
            else:
                os.mkdir('D:\\testreport')
                time.sleep(1)

                os.system(f'adb -s {ip} shell screencap -p sdcard/1.png')
                time.sleep(1)
                nowtime = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
                os.system(f'adb -s {ip} pull sdcard/1.png D:\\testreport\\'
                          f'{nowtime}_error.png')
                return False


def main():
    start = 1
    while True:
        WaitForDevices()
        if start <= 300:
            if BootWizard():
                time.sleep(3)
                if set_connect_wifi():
                    time.sleep(10)
                    if LogInGoogleAccount():
                        time.sleep(30)
                        if MonitorTemperature():
                            time.sleep(5)
                            if FactoryReset(d=d):
                                time.sleep(1)
                                sys.stdout.write('\r' + f'测试第{start}次成功')
                                sys.stdout.flush()
                                start += 1
                                time.sleep(150)
                                continue
                            else:
                                print(f'恢复出厂设置异常，测试{start}次失败')
                                break
                        else:
                            print(f'温度异常，测试{start}次失败')
                            break
                    else:
                        print(f'登录Google account异常，测试{start}次失败')
                        break
                else:
                    print(f'连接WiFi异常，测试{start}次失败')
                    break
            else:
                print(f'开机向导异常，测试{start}次失败')
                break
        if start > 300:
            sys.stdout.write('\r' + f'测试{start - 1}次完成')
            sys.stdout.flush()
            break


if __name__ == '__main__':
    main()





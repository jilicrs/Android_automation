"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/2/20 16:41
@Author    :risheng.chen@lango-tech.cn
@File      :BootWizard.py
__version__ = '1.0.0'
"""
import time
import uiautomator2 as u2
import subprocess
from configparser import ConfigParser


config = ConfigParser()

devices = str(input('输入测试设备IP：'))

def ConfigSavePath():
    config.read('config.ini', encoding='utf-8')
    save_path = config.get(section='DATABASE', option='Screenshot_save_path')
    print(save_path)
    return save_path



class SkipBootWizardAndFactoryReset(object):
    """
    跳过开机向导与恢复出厂设置
    """


    def __init__(self, IP = devices,
                 SAVE_PATH = ConfigSavePath()):
        self.ip = IP
        self.d = u2.connect_usb(self.ip)
        self.SavePath = SAVE_PATH

    def BootWizard(self):
        """
        BootWizard:Android12 3566系列MCD开机向导
        :return:
        """
        if SkipBootWizardAndFactoryReset().WaitForDevices():
            while True:
                if self.d.xpath("//*[@text='START']").exists:
                    print('执行开机向导第一步')
                    self.d(resourceId="com.google.android.setupwizard:id/start", text='START').click_exists(timeout=10)
                    time.sleep(3)
                    continue
                elif self.d.xpath("//*[@text='Set up offline']").exists:
                    print('执行开机向导第二步')
                    self.d(text="Set up offline").click_exists(timeout=10)
                    time.sleep(3)
                    continue
                elif self.d.xpath("//*[@text='Continue']").exists:
                    print('执行开机向导第三步')
                    self.d(resourceId="android:id/button1", text='Continue').click_exists(timeout=10)
                    time.sleep(3)
                    continue
                elif self.d.xpath("//*[@text='Date & time']").exists:
                    print('执行开机向导第四步')
                    self.d(text="Next").click_exists(timeout=10)
                    time.sleep(3)
                    continue
                elif self.d.xpath("//*[@text='Accept']").exists:
                    print('执行开机向导第五步')
                    self.d(text="Accept").click_exists(timeout=10)
                    time.sleep(3)
                    continue
                elif self.d.xpath("//*[@text='Skip']").exists:
                    print('执行开机向导第六步')
                    self.d(text="Skip").click_exists(timeout=10)
                    time.sleep(3)
                    continue
                elif self.d.xpath("//*[@text='Skip anyway']").exists:
                    print('执行开机向导第七步')
                    self.d(resourceId="android:id/button1", text='Skip anyway').click_exists(timeout=10)
                    time.sleep(3)
                    return True
                else:
                    print('开机向导异常')
                    return False





    def set_factory_reset(self):
        """
        set_factory_reset:恢复出厂设置
        :return:True or False
        """
        try:
            self.d.app_start('com.android.settings')
            time.sleep(2)
            self.d.swipe_ext('up')
            time.sleep(0.5)
            self.d.swipe_ext('up')
            # click_system = option.find_system()
            click_system = self.d(resourceId="android:id/title", text="System").click_exists(timeout=3)
            time.sleep(3)
            if click_system:
                self.d.swipe_ext('up')
                # click_reset_options = option.click_reset_options()
                click_reset_options = self.d(resourceId="android:id/title", text="Reset options").click_exists(timeout=3)
                time.sleep(2)
                if click_reset_options:
                    # factory_reset = option.click_factory_reset()
                    factory_reset = (self.d(resourceId="android:id/title", text="Erase all data (factory reset)").
                                     click_exists(timeout=3))
                    time.sleep(2)
                    if factory_reset:
                        # option.enter_reset()
                        self.d(text="Erase all data").click_exists(timeout=3)
                        time.sleep(2)
                        # reset = option.enter_reset()
                        reset = self.d(text="Erase all data").click_exists(timeout=3)
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



    def PushFileForSdcard(self, PushFilePath):
        """
        PushFileForSdcard:推送本地文件到sdcard/test目录下
        :param PushFilePath:被推送文件的本地路径(=input('输入推送到sdcard/test目录下的文件路径：'))
        :return:
        """
        try:
            subprocess.Popen(f'adb -s {self.ip} shell mkdir sdcard/test', shell=True)
            time.sleep(2)
            file = subprocess.Popen(f'adb -s {self.ip} shell ls /sdcard/', shell=True,
                                    stdout=subprocess.PIPE, encoding='utf-8')
            time.sleep(1)
            output = file.stdout.readlines()
            if 'test\n' in output:
                print(f'创建成功:{output}')
                time.sleep(1)
                subprocess.Popen(f'adb -s {self.ip} push {PushFilePath} sdcard/test/')
                time.sleep(1)
                return True
            else:
                print(f'创建失败：{output}')
                return False
        except Exception as MkdirDirectoryError:
            print('创建文件夹失败：', MkdirDirectoryError)
            return False




    def WaitForDevices(self):
        """
        WaitForDevices:持续检测设备是否在线
        :return:
        """
        while True:
            connect = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE,
                                       universal_newlines=True, encoding='utf-8')
            device = connect.stdout.read()

            if self.ip in device:
                print(device)
                time.sleep(1)
                return True
            else:
                print('连接失败')
                time.sleep(3)
                continue



if __name__ == '__main__':
    SkipBootWizardAndFactoryReset().BootWizard()



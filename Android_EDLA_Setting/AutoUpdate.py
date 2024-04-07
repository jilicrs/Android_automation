"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/2/29 14:26
@Author    :risheng.chen@lango-tech.cn
@File      :AutoUpdate.py
__version__ = '1.0.0'
"""
import time
import autoit
import subprocess
import sys
from win32gui import *
from PIL import ImageGrab
import win32con
import os
import pytesseract
from PIL import Image
from configparser import ConfigParser



class RktoolsUpdateFirmware(object):
    """
    RktoolsUpdateFirmware:使用RK的工具进行升级，前提需要OPS盒子升级之前开启adb模式
    """
    config = ConfigParser()
    config.read('config.ini', encoding='utf-8')

    RKDevTool_EXE = config.get('DATABASE', 'RkUpdateTool_exe_path')
    RKDevTool_Name = config.get('DATABASE', 'RkUpdateTool_exe_name')
    Screenshot_Save_Path = config.get('DATABASE', 'Screenshot_save_path')
    Screenshot_Save_name = config.get('DATABASE', 'Screenshot_save_name')
    Firmware_Path = config.get('DATABASE', 'FirmwareUpdate_img_path')



    def __init__(self, app = autoit.run(RKDevTool_EXE),
                 app_name = RKDevTool_Name,
                 filepath = Screenshot_Save_Path,
                 save_name = Screenshot_Save_name,
                 firmware_path = Firmware_Path):
        """
        初始化
        :param app: Rkupdatetools 工具绝对路径
        :param app_name: rk升级工具名称
        :param filepath: 截图保存位置
        :param save_name:截图保存命名
        :param firmware_path: 升级固件绝对路径
        """
        self.app = app
        self.app_name = app_name
        self.screenshot_filepath = filepath
        self.screenshot_save_name = save_name
        self.firmware_path = firmware_path



    def AppStart(self, start=True):
        """
        AppStart:启动RK升级工具
        :param start:
        :return:
        """
        while start:
            app = self.app
            time.sleep(2)
            app_type = autoit.win_exists(self.app_name)
            if app_type == 1:
                print(f'app running, PID:{app}')
                break
            else:

                continue

    def MonitorBootLoader(self):
        """
        MonitorBootLoader:监听设备进入boot loader状态
        :return:
        """
        for boot in range(30):
            loader = autoit.control_get_text(title=self.app_name, control='1004')
            if loader == 'No Devices Found':
                sys.stdout.write("\r" + loader +' '+ str(boot))
                sys.stdout.flush()
                time.sleep(1)
                continue
            elif loader == 'Found One ADB Device':
                sys.stdout.write("\r" + loader +' '+ str(boot))
                sys.stdout.flush()
                time.sleep(1)
                continue
            elif loader == 'Found One LOADER Device':
                sys.stdout.write("\r" + loader +' '+ str(boot))
                sys.stdout.flush()
                time.sleep(1)
                return True
            elif boot == 20:
                sys.stdout.write("\r" + loader +' '+ str(boot))
                sys.stdout.flush()
                time.sleep(1)
                return False



    def MonitorUpdateResult(self):
        """
        MonitorUpdateResult:监听设备升级是否完成并提示找到一个adb设备
        :return:
        """
        for update in range(300):
            UpdateResult = autoit.control_get_text(title=self.app_name, control='1004')
            if 'Found One ADB Device' in UpdateResult:
                sys.stdout.write("\r" + UpdateResult +' '+ str(update))
                sys.stdout.flush()
                time.sleep(1)
                return True
            elif update < 300:
                sys.stdout.write("\r" + UpdateResult +' '+ str(update))
                sys.stdout.flush()
                time.sleep(1)
                continue
            elif update == 300:
                sys.stdout.write("\r" + UpdateResult +' '+ str(update))
                sys.stdout.flush()
                time.sleep(1)
                return True


    def SaveScreenShot(self):
        """
        SaveScreenShot:升级完成之后将RK的升级结果进行截图保存
        :return:
        """
        app_name = self.app_name
        time.sleep(1)
        # 根据窗口名称获取窗口对象
        window = FindWindow(0, app_name)
        time.sleep(2)
        # 将该窗口最大化
        ShowWindow(window, win32con.SW_MAXIMIZE)
        time.sleep(1)
        # 获取窗口坐标
        x_start, y_start, x_end, y_end = GetWindowRect(window)
        box = (x_start, y_start, x_end, y_end)
        screenshot = ImageGrab.grab(box)
        screenshot.save(self.screenshot_filepath+self.screenshot_save_name)
        time.sleep(2)
        # 将该窗口最小化
        ShowWindow(window, win32con.SW_MINIMIZE)
        file = os.listdir(self.screenshot_filepath)
        if self.screenshot_save_name in file:
            print('screenshot save pass')
            time.sleep(1)
            return True
        else:
            print(f'screenshot save fail:{file}')
            time.sleep(1)
            return False


    def ExtractTextFromImage(self):
        """
        ExtractTextFromImage:文字识别保存的RK截图中文字信息是否存在升级成功的字样
        :return:
        """
        image = Image.open(self.screenshot_filepath+self.screenshot_save_name)
        text = pytesseract.image_to_string(image)
        if 'Download Firmware Success' in text:
            print(f'pass,{text}')
            os.remove(self.screenshot_filepath+self.screenshot_save_name)
            return True
        else:
            print(f'fail,{text}')
            return False


    def RkToolsUpdate(self):
        """
        RkToolsUpdate:RK工具升级操作
        :return:
        """
        autoit.control_click(title=self.app_name, control='1011', button='left', clicks=1)
        print('打开文件列表\n')
        time.sleep(2)
        autoit.control_click(title='打开', control='1148', button='left', clicks=1)
        time.sleep(1)
        autoit.send(send_text=self.firmware_path)
        time.sleep(2)
        autoit.send("{enter down}")
        print('按下')
        autoit.send('{enter up}')
        print('抬起')
        autoit.send("{enter down}")
        print('按下')
        autoit.send('{enter up}')
        print('抬起')
        time.sleep(2)
        firmware = autoit.control_get_text(title=self.app_name, control="1017")
        print(firmware)
        if self.firmware_path == firmware:
            print('固件正确', firmware)
            time.sleep(1)
            subprocess.Popen('adb reboot loader', shell=True)
            time.sleep(1)
            return True
        else:
            print('固件选择错误', firmware)

    def ClickUpdate(self):
        """
        ClickUpdate:升级按键
        :return:
        """
        update = autoit.control_click(title=self.app_name, control='1013', button='left', clicks=1)
        return update


def AutoUpdate():
    """
    自动升级
    :return:
    """
    RktoolsUpdateFirmware().AppStart()
    if RktoolsUpdateFirmware().RkToolsUpdate():
        time.sleep(1)
        if RktoolsUpdateFirmware().MonitorBootLoader():
            print('正在升级')
            RktoolsUpdateFirmware().ClickUpdate()
            time.sleep(1)
            if RktoolsUpdateFirmware().MonitorUpdateResult():
                if RktoolsUpdateFirmware().SaveScreenShot():
                    if RktoolsUpdateFirmware().ExtractTextFromImage():
                        print('升级完成')
                        return True
                    else:
                        print('升级失败')
                        return False
                else:
                    print('error')
                    return False
            else:
                print('device error')
                return False
        else:
            print('no device')
            return False
    else:
        print('固件错误')
        return False








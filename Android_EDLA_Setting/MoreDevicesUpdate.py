"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/4/9 10:54
@Author    :risheng.chen@lango-tech.cn
@File      :MoreDevicesUpdate.py
__version__ = '1.0.0'
"""
import subprocess
import time
import autoit
from configparser import ConfigParser


class UpdateMoreDevices(object):

    config = ConfigParser()
    config.read('config.ini', encoding='utf-8')

    RkUpdateMoreDevices = config.get('DATABASE', 'RkUpdateMoreTool_exe_path')
    RkUpdateMoreDevices_name = config.get('DATABASE', 'RkUpdateMoreTool_exe_name')
    UpdateFirmware_path = config.get('DATABASE', 'FirmwareUpdate_img_path')

    print(RkUpdateMoreDevices)

    def __init__(self, UpdateTools = RkUpdateMoreDevices, UpdateTools_name = RkUpdateMoreDevices_name,
                 UpdateFirmware = UpdateFirmware_path):
        self.UpdateExe = UpdateTools
        self.UpdateExe_name = UpdateTools_name
        self.UpdateForFirmware = UpdateFirmware


    def StartUpdateTools(self, start=True) -> None:
        while start:
            exe = subprocess.Popen(self.UpdateExe, stdout=subprocess.PIPE, shell=True)
            time.sleep(2)
            exe_type = autoit.win_exists(self.UpdateExe_name)
            if exe_type == 1:
                print(f'program running:{exe}')
                break
            else:
                continue


    def ChooseFirmware(self):
        test = autoit.control_get_text(title=self.UpdateExe_name, control='1000')
        print(test)
        time.sleep(1)
        autoit.mouse_click(button='left', clicks=1, x=47, y=26)
        print('选择固件')















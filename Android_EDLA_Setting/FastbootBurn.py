"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/3/19 13:50
@Author    :risheng.chen@lango-tech.cn
@File      :FastbootBurn.py
__version__ = '1.0.0'
"""

import subprocess
import time
from configparser import ConfigParser
from Android_EDLA_Setting.BootWizard import devices


def FastbootSystemImg():
    config = ConfigParser()
    config.read('config.ini', encoding='utf-8')
    img = config.get('FASTBOOT_PATH', 'FASTBOOT_FLASH_IMG')
    return img


class Fastboot(object):


    def __init__(self, device = devices, SystemUpdate = FastbootSystemImg()):
        self.device = device
        self.fastboot_flash_img = SystemUpdate



    def FastbootBurn(self):
        """
        FastbootBurn:进入fastboot烧录固件
        :return:
        """
        subprocess.Popen(f'adb -s {self.device} shell reboot bootloader', shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
        time.sleep(5)
        unlock = subprocess.Popen(f'fastboot oem at-unlock-vboot', shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
        unlock_result = unlock.stdout.read()
        if 'OKAY' in unlock_result:
            time.sleep(2)
            reboot_fastboot = subprocess.Popen('fastboot reboot fastboot', shell=True,
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
            reboot_result = reboot_fastboot.stdout.read()
            if 'Rebooting into fastboot' in reboot_result:
                time.sleep(2)
                delete_product_a = subprocess.Popen('fastboot delete-logical-partition product_a', shell=True,
                                                   stdout=subprocess.PIPE,
                                                   stderr=subprocess.PIPE)
                delete_result = delete_product_a.stdout.read()
                if "Deleting 'product_a'" in delete_result:
                    time.sleep(2)
                    fastboot_flash = subprocess.Popen(f'fastboot flash system {self.fastboot_flash_img}', shell=True,
                                                      stdout=subprocess.PIPE,
                                                      stderr=subprocess.PIPE)
                    fastboot_flash_result = fastboot_flash.stdout.read()
                    if 'Finished.' in fastboot_flash_result:
                        print('升级成功')
                        return True
                    else:
                        print('升级失败')
                        return False
                else:
                    print('delete product_a失败')
            else:
                print('reboot fastboot失败')
        else:
            print('解锁失败')





























"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/3/16 11:14
@Author    :risheng.chen@lango-tech.cn
@File      :RunCaseTest.py
__version__ = '1.0.0'
"""
import time
import sys
from Android_EDLA_Setting.AutoUpdate import AutoUpdate
from Android_EDLA_Setting.BootWizard import SkipBootWizardAndFactoryReset
from Android_EDLA_Setting.ConnectWifi import ConnectWifiForIPV4
from Android_EDLA_Setting.SSHLinkLinux import RunStsCase
from Android_EDLA_Setting.UsbSwitch import SwitchDP
from Android_EDLA_Setting.UsbSwitch import GetSource
from Android_EDLA_Setting.UsbSwitch import ser



def RunCase():
    """
    测试主函数
    :return:
    """
    # 自动升级
    if AutoUpdate():
        for i in range(151):
            sys.stdout.write('\r' + f'等待开机:{i}' + '\r')
            time.sleep(1)
            continue
        # 跳过开机向导
        if SkipBootWizardAndFactoryReset().BootWizard():
            time.sleep(3)
            # 连接WiFi
            if ConnectWifiForIPV4().set_connect_wifi():
                time.sleep(3)
                # 切换USB OTG到Linux
                SwitchDP()
                time.sleep(2)
                if ser.is_open:
                    pass
                else:
                    ser.open()
                time.sleep(1)
                if 'F63002143C6F' == GetSource():
                    time.sleep(1)
                    # Linux跑sts case
                    if RunStsCase():
                        print('测试完成')
                        return True
                    else:
                        print('测试失败')
                        return False
                else:
                    print('切换DP异常')
            else:
                print('wifi连接失败')
                return False
        else:
            print('开机向导异常')
            return False
    else:
        print('固件升级失败')
        return False


if __name__ == '__main__':
    RunCase()






















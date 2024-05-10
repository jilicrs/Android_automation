#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/12/8 17:55
# @Author    :risheng.chen@lango-tech.com
# @File      :Burn_Google_Key .py
__version__ = '2.0.0'

import os
import time
from subprocess import Popen, PIPE, STDOUT
import datetime
from pynput.mouse import Controller, Button
from email_setting.email_setting import SendEmail


class BurnGoogleKey(object):
    def __init__(self, mouse=Controller(), x=1642, y=297, device='192.168.123.226',
                 key_65='LA0101B650000000001.keybox-9800B4910E6E8CA33986C85264F162'
                        '0249DC9C303F58DB79C51EC0FE9DA78224.factory-user.enc',
                 key_75='LA0102B750000000501.keybox-D4DCDE773BBAF5DED803E9AA34B55B'
                        '484510F648F57D0652736BF13BF85BB250.factory-user.enc'):
        self.mouse = mouse
        self.device = device
        self.x = x
        self.y = y
        self.six_key = key_65
        self.seven_key = key_75

    def MouseClickForPower(self):
        self.mouse.position = (self.x, self.y)
        self.mouse.click(Button.left, 1)
        time.sleep(5)
        self.mouse.position = (self.x, self.y)
        self.mouse.click(Button.left, 1)
        time.sleep(55)


    def connect_wifi(self):
        while True:
            connect = Popen(r'adb connect {}'.format(self.device), shell=True, stdout=PIPE, stderr=STDOUT,
                            universal_newlines=True, encoding='UTF-8')
            network = connect.stdout.read()
            if 'connected to {}'.format(self.device) in network:
                return True
            else:
                continue


    def Send_Google_Key_65(self):
        try:
            BurnGoogleKey().connect_wifi()
            os.system('adb -s {} root'.format(self.device))
            time.sleep(1)
            BurnGoogleKey().connect_wifi()
        except Exception as e:
            print('WiFi连接存在问题，重新连接WiFi测试', e)
            BurnGoogleKey().MouseClickForPower()
            raise e
        result = Popen(r'adb -s {} shell tee_provision -i /mnt/media_rw/2CEA-44C1/{} -t 0x42'.format(self.device, self.six_key),
                       shell=True,
                       stdout=PIPE,
                       stderr=STDOUT,
                       universal_newlines=True)
        Google_Key_Result = result.stdout.read()
        if '[PROVISION-CA] store key success' in Google_Key_Result:
            print('烧录65寸Google Key成功：', Google_Key_Result)
            time.sleep(2)
            BurnGoogleKey().MouseClickForPower()
            return True
        else:
            print('烧录65寸Google Key失败：', Google_Key_Result)
            time.sleep(2)
            BurnGoogleKey().MouseClickForPower()
            return False

    def Send_Google_Key_75(self):
        try:
            BurnGoogleKey().connect_wifi()
            os.system('adb -s {} root'.format(self.device))
            time.sleep(1)
            BurnGoogleKey().connect_wifi()
        except Exception as e:
            print('WiFi连接存在问题，重新连接WiFi测试', e)
            BurnGoogleKey().MouseClickForPower()
            raise e

        result = Popen(r'adb -s {}  shell tee_provision -i /mnt/media_rw/2CEA-44C1/{} -t 0x42'.format(self.device, self.seven_key),
                       shell=True,
                       stdout=PIPE,
                       stderr=STDOUT,
                       universal_newlines=True)
        Google_Key_Result = result.stdout.read()
        if '[PROVISION-CA] store key success' in Google_Key_Result:
            print('烧录75寸Google Key成功：', Google_Key_Result)
            time.sleep(2)
            BurnGoogleKey().MouseClickForPower()
            return True
        else:
            print('烧录75寸Google Key失败：', Google_Key_Result)
            time.sleep(2)
            BurnGoogleKey().MouseClickForPower()
            return False


    def Delete_Google_Key(self):
        try:
            BurnGoogleKey().connect_wifi()
            os.system('adb -s {} root'.format(self.device))
            time.sleep(1)
            BurnGoogleKey().connect_wifi()
        except Exception as e:
            print('WiFi连接存在问题，重新连接WiFi测试', e)
            BurnGoogleKey().MouseClickForPower()
            raise e

        result = Popen(r'adb -s {} shell tee_provision -d -t 0x42'.format(self.device), shell=True, stdout=PIPE, stderr=STDOUT,
                       universal_newlines=True)
        delete_result = result.stdout.read()
        if '[PROVISION-CA] delete [0x42 KEYMASTER3_KEY] success' in delete_result:
            print('google key delete success', delete_result)
            time.sleep(2)
            BurnGoogleKey().MouseClickForPower()
            return True
        else:
            print('google key delete fail', delete_result)
            time.sleep(2)
            BurnGoogleKey().MouseClickForPower()
            return True


    def Check_Google_key(self):
        try:
            BurnGoogleKey().connect_wifi()
            os.system('adb -s {} root'.format(self.device))
            time.sleep(1)
            BurnGoogleKey().connect_wifi()
        except Exception as e:
            print('WiFi连接存在问题，重新连接WiFi测试', e)
            BurnGoogleKey().MouseClickForPower()
            raise e

        result = Popen(r'adb -s {} shell tee_provision -q -t 0x42'.format(self.device), shell=True, stdout=PIPE, stderr=STDOUT,
                       universal_newlines=True)
        check_result = result.stdout.read()
        if '[PROVISION-CA] query [0x42 KEYMASTER3_KEY] not provisioned' in check_result:
            print('google key is unburned', check_result)
            time.sleep(2)
            return False
        elif '[PROVISION-CA] query [0x42 KEYMASTER3_KEY] provisioned in RPMB, length = 8610 bytes.' in check_result:
            print('google key is burn', check_result)
            time.sleep(2)
            return True
        else:
            time.sleep(2)
            print('Chick fail', check_result)
            pass


if __name__ == '__main__':
    start_test = 1
    fail_count = 0
    burn_key_error = 0
    delete_key_error = 0
    check_key_error = 0
    success_count = 0
    end_test = 100
    while True:
        if start_test <= end_test:
            if BurnGoogleKey().Delete_Google_Key():
                if not BurnGoogleKey().Check_Google_key():
                    if start_test % 2 == 0:
                        if BurnGoogleKey().Send_Google_Key_65():
                            if BurnGoogleKey().Check_Google_key():
                                print('*{}第{}次测试通过'.format(datetime.datetime.now().
                                                                 strftime('%Y/%m/%d_%H:%M:%S:'),
                                                                 start_test))
                                start_test += 1
                                success_count += 1
                                continue
                            else:
                                print('*{}第{}次测试失败，烧录异常'.format(datetime.datetime.now().
                                                                          strftime('%Y/%m/%d_%H:%M:%S:'),
                                                                          start_test))
                                start_test += 1
                                fail_count += 1
                                burn_key_error += 1
                                continue
                        else:
                            print('*{}第{}次测试失败，烧录异常'.format(datetime.datetime.now().
                                                                      strftime('%Y/%m/%d_%H:%M:%S:'),
                                                                      start_test))
                            start_test += 1
                            fail_count += 1
                            burn_key_error += 1
                            continue
                    elif start_test % 2 != 0:
                        if BurnGoogleKey().Send_Google_Key_75():
                            if BurnGoogleKey().Check_Google_key():
                                print('*{}第{}次测试通过'.format(datetime.datetime.now().
                                                                 strftime('%Y/%m/%d_%H:%M:%S:'),
                                                                 start_test))
                                start_test += 1
                                success_count += 1
                                continue
                            else:
                                print('*{}第{}次测试失败，烧录异常'.format(datetime.datetime.now().
                                                                          strftime('%Y/%m/%d_%H:%M:%S:'),
                                                                          start_test))
                                start_test += 1
                                fail_count += 1
                                burn_key_error += 1
                                continue
                        else:
                            print('*{}第{}次测试失败，烧录异常'.format(datetime.datetime.now().
                                                                      strftime('%Y/%m/%d_%H:%M:%S:'),
                                                                      start_test))
                            start_test += 1
                            fail_count += 1
                            burn_key_error += 1
                            continue
                else:
                    print('*{}第{}次测试失败，删除异常'.format(datetime.datetime.now().
                                                              strftime('%Y/%m/%d_%H:%M:%S:'),
                                                              start_test))
                    start_test += 1
                    fail_count += 1
                    delete_key_error += 1
                    continue
        elif start_test > end_test:
            text = ('311D2.S Google Key自动烧录测试：\n'+'               '+
                    '{}测试{}次完成，测试通过{}次，失败{}次，烧录失败{}次，删除失败{}次'.
                  format(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S:'), end_test,
                         success_count, fail_count, burn_key_error, delete_key_error))
            print(text)
            SendEmail().send_email(contents=text, to_address=('risheng.chen@lango-tech.cn',
                                                              'fangwei.chen@lango-tech.cn',
                                                              ))
            break



















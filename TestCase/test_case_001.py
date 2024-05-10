#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/7/18 9:05
# @Author    :risheng.chen@lango-tech.com
# @File      :test_case_001.py
# coding     :utf-8
__version__ = '1.0.0'

from BasePage.DeviceConnect import DeviceConnect
from BasePage.globals import BasePage
from Logger.getlogger import Logging
from screenshot.screenshot import GetScreen
import pytest
import os
import allure
import time
import datetime


@allure.epic('公版setting')
class TestCase(object):

    def __init__(self, d = DeviceConnect().ConnectDeviceForWifi(), logger = Logging().getloger(),
                 down_log = BasePage().GetErrorLog(), basepage = BasePage(),
                 Now_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')):
        self.d = d
        self.logger = logger
        self.down_log = down_log
        self.basepage = basepage
        self.Now_time = Now_time

    def setup_class(self):
        try:
            with allure.step('start setting app'):
                print('test start:{}'.format(self.basepage.now_time()))
                self.basepage.app_start(packages_name='com.xbh.jyjsetting')
                time.sleep(3)
        except Exception as e:
            print('start setting error', e)
            os.system(self.down_log)
            raise e
        pid = self.basepage.app_wait(packages_name='com.xbh.jyjsetting')
        if not pid:
            print('com.xbh.jyjsetting is not running')
        else:
            print('{packages} is {package}'.format(packages=self.d.info['currentPackageName'], package=pid))
            self.logger.info('%s start app success' % str(self.Now_time))
        self.d.app_wait('com.xbh.jyjsetting', front=True)
        # 等待应用启动，默认20S
        self.d.app_wait('com.xbh.jyjsetting', timeout=20)
        self.d.implicitly_wait(10)

    def teardown_class(self):
        try:
            with allure.step('stop and clear setting app'):
                self.basepage.app_stop(packages_name='com.xbh.jyjsetting')
                time.sleep(1)
                self.d.app_clear("com.xbh.jyjsetting")
                print('test finish:{}'.format(self.basepage.now_time()))
        except Exception as e:
            print('app stop error', e)
            raise e

    @pytest.mark.P1
    @allure.title("切换主题")
    @allure.story('一、切换系统主题功能验证')
    @allure.severity("blocker")
    def test_01(self):
        """
        test_01:setting-通用-个性化替换主题功能验证
        """
        with allure.step('1.验证setting替换主题功能'):
            try:
                with allure.step('1.选择通用--个性化'):
                    self.d(resourceId="com.xbh.jyjsetting:id/setting_tv", text="通用").click()
                    time.sleep(2)
                    assert '个性化', self.d(text='个性化').get_text()
                    print('case1-1:Choose universal -- personal is success')
                    self.logger.info('case1-1:%s: Choose universal -- personal is success' % str(self.Now_time))
                    time.sleep(2)
                    GetScreen().screenshot()
            except Exception as e:
                print('case1-1:%s:Choose universal -- personal error' % str(self.Now_time), e)
                self.logger.info('case1-1:%s:Choose universal -- personal error' % str(self.Now_time), e)
            try:
                with allure.step('2.选择第三个模板并应用'):
                    self.d.xpath('//*[@resource-id="com.xbh.jyjsetting:id/rv_theme"]/android.widget.FrameLayout[3]').click()
                    time.sleep(1)
                    assert '确认应用主题？', self.d(text='确认应用主题？').get_text()
                    self.d(resourceId="com.xbh.jyjsetting:id/bt2Right").click()
                    print('case1-2:Select the third template and apply it is success')
                    self.logger.info('case1-2:%s:Select the third template and apply it is success' % str(self.Now_time), e)
                    time.sleep(4)
                    GetScreen().screenshot()
            except Exception as e:
                print('case1-2:%s:Select the third template and apply it is error' % str(self.Now_time), e)
                self.logger.info('case1-2:%s:Select the third template and apply it is error' % str(self.Now_time), e)


if __name__ == '__main__':
    pytest.main(['-s', '-q', "test_case_001.py", '--alluredir', './temp/'])
    os.system('allure generate ./temp/ -o ./report/ --clean')












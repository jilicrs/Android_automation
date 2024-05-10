#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/7/23 11:43
# @Author    :risheng.chen@lango-tech.com
# @File      :screenshot.py
__version__ = '1.0.0'

from BasePage.globals import DeviceConnect
from Logger.getlogger import Logging
import os
import allure
import datetime


class GetScreen(object):
    def __init__(self, NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S'),
                 logger = Logging().getloger()):
        self.NowTime = NowTime
        self.logger = logger


    def screenshot(self):
        """
        截图并附加到测试报告中
        :return:
        """
        picture_file = os.path.join(os.getcwd(), 'tmp_picture.png')
        try:
            # 截图
            DeviceConnect().ConnectDeviceForWifi().d.screenshot(picture_file)
            # 将生成的截图附加到测试报告中，这里一定文件读取方式一定要为 rb
            # 否则会造成测试报告中图片无法打开的错误
            allure.attach(open(picture_file, 'rb').read(),
                          'Fail Screenshot',
                          attachment_type=allure.attachment_type.PNG)
            self.logger.info('\n%s:Screenshot success' % self.NowTime)
            os.remove(picture_file)
        except Exception as e:
            self.logger.exception('\n%s:Screenshot fail' % self.NowTime)
            raise e

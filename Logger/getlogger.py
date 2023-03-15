#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/7/22 11:53
# @Author    :risheng.chen@lango-tech.com
# @File      :getlogger.py
__version__ = '1.0.0'

import os
import os.path
import socket
import logging
import logging.handlers
import datetime

NowTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
logging.basicConfig()


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class Logging(object):
    logger = logging.getLogger()

    def __init__(self):
        host_name = socket.gethostname()
        # ip = socket.gethostbyname(host_name)
        logging_msg_format = '[%(asctime)s] [%(levelname)s] ' \
                             '[' + host_name + '][%(module)s.py - line:%(lineno)d] %(message)s'
        logging_date_format = '%Y-%m-%d %H:%M:%S'
        log_path = 'D:\\Android automation\\TestCase\\logger'  # 日志存放目录
        logging.basicConfig(level=logging.INFO, format=logging_msg_format, datefmt=logging_date_format)
        self.logger.setLevel(logging.INFO)

        if not os.path.exists(log_path):
            os.mkdir(log_path)
        log_file = os.path.join(log_path, 'Test%s.log' % NowTime)

        fileHandler = logging.handlers.TimedRotatingFileHandler(log_file, 'midnight', 1)
        fileHandler.setFormatter(logging.Formatter(logging_msg_format))
        self.logger.addHandler(fileHandler)

    def getloger(self):
        return self.logger

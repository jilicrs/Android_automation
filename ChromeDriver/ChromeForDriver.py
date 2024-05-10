"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2023/12/13 15:26
@Author    :risheng.chen@lango-tech.cn
@File      :ChromeForDriver.py
__version__ = '1.0.0'
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



class ChromeTest(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def WebSearch(self):
        self.driver.get(url='http://www.baidu.com')
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '[id="kw"]').send_keys('自动测试')
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '[id="su"]').click()
        time.sleep(10)
        return True



def main():
    ChromeTest().WebSearch()


if __name__ == '__main__':
    main()


















"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/3/12 16:49
@Author    :risheng.chen@lango-tech.cn
@File      :TextQualifier.py
__version__ = '1.0.0'
"""

import time
import numpy as np
import pyautogui
import cv2
import pytesseract

time.sleep(3)
screen_width, screen_height = pyautogui.size()


screenshot = pyautogui.screenshot()

image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


ret, binary_image = cv2.threshold(gray_image, 127,255, cv2.THRESH_BINARY)

text = pytesseract.image_to_string(binary_image, lang='eng')

text_position = pyautogui.locateAllOnScreen(text)

print(text)






































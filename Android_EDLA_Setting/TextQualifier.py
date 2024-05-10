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
# 获取屏幕尺寸
screen_width, screen_height = pyautogui.size()

# 截取整个屏幕图像
screenshot = pyautogui.screenshot()

# 将截图转换成opencv图像格式
image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# 转换成灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 二值化处理
ret, binary_image = cv2.threshold(gray_image, 127,255, cv2.THRESH_BINARY)

# 文字识别
text = pytesseract.image_to_string(binary_image, lang='eng')

# 获取文字在屏幕上的位置
text_position = pyautogui.locateAllOnScreen(text)

print(text)
print('位置：', type(text_position))





































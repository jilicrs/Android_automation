"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2023/12/14 9:15
@Author    :risheng.chen@lango-tech.cn
@File      :video.py
__version__ = '1.0.0'
"""

import os
import ffmpeg

input_file = 'D:\\logs\\1702317603545.avi'
output_file = 'D:\\logs\\123.mp4'


try :
    if not os.path.exists(input_file):
        print('找不到文件')
        raise FileNotFoundError
    else:
        print("pass")
        stream = ffmpeg.input(input_file)
        stream1 = ffmpeg.output(stream, output_file)
        ffmpeg.run(stream1)

except FileNotFoundError as e:
    print('111找不到文件', e)







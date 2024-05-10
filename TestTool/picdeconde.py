#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/4/20 17:42
# @Author    :risheng.chen@lango-tech.com
# @File      :picdeconde.py
__version__ = '1.0.0'

import base64

PngPath = 'D:\\Android automation\\TestTool\\LoginPic.png'


def transform(picture_name):
    # 将图片转换问base64码
    open_pic = open("%s" % picture_name, 'rb')
    b64str = base64.b64encode(open_pic.read())
    open_pic.close()
    # 注意这边b64str一定要加上.decode()
    write_data = 'img = "%s"' % b64str.decode()
    f = open('%s.py' % picture_name.replace('.', '_'), 'w+')
    f.write(write_data)
    f.close()


if __name__ == '__main__':
    pics = [PngPath]
    for i in pics:
        transform(i)
    print("ok")

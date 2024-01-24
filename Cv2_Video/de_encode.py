"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/1/23 19:59
@Author    :risheng.chen@lango-tech.cn
@File      :de_encode.py
__version__ = '1.0.0'
"""

import base64

path = ''


def transform(picture_name):
    open_pic = open("%s" % picture_name, 'rb')
    b64str = base64.b64encode(open_pic.read())
    open_pic.close()
    write_data = 'img = "%s"' % b64str.decode()
    f = open('%s.py' % picture_name.replace('.', '_'), 'w+')
    f.write(write_data)
    f.close()


if __name__ == '__main__':
    pics = [path]
    for i in pics:
        transform(i)
    print("ok")
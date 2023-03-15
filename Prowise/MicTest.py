#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/11/26 18:58
# @Author    :risheng.chen@lango-tech.com
# @File      :MicTest.py
__version__ = '1.0.0'

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


windows = tk.Tk()
windows.title('测试工具')
windows.geometry('800x600')


def com():
    try:
        float(e1.get())  # 获取e1的值，转为浮点数，如果不能转捕获异常
        l1.config(text=e1.get())
    except Exception as e:
        messagebox.showwarning('警告', '请输入数字')
        print(e)


e1 = Entry(windows)
e1.pack()
Button(windows, text='获取', command=com).pack()
l1 = Label(windows, text='只能数字')
l1.pack()

windows.mainloop()




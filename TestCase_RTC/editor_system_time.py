"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2023/11/23 8:54
@Author    :risheng.chen@lango-tech.cn
@File      :editor_system_time.py
__version__ = '1.0.0'
"""

import os
from open_cussdk import ip
from open_cussdk import isCorrectIp
import time

device = '202311211511'


def year_revise():
    """
    year_revise:设置月份并自动校正
    :return:
    """
    while True:
        try:
            year = (input('输入设置的年份：'))
            if year.isalpha():
                raise TypeError
            elif len(year) < 4:
                print('年份错误，请重新输入4位数！')
                continue
            elif len(year) >= 5:
                print('年份错误，请重新输入4位数！')
                continue
            elif len(year) == 4:
                year_int = int(year)
                if year_int == 0:
                    print('年份错误，请重新输入4位数！')
                    continue
                else:
                    year_str = str(year_int)
                    if len(year_str) < 4:
                        print('年份错误，请重新输入4位数！')
                        continue
                    else:
                        print(year_str)
                        return year_str
            else:
                print(year)
                return year
        except TypeError:
            print('格式错误')



def month_revise():
    """
    month_revise:设置月份并自动校正
    :return:
    """
    while True:
        try:
            month = (input('输入设置的月份：'))
            if month.isalpha():
                raise TypeError
            elif 2 > len(month):
                str1 = str(month)
                str2 = str(0)
                months_str = str2 + str1
                months_int = int(months_str)
                if months_int == 0:
                    print('请输入正确的月份')
                    continue
                elif 0 < months_int <= 12:
                    month_revises = str(months_int)
                    if 2 > len(month_revises):
                        str3 = str(month_revises)
                        str4 = str(0)
                        month_revises_str = str4 + str3
                        print(month_revises_str)
                        return month_revises_str
                    else:
                        print(month_revises)
                        return month_revises
            elif len(month) >= 2:
                int_month = int(month)
                if int_month == 0:
                    print('请输入正确的月份')
                    continue
                elif int_month <= 12:
                    int_month_str = str(int_month)
                    if len(int_month_str) < 2:
                        str_month = str(int_month_str)
                        str_math = str(0)
                        month_str = str_math + str_month
                        print(month_str)
                        return month_str
                    else:
                        print(int_month_str)
                        return int_month_str
                elif int_month > 12:
                    print('月份不可以大于12月')
                    continue
            else:
                print(month)
                return month
        except TypeError:
            print('格式错误')




def date_revise():
    """
    date_revise:设置日期并自动校正
    :return:
    """
    while True:
        try:
            date = (input('输入设置的日期：'))
            if date.isalpha():
                raise TypeError
            elif 2 > len(date):
                str1 = str(date)
                str2 = str(0)
                date_str = str2 + str1
                date_int = int(date_str)
                if date_int == 0:
                    print('请输入正确的日期')
                    continue
                elif 0 < date_int <= 31:
                    date_revises = str(date_int)
                    if 2 > len(date_revises):
                        str3 = str(date_revises)
                        str4 = str(0)
                        date_revises_str = str4 + str3
                        print(date_revises_str)
                        return date_revises_str
                    else:
                        print(date_revises)
                        return date_revises
            elif len(date) >= 2:
                int_date = int(date)
                if int_date == 0:
                    print('请输入正确的日期')
                    continue
                elif int_date <= 31:
                    int_date_1 = str(int_date)
                    if len(int_date_1) < 2:
                        int_date_str = int_date_1
                        int_date_str1 = str(0)
                        date_str_1 = int_date_str1 + int_date_str
                        print(date_str_1)
                        return date_str_1
                    else:
                        print(int_date)
                        return int_date
                elif int_date > 31:
                    print('日期不可以大于31')
                    continue
            else:
                print(date)
                return date
        except TypeError:
            print('格式错误')




def hour_revise():
    """
    hour_revise:设置小时并自动校正
    :return:
    """
    while True:
        try:
            hour = (input('输入设置的小时：'))
            if hour.isalpha():
                raise TypeError
            elif 2 > len(hour):
                str1 = str(hour)
                str2 = str(0)
                hour_str = str2 + str1
                hour_int = int(hour_str)
                if hour_int == 0:
                    strs = str(hour_int)
                    strs_1 = str(0)
                    hour_strs = strs_1 + strs
                    print(hour_strs)
                    return hour_strs
                elif 0 < hour_int <= 24:
                    hour_revises = str(hour_int)
                    if 2 > len(hour_revises):
                        str3 = str(hour_revises)
                        str4 = str(0)
                        hour_revises_str = str4 + str3
                        print(hour_revises_str)
                        return hour_revises_str
                    else:
                        print(hour_revises)
                        return hour_revises
            elif len(hour) >= 2:
                int_hour = int(hour)
                if int_hour == 0:
                    str11 = str(int_hour)
                    str22 = str(0)
                    hour_str_1 = str11 + str22
                    print(hour_str_1)
                    return hour_str_1
                elif int_hour <= 23:
                    hour_str_2 = str(int_hour)
                    if 2 > len(hour_str_2):
                        str33 = str(hour_str_2)
                        str44 = str(0)
                        hour_str_11 = str44 + str33
                        print(hour_str_11)
                        return hour_str_11
                    else:
                        print(hour_str_2)
                        return hour_str_2
                elif int_hour > 23:
                    print('小时不可以大于24')
                    continue
            else:
                print(hour)
                return hour
        except TypeError:
            print('格式错误')



def minute_revise():
    """
    minute_revise：设置分钟并自动校正
    :return:
    """
    while True:
        try:
            minute = (input('输入设置的分钟：'))
            if minute.isalpha():
                raise TypeError
            elif 2 > len(minute):
                str1 = str(minute)
                str2 = str(0)
                hour_str = str2 + str1
                hour_int = int(hour_str)
                if hour_int == 0:
                    strs = str(hour_int)
                    strs_1 = str(0)
                    hour_strs = strs_1 + strs
                    print(hour_strs)
                    return hour_strs
                elif 0 < hour_int <= 59:
                    hour_revises = str(hour_int)
                    if 2 > len(hour_revises):
                        str3 = str(hour_revises)
                        str4 = str(0)
                        hour_revises_str = str4 + str3
                        print(hour_revises_str)
                        return hour_revises_str
                    else:
                        print(hour_revises)
                        return hour_revises
            elif len(minute) >= 2:
                int_hour = int(minute)
                if int_hour == 0:
                    str11 = str(int_hour)
                    str22 = str(0)
                    hour_str_1 = str11 + str22
                    print(hour_str_1)
                    return hour_str_1
                elif int_hour <= 59:
                    hour_str_2 = str(int_hour)
                    if 2 > len(hour_str_2):
                        str33 = str(hour_str_2)
                        str44 = str(0)
                        hour_str_11 = str44 + str33
                        print(hour_str_11)
                        return hour_str_11
                    else:
                        print(hour_str_2)
                        return hour_str_2
                elif int_hour > 59:
                    print('分钟不可以大于60')
                    continue
            else:
                print(minute)
                return minute
        except TypeError:
            print('格式错误')



def second_revise():
    """
    second_revise:设置秒钟并自动校正
    :return:
    """
    while True:
        try:
            second = (input('输入设置的秒钟：'))
            if second.isalpha():
                raise TypeError
            elif 2 > len(second):
                str1 = str(second)
                str2 = str(0)
                hour_str = str2 + str1
                hour_int = int(hour_str)
                if hour_int == 0:
                    strs = str(hour_int)
                    strs_1 = str(0)
                    hour_strs = strs_1 + strs
                    print(hour_strs)
                    return hour_strs
                elif 0 < hour_int <= 59:
                    hour_revises = str(hour_int)
                    if 2 > len(hour_revises):
                        str3 = str(hour_revises)
                        str4 = str(0)
                        hour_revises_str = str4 + str3
                        print(hour_revises_str)
                        return hour_revises_str
                    else:
                        print(hour_revises)
                        return hour_revises
            elif len(second) >= 2:
                int_hour = int(second)
                if int_hour == 0:
                    str11 = str(int_hour)
                    str22 = str(0)
                    hour_str_1 = str11 + str22
                    print(hour_str_1)
                    return hour_str_1
                elif int_hour <= 59:
                    hour_str_2 = str(int_hour)
                    if 2 > len(hour_str_2):
                        str33 = str(hour_str_2)
                        str44 = str(0)
                        hour_str_11 = str44 + str33
                        print(hour_str_11)
                        return hour_str_11
                    else:
                        print(hour_str_2)
                        return hour_str_2
                elif int_hour > 59:
                    print('秒钟不可以大于60')
                    continue
            else:
                print(second)
                return second
        except TypeError:
            print('格式错误')



def editor_system_time(editor_time='{M}{D}{h}{m}{Y}.{s}'.format(M=month_revise(),
                        D=date_revise(), h=hour_revise(), m=minute_revise(), Y=year_revise(),
                        s=second_revise())):
    """
    editor_system_time:修改系统时间接口
    args: "MMDDhhmmYYYY.ss"  # MM-月，DD-日，hh-小时，mm-分钟，YYYY年，ss-秒
    :return: time
    """
    time.sleep(1)
    os.system('adb -s {} root'.format(device))
    if isCorrectIp():
        os.system('adb connect {}'.format(device))
    else:
        pass
    time.sleep(2)
    set_time = os.popen('adb -s {} shell date {} set'.format(device, editor_time)).read()
    if 'date: cannot set date' in set_time:
        print('set {} system time error'.format(set_time))
        return False
    elif 'date: bad date' in set_time:
        print('set {} system time error'.format(set_time))
        return False
    else:
        print('set {} system time success'.format(set_time))
        return set_time


if __name__ == '__main__':
   year_revise()



























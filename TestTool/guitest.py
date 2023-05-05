#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/12/29 16:40
# @Author    :risheng.chen@lango-tech.com
# @File      :guitest.py
__version__ = '1.0.0'

import datetime
import os
import time
from TestTool.guitestpage import ComPort
import PySimpleGUI as pg
import base64
from TestTool.LoginPic_png import img as pic
from TestTool.guitestpage import adb_connect_ip
from TestTool.guitestpage import check_adb_status
from TestTool.guitestpage import ExitSystem, Send, TestManageSystem, Getport, \
    User, PassWord, Login, Cancel, open_comport, open_down, adb_connect, choose_instruct


class ToolsPage(object):
    def __init__(self):
        self.Getport = Getport
        self.open_comport = open_comport
        self.cols_comport = open_down
        self.ExitSystem = ExitSystem
        self.Send = Send
        self.TestManageSystem = TestManageSystem
        self.User = User
        self.PassWord = PassWord
        self.Login = Login
        self.Cancel = Cancel
        self.ADB_Connect = adb_connect
        self.choose_instruct = choose_instruct
        self.comport = ComPort()

    def get_port(self):
        get_serial_comport = self.comport.get_serial_comport()
        return get_serial_comport

    def open_port(self):
        open_serial_comport = self.comport.open_serial_comport()
        return open_serial_comport

    def close_port(self):
        close_serial_port = self.comport.close_serial_comport()
        return close_serial_port

    def serial_send_hex(self):
        send_hex = self.comport.serial_sent_hex(command=values["_SERIAL_"])
        return send_hex


# 编码图片/登录
tmp = open('login_pic.png', 'wb')
tmp.write(base64.b64decode(pic))
tmp.close()


# Dark Blue 3
# Default 1
pg.change_look_and_feel('Default 1')

# justification='right'
status = [('\u2B24' + ' Disconnect', 'red'), ('\u2B24' + ' Connect', 'green')]
state = 0

status1 = [('\u2B24' + ' Disconnect', 'red'), ('\u2b24' + ' Connect', 'green')]
state1 = 0

# 打开串口****************************
open_up = pg.Button(ToolsPage().open_comport, font=('宋体', 10), size=(10, 1), key="_COMPORT_", border_width=3,
                    mouseover_colors='green', pad=(2, 6))

# 关闭串口****************************
cols_comport = pg.Button(ToolsPage().cols_comport, font=('宋体', 10), size=(10, 1), key="_COMPORT_COLS_",
                         border_width=3, mouseover_colors='red', pad=(2, 6))

# 串口指示灯******************************
Status = pg.Text(text=status[state][0], text_color=status[state][1], size=(12, 1),
                 font=("Courier New", 8), key='INDICATOR')

# adb指示灯******************************
Status1 = pg.Text(text=status1[state1][0], text_color=status1[state1][1], size=(12, 1),
                  font=("Courier New", 8), key='INDICATOR1')

# 发送*******************************
bt = pg.Button(ToolsPage().Send, font=('宋体', 10), size=(10, 1), key="_SEND_", border_width=3,
               mouseover_colors='yellow')

# 退出*******************************
cbt = pg.Button(ToolsPage().ExitSystem, font=('宋体', 10), size=(10, 1), button_color=('red', 'white'),
                key='_EXIT_', border_width=3, mouseover_colors='red')

# 调试设置=================================================================================================
config = [
    # 端口号
    [pg.Button(ToolsPage().Getport, font=('宋体', 10), size=(10, 1), key='_GET_COMPORT_',
               border_width=3, pad=(2, 6)),
     pg.InputText(disabled=True, font=('楷体', 10), size=(8, 1), key='_SHOW_COMPORT_', border_width=3)],
    [open_up, Status],
    [cols_comport],
    # adbIP输入框
    [pg.Text(text='输入IP地址：', font=('宋体', 10), size=(6, 1), key='_ADB_IP_', border_width=3,
             pad=(2, 6), relief='ridge'),
     pg.InputText("", key='_ADB_IP_INPUT_', font=('楷体', 10), size=(14, 1), border_width=3)],
    # adb连接
    [pg.Button(ToolsPage().ADB_Connect, font=('宋体', 10), size=(10, 1), key='_ADB_CONNECT_',
               border_width=3, pad=(2, 6)),
     pg.Text(text=status1[state1][0], text_color=status1[state1][1], size=(12, 1),
             font=("Courier New", 8), key='INDICATOR1')],
    [pg.Text(text=ToolsPage().choose_instruct, size=(20, 1), font=("宋体", 10), relief='ridge', pad=(2, 6))],
    [pg.Combo(['Rs232：Power_Off', 'Rs232：Power_On', 'ADB:重启整机'],
              size=(10, 1), font=("宋体", 10),
              default_value=None, key="_SERIAL_",
              background_color='', readonly=True)]
]

# 发送-退出===================================================================================================
send = [[bt, cbt]]

# 登录layout=================================================================================================
layout1 = [
    [pg.Image(size=(350, 50), filename=r'login_pic.png')],
    [pg.Text(ToolsPage().User, font=('宋体', 10), justification='left', relief='raised'),
     pg.InputText("", key='_USER_')],
    [pg.Text(ToolsPage().PassWord, font=('宋体', 10), justification='left', relief='raised'),
     pg.InputText("", password_char='*', enable_events=True, key='_PASSWORD_')],
    [pg.Button(ToolsPage().Login, size=(10, 1), key="_LOGIN_", disabled=False, border_width=3),
     pg.Button(ToolsPage().Cancel, size=(10, 1), key="_CANCEL_", border_width=3)]
]

# 主layout====================================================================================================
layout = [
    [pg.Frame('config', layout=config, pad=(10, 20), title_color='blue', title_location='n', size=(200, 350),
              border_width=5, tooltip=None),
     pg.Multiline("", size=(300, 26), key="_OUTPUT_", disabled=True, font=('楷体', 10), tooltip=None,
                  border_width=2)],
    [pg.Frame('send or exit', layout=send, pad=(10, 20), title_color='blue', title_location='n',
              element_justification='center', vertical_alignment='bottom', expand_x=True, border_width=5,
              tooltip=None)]
]

# element_justification='center' 居中,登录layout标题栏=======================================================
TitleLayout = [
    [pg.Frame(ToolsPage().TestManageSystem, layout=layout1, pad=(10, 10),
              title_location='n', element_justification='center')]
]

# no_titlebar=True 去掉标题栏，创建窗口==========================================================================
LoginWindow = pg.Window('LOGIN TEST SYSTEM', TitleLayout, size=(400, 190), no_titlebar=True,
                        grab_anywhere=True)
window = pg.Window(ToolsPage().TestManageSystem, layout, size=(800, 500))

# 主函数=====================================================================================================
if __name__ == '__main__':
    while True:
        event2, values2 = LoginWindow.read()
        if event2 in (None, "_CANCEL_") or pg.WINDOW_CLOSED:
            break
        elif event2 in "_LOGIN_":
            print(values2)
            if values2["_USER_"] == 'admin' and values2["_PASSWORD_"] == '123456':
                # 退出窗口并删除图片文件
                os.remove('login_pic.png')
                LoginWindow.close()
                while True:
                    event, values = window.read()
                    if event == pg.WINDOW_CLOSED:
                        break
                    elif event in "_EXIT_":
                        ExitProject = pg.popup_yes_no('是否退出程序？', title='warning ')
                        if ExitProject == 'Yes':
                            break
                        else:
                            continue
                    if event in "_GET_COMPORT_":
                        window['_SHOW_COMPORT_'].update(ToolsPage().get_port())
                    if event in "_ADB_CONNECT_":
                        adb_connect_ip(values['_ADB_IP_INPUT_'])
                        if not check_adb_status(values['_ADB_IP_INPUT_']):
                            state1 = 0
                            window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                      '连接超时：请输入IP或检查IP是否正确!')
                        else:
                            # 判断adb是否正常连接
                            if check_adb_status(values["_ADB_IP_INPUT_"]):
                                state1 = 1
                                adb_value, adb_text_color = status1[state1]
                                window['INDICATOR1'].update(value=adb_value, text_color=adb_text_color)
                                time.sleep(0.5)
                                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                          "connect to {} success".format(values['_ADB_IP_INPUT_']))
                            elif not check_adb_status(values["_ADB_IP_INPUT_"]):
                                state1 = 0
                                adb_value, adb_text_color = status1[state1]
                                window['INDICATOR1'].update(value=adb_value, text_color=adb_text_color)
                                time.sleep(0.5)
                                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                          "connect to {} fail".format(values['_ADB_IP_INPUT_']))

                    # ++++++++++++++++++++++++++++++++________________________-------------------------
                    if event in "_COMPORT_":
                        try:
                            if ToolsPage().open_port():
                                if ToolsPage().open_port().isOpen():
                                    state = 1
                                    serial_value, serial_text_color = status[state]
                                    print(state)
                                    window['INDICATOR'].update(value=serial_value, text_color=serial_text_color)
                                    window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                              '串口打开成功!')
                                else:
                                    state = 0
                                    serial_value, serial_text_color = status[state]
                                    print(state)
                                    window['INDICATOR'].update(value=serial_value, text_color=serial_text_color)
                                    window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                              '串口连接异常，请检查串口是否连接或被其他程序占用！')
                            elif not ToolsPage().open_port():
                                state = 0
                                serial_value, serial_text_color = status[state]
                                window['INDICATOR'].update(value=serial_value, text_color=serial_text_color)
                                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                          '串口打开失败！')
                            else:
                                raise KeyError('Serial port exception')
                        except:
                            window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                      '串口连接异常，请检查串口是否连接或被其他程序占用！')
                            continue
                    elif event in "_COMPORT_COLS_":
                        try:
                            if ToolsPage().open_port().isOpen():
                                ToolsPage().close_port()
                                state = 0
                                serial_value, serial_text_color = status[state]
                                window['INDICATOR'].update(value=serial_value, text_color=serial_text_color)
                                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                          '串口关闭成功')
                            elif state == 1:
                                state = 1
                                serial_value, serial_text_color = status[state]
                                print("Serial port not turned off", state)
                                window['INDICATOR'].update(value=serial_value, text_color=serial_text_color)
                                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                          '串口未关闭')
                            else:
                                raise KeyError('Serial port exception')
                        except:
                            window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                      '串口未打开，不用关闭串口')
                            continue
                    if event in "_SEND_":
                        try:
                            if values["_SERIAL_"] == 'Rs232：Power_On':
                                if state == 0:
                                    EP = pg.popup_ok('Serial port not enabled！！', title='warning ')
                                    if EP == 'Ok':
                                        break
                                else:
                                    ToolsPage().serial_send_hex()
                                    name = values["_SERIAL_"]
                                    window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:')
                                                              + name)
                            else:
                                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                          '发送失败！')
                                raise KeyError('The value must be byte data')
                        except KeyError as e:
                            print("Serial throw an exception：", repr(e))
                        try:
                            if values["_SERIAL_"] == 'Rs232：Power_Off':
                                if state == 0:
                                    EP = pg.popup_ok('Serial port not enabled！！', title='warning ')
                                    if EP == 'Ok':
                                        break
                                else:
                                    ToolsPage().serial_send_hex()
                                    name = values["_SERIAL_"]
                                    window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:')
                                                              + name)
                            else:
                                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                          '发送失败！')
                                raise KeyError('The value must be byte data')
                        except KeyError as e:
                            print("Serial throw an exception：", repr(e))
                        try:
                            if values["_SERIAL_"] == 'ADB:重启整机':
                                if state1 == 1:
                                    os.system('adb reboot')
                                    time.sleep(0.5)
                                    state1 = 0
                                    adb_value, adb_text_color = status1[state1]
                                    window['INDICATOR1'].update(value=adb_value, text_color=adb_text_color)
                                    time.sleep(3)
                                    window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                              '正在重启!')
                                else:
                                    EP = pg.popup_ok('ADB is disconnect！！', title='warning ')
                                    if EP == 'Ok':
                                        break
                                    window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                              'adb is disconnect!')
                                    raise KeyError('ADB abnormal')
                        except KeyError as e:
                            print("ADB throw an exception：", repr(e))
                    print(f'Event:{event}')
                    print(str(values))
                window.close()
            elif values2["_USER_"] != 'admin':
                pg.PopupOK('用户名错误！')
                continue
            elif values2["_PASSWORD_"] != '123456':
                pg.PopupOK('密码错误！')
                continue
    LoginWindow.close()

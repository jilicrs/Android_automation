#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/12/29 16:40
# @Author    :risheng.chen@lango-tech.com
# @File      :guitest.py
__version__ = '1.0.0'

import datetime
from TestTool.guitestpage import ComPort
import PySimpleGUI as pg
from TestTool.guitestpage import ExitSystem, Send, TestManageSystem, Getport, \
    User, PassWord, Login, Cancel, file, open_comport, open_down, adb_connect, choose_instruct


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
        self.file = file
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


# Dark Blue 3
# Default 1
pg.change_look_and_feel('Default 1')

# justification='right'
status = [('\u2B24'+' Disconnect', 'red'), ('\u2B24'+' Connect', 'green')]
state = 0

status1 = [('\u2B24'+' Disconnect', 'red'), ('\u2b24'+' Connect', 'green')]
state1 = 0

# 打开串口****************************
open_up = pg.Button(ToolsPage().open_comport, font=('宋体', 10), size=(10, 1), key="_COMPORT_", border_width=3,
                    mouseover_colors='green', pad=(2, 6))

# 关闭串口****************************
cols_comport = pg.Button(ToolsPage().cols_comport, font=('宋体', 10), size=(10, 1), key="_COMPORT_COLS_",
                         border_width=3, mouseover_colors='red', pad=(2, 6))

# 指示灯******************************
Status = pg.Text(text=status[state][0], text_color=status[state][1], size=(12, 1),
                 font=("Courier New", 8), key='INDICATOR')

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
     font=("Courier New", 8), key='INDICATOR')],
    [pg.Text(text=ToolsPage().choose_instruct, size=(20, 1), font=("宋体", 10), relief='ridge', pad=(2, 6))],
    [pg.Combo(['Power_Off', 'Power_On'],
              size=(10, 1), font=("宋体", 10),
              default_value=['Power_Off'], key="_SERIAL_",
              background_color='', readonly=True)]
]

# 发送-退出===================================================================================================
send = [[bt, cbt]]

# 登录layout=================================================================================================
layout1 = [
    [pg.Image(size=(350, 50), filename=ToolsPage().file)],
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
              border_width=5, tooltip='config'),
     pg.Multiline("", size=(300, 26), key="_OUTPUT_", disabled=True, font=('楷体', 10), tooltip='display',
                  border_width=2)],
    [pg.Frame('send or exit', layout=send, pad=(10, 20), title_color='blue', title_location='n',
              element_justification='center', vertical_alignment='bottom', expand_x=True, border_width=5,
              tooltip='choose send or exit')]
]

# element_justification='center' 居中,登录layout标题栏
TitleLayout = [
    [pg.Frame(ToolsPage().TestManageSystem, layout=layout1, pad=(10, 10),
              title_location='n', element_justification='center')]
]

# no_titlebar=True 去掉标题栏，创建窗口==========================================================================
LoginWindow = pg.Window('LOGIN TEST SYSTEM', TitleLayout, size=(400, 190))
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
                LoginWindow.close()
                while True:
                    event, values = window.read()
                    if event == pg.WINDOW_CLOSED:
                        break
                    elif event in "_EXIT_":
                        ExitProject = pg.popup_yes_no('Whether to exit program？', title='warning ')
                        if ExitProject == 'Yes':
                            break
                        else:
                            continue
                    if event in "_GET_COMPORT_":
                        window['_SHOW_COMPORT_'].update(ToolsPage().get_port())
                    # 这里有问题+————++++++++++++++++++++++++++++++++++++++++++++++++++++——----------
                    if event in "_ADB_CONNECT_":
                        if "_ADB_IP_INPUT_" == '':
                            connect_ip = 1
                        else:
                            connect_ip = 0
                            print('ip状态', connect_ip)
                            if connect_ip == 1:
                                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y%m%d_%H%M%S:') +
                                                          'Error:enter the ip address you want to connect to')
                    # ++++++++++++++++++++++++++++++++________________________-------------------------
                    if event in "_COMPORT_":
                        try:
                            if ToolsPage().open_port():
                                if ToolsPage().open_port().isOpen():
                                    state = 1
                                    value, text_color = status[state]
                                    print(state)
                                    window['INDICATOR'].update(value=value, text_color=text_color)
                                    window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y%m%d_%H%M%S:') +
                                                              'Serial port enabled successfully!!!')
                                else:
                                    state = 0
                                    value, text_color = status[state]
                                    print(state)
                                    window['INDICATOR'].update(value=value, text_color=text_color)
                                    window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y%m%d_%H%M%S:') +
                                                              'Failed to open the serial port, '
                                                              'Check whether the serial port '
                                                              'is connected or occupied！')
                            elif not ToolsPage().open_port():
                                state = 0
                                value, text_color = status[state]
                                print(status)
                                window['INDICATOR'].update(value=value, text_color=text_color)
                                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y%m%d_%H%M%S:') +
                                                          'Failed to open the serial port')
                            else:
                                raise KeyError('Serial port exception')
                        except KeyError as e:
                            print("The serial port switch is abnormal. Procedure", repr(e))
                    elif event in "_COMPORT_COLS_":
                        try:
                            if ToolsPage().open_port().isOpen():
                                ToolsPage().close_port()
                                state = 0
                                value, text_color = status[state]
                                print("The serial port is off", state)
                                # pg.Print(state)
                                window['INDICATOR'].update(value=value, text_color=text_color)
                                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y%m%d_%H%M%S:') +
                                                          'The serial port is off')
                            elif state == 1:
                                state = 1
                                value, text_color = status[state]
                                print("Serial port not turned off", state)
                                window['INDICATOR'].update(value=value, text_color=text_color)
                                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y%m%d_%H%M%S:') +
                                                          'Serial port not turned off')
                            else:
                                raise KeyError('Serial port exception')
                        except KeyError as e:
                            print("The serial port switch is abnormal. Procedure", repr(e))
                    if event in "_SEND_":
                        try:
                            if state == 0:
                                EP = pg.popup_ok('Serial port not enabled！！', title='warning ')
                                if EP == 'Ok':
                                    break
                            elif values["_SERIAL_"] == 'Power_On' or 'Power_Off':
                                ToolsPage().serial_send_hex()
                                name = values["_SERIAL_"]
                                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y%m%d_%H%M%S:')+name)
                            else:
                                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y%m%d_%H%M%S:') +
                                                          'Send failed！')
                                raise KeyError('The value must be byte data')
                        except KeyError as e:
                            print("throw an exception：", repr(e))
                    print(f'Event:{event}')
                    print(str(values))
                window.close()
            else:
                pg.PopupOK('The user name or password is incorrect')
                continue
    LoginWindow.close()

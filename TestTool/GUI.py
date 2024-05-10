#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/12/29 21:27
# @Author    :risheng.chen@lango-tech.com
# @File      :GUI.py
__version__ = '1.0.0'

# import PySimpleGUI as sg
#
# layout = [
#     [sg.Text("Name: "), sg.Input(key='INPUT')],
#     [sg.Ok()],
#     [sg.Text("", size=(0, 1), key='OUTPUT')],
# ]
#
# window = sg.Window("Just a window", layout)
#
# while True:
#     event, values = window.read()
#     if event == sg.WINDOW_CLOSED:
#         break
#     elif event == 'Ok':
#         name = values['INPUT']
#         window['OUTPUT'].update(value=name)
#
# window.close()


# 2
# import PySimpleGUI as sg
# layout1 = [[sg.Text('temp text : ',pad=(30,30)),sg.Input('input field inside frame')]]
#
# layout = [
#           [sg.Frame('title', layout=layout1, title_location='n')]
#          ]
#
# window = sg.Window('frame ', layout,)
#
# event, values = window.read()
#
# window.close()

# 3
# import PySimpleGUI as sg
#
# sg.theme("DarkBlue3")
# sg.set_options(font=("Courier New", 16))
#
# status = [('\u2B24'+' Disconnect', 'red'), ('\u2B24'+' Connect', 'green')]
# state = 0
#
# layout = [
#     [sg.Text(text=status[state][0], text_color=status[state][1], size=(20, 1),
#              justification='center', font=("Courier New", 24), key='INDICATOR')],
#     [sg.Column([[sg.Button('Connect'), sg.Button('Disconnect')]], justification='center')],
# ]
#
# window = sg.Window('Title', layout, finalize=True)
#
# while True:
#     event, values = window.read()
#     if event in (sg.WINDOW_CLOSED, "Exit"):
#         break
#     elif event == 'Connect':
#         state = 1
#     elif event == 'Disconnect':
#         state = 0
#     if event in ('Disconnect', 'Connect'):
#         value, text_color = status[state]
#         window['INDICATOR'].update(value=value, text_color=text_color)
#
# window.close()

import PySimpleGUI as sg

layout = [[sg.Text('Input passworld:'), sg.Input(key='-PASSWORLD-', enable_events=True)],
          [sg.Button('EXIT')]]

window = sg.Window('', layout)

while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, 'EXIT']:
        break
    # 输入框事件，且输入框内容不为空时，如果不符合，便退格。
    if event == '-PASSWORLD-' and values['-PASSWORLD-'] and values['-PASSWORLD-'][-1] not in '0123456789':
        window['-PASSWORLD-'].update(values['-PASSWORLD-'][:-1])

window.close()

"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/1/19 16:10
@Author    :risheng.chen@lango-tech.cn
@File      :cv2_gui.py
__version__ = '2.0.0'
"""
import time
import os
import PySimpleGUI as sg
import datetime
from Cv2_Video.Cv2_Create_exe import draw_file
from logo_png import decode_image, encode_image


encode_image('D:\\Android automation\\Cv2_Video\\logo.png',
             'D:\\Android automation\\Cv2_Video\\encode.txt')
decode_image('D:\\Android automation\\Cv2_Video\\encode.txt',
             'D:\\Android automation\\Cv2_Video\\decode.png')

encode_image('D:\\Android automation\\Cv2_Video\\android.ico',
             'D:\\Android automation\\Cv2_Video\\encode1.txt')
decode_image('D:\\Android automation\\Cv2_Video\\encode1.txt',
             'D:\\Android automation\\Cv2_Video\\decode1.ico')


front_layout = [

        [sg.Image('decode.png', size=(550, 120), background_color='#add123', pad=(15, 2))],
        [sg.Text(text='CV-2', font=('楷体', 80), size=(5, 1), key='_SCREEN_TIME_', border_width=3,
                     pad=(150, 10), relief='ridge', background_color='#add123', text_color='blue')],
        [sg.Text(text='•Version:2.0', font=('宋体', 10), size=(12, 1), key='_SCREEN_TIME_', border_width=3,
                 pad=(150, 10), relief='ridge')],
        [sg.Text(text='1.修复截图无法保存至中文路径', font=('宋体', 10), size=(27, 1), key='_SCREEN_TIME_', border_width=3,
                 pad=(150, 1), relief='ridge', background_color='#add123', text_color='yellow')],
        [sg.Text(text='2.添加output打印窗口', font=('宋体', 10), size=(20, 1), key='_SCREEN_TIME_', border_width=3,
                 pad=(150, 1), relief='ridge', background_color='#add123', text_color='yellow')],
        # [sg.one_line_progress_meter(title='正在加载...', current_value=0, max_value=100, key='key2', orientation='h')]
        [sg.ProgressBar(200, size=(30, 20), orientation='h', pad=(150, 1), key='progressbar')]

]




layout = [

            [sg.FolderBrowse(button_text='打开文件', size=(10, 1), key="_OPENFILE_", disabled=False, pad=(10, 10)), sg.In()],

            [sg.FolderBrowse(button_text='保存文件', size=(10, 1), key="_SAVEFILE_", disabled=False, pad=(10, 2)), sg.In()],
            [sg.Text(text='截图时间点：', font=('宋体', 10), size=(12, 1), key='_SCREEN_TIME_', border_width=3,
                     pad=(10, 10), relief='ridge'),
             sg.InputText("", key='_TIME_INPUT_', font=('楷体', 10), size=(14, 1), pad=(10, 10), border_width=3)],
            # ==========================================
            [sg.Multiline("", size=(100, 2), key="_OUTPUT_", disabled=True, font=('楷体', 10), tooltip=None,
                         border_width=2,  pad=(10, 2), autoscroll=True, reroute_cprint=True)],
            [sg.Output(size=(200, 18), pad=(10, 1), key='_OUT_')],
            # =========================================
            [sg.Button(button_text='开始截图', font=('宋体', 10), size=(10, 1), border_width=3, pad=(10, 10),
                       key='_START_DRAW_'),
            sg.Button(button_text='退出', font=('宋体', 10), size=(10, 1), border_width=3, pad=(10, 10),
                      key='_EXIT_')],

        ]

# 主题背景
sg.theme('LightGrey1')
window_f = sg.Window('', no_titlebar=True, layout=front_layout, size=(600, 380), background_color='white',
                     grab_anywhere=True, transparent_color='#add123')

window = sg.Window('视频截图工具', layout=layout, size=(800, 500), resizable=True, icon='decode1.ico',
                   transparent_color='#add123')

# 根据key值获取进度条
Progress_Bar = window_f['progressbar']

def main():
    while True:
        for i in range(200):
            event1, values1 = window_f.read(timeout=10)
            if event1 is None:
                break
            Progress_Bar.UpdateBar(i + 1)


        window_f.close()
        os.remove('decode.png')
        os.remove('encode.txt')

        while True:
            event, values = window.read(timeout=20)
            if event is None:
                break
            if event == '_EXIT_'  or sg.WINDOW_CLOSED:
                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +'退出！')
                ExitProject = sg.popup_yes_no('是否退出程序？', title='warning ', icon='decode1.ico',
                                              grab_anywhere=True)
                if ExitProject == 'Yes':
                    break
                else:
                    continue
            if event == '_START_DRAW_':
                    # 编译时去掉print values=========================================================
                    print(values)
                    # 编译时去掉print values=========================================================
                    if values['_OPENFILE_'] and values['_SAVEFILE_'] and values['_TIME_INPUT_']:
                        draw_file(video_folder=values['_OPENFILE_'], output_folder=values['_SAVEFILE_'],
                                  second=int(values['_TIME_INPUT_']))
                        window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                  '截图成功!!')
                        continue
                    elif values['_OPENFILE_'] == '':
                        window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                              '请选择文件夹')
                        continue
                    elif values['_SAVEFILE_'] == '':
                        window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                  '请选择保存位置')
                        continue
                    elif values['_TIME_INPUT_'] == '':
                        window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S:') +
                                                  '请输入截图位置（秒）')
                        continue
        os.remove('decode1.ico')
        os.remove('encode1.txt')
        window.close()

        break




if __name__ == '__main__':
    main()




























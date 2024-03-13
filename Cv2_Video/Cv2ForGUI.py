"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/1/19 16:10
@Author    :risheng.chen@lango-tech.cn
@File      :Cv2ForGUI.py
__version__ = '3.0.0'
"""

import base64
import os
import PySimpleGUI as sg
import datetime
from Cv2_Video.VideoShotsSeconds import cut_video
from Cv2_Video.VideoShotsFile import draw_file
from Cv2_Video.android_ico import img as pic
from Cv2_Video.fromlogo_png import img as pic1
# from Cv2_Video.cvtelogo_png import img as pic1

# 创建图片并进行解码，释放资源
tmp = open('decode.png', 'wb')
tmp.write(base64.b64decode(pic1))
tmp.close()


# 创建图片并进行解码，释放资源
tmp1 = open('decode1.ico', 'wb')
tmp1.write(base64.b64decode(pic))
tmp1.close()


front_layout = [

        [sg.Image('decode.png', size=(550, 120), background_color='white', pad=(15, 2))],
        [sg.Text(text='CV-2', font=('楷体', 80), size=(5, 1), key='_SCREEN_TIME_', border_width=3,
                     pad=(150, 10), relief='ridge', background_color='#add123', text_color='blue')],
        [sg.Text(text='•Version:3.0', font=('宋体', 10), size=(12, 1), key='_SCREEN_TIME_', border_width=3,
                 pad=(155, 10), relief='ridge', text_color='red', background_color='black')],
        [sg.Text(text='1.修复截图无法保存至中文路径', font=('宋体', 10), size=(27, 1), key='_SCREEN_TIME_', border_width=3,
                 pad=(155, 1), relief='ridge', background_color='black', text_color='yellow')],
        [sg.Text(text='2.添加output打印窗口', font=('宋体', 10), size=(20, 1), key='_SCREEN_TIME_', border_width=3,
                 pad=(155, 1), relief='ridge', background_color='black', text_color='yellow')],
        [sg.Text(text='3.新增文件间隔截取指定帧数', font=('宋体', 10), size=(25, 1), key='_SCREEN_TIME_', border_width=3,
                 pad=(155, 1), relief='ridge', background_color='black', text_color='yellow')],
        [sg.Text(text='4.优化系统逻辑', font=('宋体', 10), size=(15, 1), key='_SCREEN_TIME_', border_width=3,
                 pad=(155, 1), relief='ridge', background_color='black', text_color='yellow')],
        [sg.ProgressBar(200, size=(30, 20), orientation='h', pad=(155, 1), key='progressbar')]

]




layout = [
            [sg.FolderBrowse(button_text='打开文件', size=(10, 1), key="_OPENFILE_", disabled=False, pad=(10, 10)),
             sg.In(key="_OPENFILE_TEXT_")],

            [sg.FolderBrowse(button_text='保存文件', size=(10, 1), key="_SAVEFILE_", disabled=False, pad=(10, 2)),
             sg.In(key="_SAVEFILE_TEXT_")],
            [sg.Text(text='截图时间点：', font=('宋体', 10), size=(12, 1), key='_SCREEN_TIME_', border_width=3,
                     pad=(10, 10), relief='ridge'),
             sg.InputText("", key='_TIME_INPUT_', font=('楷体', 10), size=(14, 1), pad=(10, 10), border_width=3)],
            # ==========================================
            [sg.Multiline("", size=(100, 1), key="_OUTPUT_", disabled=True, font=('楷体', 10), tooltip=None,
                         border_width=2,  pad=(10, 2), autoscroll=True, reroute_cprint=True)],
            [sg.Output(size=(200, 21), pad=(10, 1), key='_OUT_', text_color='yellow', font=('楷体', 10),
                       background_color='black')],
            # =========================================
            [sg.Button(button_text='开始截图(每个视频的某一帧)', font=('宋体', 10), size=(25, 1),
                       border_width=3, pad=(10, 10),
                       key='_START_DRAW_'),
            sg.Button(button_text='开始截图（每个视频间隔多久截图一帧）', font=('宋体', 10), size=(35, 1),
                      border_width=3, pad=(10, 10),
                       key='_START_DRAW_MORE_'),
            sg.Button(button_text='退出', font=('宋体', 10), size=(10, 1), border_width=3, pad=(10, 10),
                      key='_EXIT_')],

        ]

# 主题背景
sg.theme('LightGrey1')
window_f = sg.Window('', no_titlebar=True, layout=front_layout, size=(600, 430), background_color='white',
                     grab_anywhere=True, transparent_color='#add123')

window = sg.Window('视频截图工具 v3.0', layout=layout, size=(800, 480), resizable=True, icon='decode1.ico',
                   transparent_color='#add123')

Progress_Bar = window_f['progressbar']

def main():
    while True:
        for i in range(200):
            # 必须异步（timeout=xx）执行，否则不会往下跑
            event1, values1 = window_f.read(timeout=10)
            if event1 is None:
                break
            Progress_Bar.UpdateBar(i + 1)


        window_f.close()
        # 删除解码图片，释放内存
        os.remove('decode.png')

        while True:
            event, values = window.read(timeout=20)
            if event is None:
                break
            elif event == '_EXIT_'  or sg.WINDOW_CLOSED:
                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S:') +'退出！')
                ExitProject = sg.popup_yes_no('是否退出程序？', title='warning ', icon='decode1.ico',
                                              grab_anywhere=True)
                if ExitProject == 'Yes':
                    break
                else:
                    continue
            elif event == '_START_DRAW_':
                    if values['_OPENFILE_TEXT_'] and values['_SAVEFILE_TEXT_'] and values['_TIME_INPUT_']:
                        if values['_TIME_INPUT_'].isnumeric():
                            if draw_file(video_folder=values['_OPENFILE_TEXT_'],
                                         output_folder=values['_SAVEFILE_TEXT_'],
                                         second=int(values['_TIME_INPUT_'])):
                                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S:') +
                                                      '截图成功!!')
                                sg.popup_notify('ScreenCap done!', location=(700, 500))

                            else:
                                window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S:') +
                                                      '截图失败!!')
                        else:
                            sg.popup_ok('请输入单位（s），每个视频的指定帧数!', title='warning ', icon='decode1.ico',
                                        grab_anywhere=True)

                    elif values['_OPENFILE_TEXT_'] == '':
                        window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S:') +
                                                              '请选择文件夹!')
                        sg.popup_ok('请选择文件夹!', title='warning ', icon='decode1.ico',
                                                      grab_anywhere=True)

                    elif values['_SAVEFILE_TEXT_'] == '':
                        window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S:') +
                                                  '请选择保存位置!')
                        sg.popup_ok('请选择保存位置!', title='warning ', icon='decode1.ico',
                                    grab_anywhere=True)

                    elif values['_TIME_INPUT_'] == '':
                        window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S:') +
                                                  '请输入截图指定帧数（秒）!')
                        sg.popup_ok('请输入截图指定帧数（秒）!', title='warning ', icon='decode1.ico',
                                    grab_anywhere=True)
            elif event == '_START_DRAW_MORE_':
                if values['_OPENFILE_TEXT_'] and values['_SAVEFILE_TEXT_'] and values['_TIME_INPUT_']:
                    if values['_TIME_INPUT_'].isnumeric():
                        if cut_video(video_path=values['_OPENFILE_TEXT_'] + '\\',
                                     f_save_path=values['_SAVEFILE_TEXT_'] + '\\',
                                     time_interval=int(values['_TIME_INPUT_'])):
                            window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S:') +
                                                      '截图成功!!')
                            sg.popup_notify('ScreenCap done!', location=(700, 500))

                        else:
                            window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S:') +
                                                      '截图失败!!')
                    else:
                        sg.popup_ok('请输入单位（s），每个视频间隔s截图!', title='warning ', icon='decode1.ico',
                                    grab_anywhere=True)

                elif values['_OPENFILE_TEXT_'] == '':
                    window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S:') +
                                              '请选择文件夹!')
                    sg.popup_ok('请选择文件夹!', title='warning ', icon='decode1.ico',
                                grab_anywhere=True)

                elif values['_SAVEFILE_TEXT_'] == '':
                    window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S:') +
                                              '请选择保存位置!')
                    sg.popup_ok('请选择保存位置!', title='warning ', icon='decode1.ico',
                                grab_anywhere=True)

                elif values['_TIME_INPUT_'] == '':
                    window['_OUTPUT_'].update(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S:') +
                                              '请输入截图间隔帧数（秒）!')
                    sg.popup_ok('请输入截图间隔帧数（秒）!', title='warning ', icon='decode1.ico',
                                grab_anywhere=True)


        #  删除解码图片，释放储存资源
        os.remove('decode1.ico')
        window.close()

        break




if __name__ == '__main__':
    main()




























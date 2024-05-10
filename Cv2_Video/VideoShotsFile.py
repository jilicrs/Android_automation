"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/1/19 15:20
@Author    :risheng.chen@lango-tech.cn
@File      :VideoShotsFile.py
__version__ = '3.1.0'
"""

import cv2
import os
import datetime
import PySimpleGUI as sg
from Cv2_Video.Cv2Thread import MyThread


def extract_frame(video_path, output_path, second, windows):
    # 打开视频文件
    vidcap = cv2.VideoCapture(video_path)

    # 设置要截取的时间点（秒数）
    vidcap.set(cv2.CAP_PROP_POS_MSEC, second * 1000)

    # 读取视频的帧
    success, image = vidcap.read()

    if success:
        cv2.imencode('.png', image)[1].tofile(output_path)
        windows.update(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S:') +
                       '正在截图!!')
        print(f"成功截取视频 {video_path} 中的第 {second} 秒的帧，并保存到 {output_path}。")
    else:
        windows.update(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S:') +
                       '截图失败!!')
        print(f"截取视频 {video_path} 中的第 {second} 秒的帧失败。")

    # 释放资源
    vidcap.release()


def draw_file(video_folder, output_folder, second, windows) -> bool:
    # 遍历文件夹内容，root：文件夹根目录， dirs：文件夹子目录，files：文件夹内所有文件
    for root, dirs, files in os.walk(video_folder):
        if not files:
            print('*****************文件夹为空*****************')
            return False
        else:
            # 定义寻找的文件格式
            fm = ['.mp4']
            # 获取列表中符合条件的字符串
            elem = list(filter(lambda text: all([word in text for word in fm]), files))
            if elem:
                # 遍历文件
                for filename in os.listdir(video_folder):
                    if filename.endswith(".mp4"):
                        # 构建视频文件路径
                        video_path = os.path.join(video_folder, filename)

                        # 构建输出图片文件路径
                        output_filename = f"{os.path.splitext(filename)[0]}_{second}s.jpg"
                        output_path = os.path.join(output_folder, output_filename)


                        # 调用函数截取图片
                        extract_frame(video_path, output_path, second, windows)
                return True
            else:
                print('*****************文件夹内没有MP4文件*****************')
                return False




def start_draw_file(video_folder, output_folder, second, windows) -> str:
    """
    start_draw_file：定义接口单独线程，防止主函数在运行接口时阻塞主线程
    :param video_folder: 需要截图得文件夹
    :param output_folder: 保存到指定文件夹
    :param second: 秒（int）
    :param windows: 信息输出窗口
    :return:
    """
    thread = MyThread(target=draw_file, arges=(video_folder, output_folder, second, windows))
    thread.start()
    result = thread.get_result()

    sg.popup_notify('ScreenCap!', location=(700, 500))
    return result











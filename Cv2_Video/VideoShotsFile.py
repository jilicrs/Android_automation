"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/1/19 15:20
@Author    :risheng.chen@lango-tech.cn
@File      :VideoShotsFile.py
__version__ = '2.1.0'
"""

import cv2
import os


def extract_frame(video_path, output_path, second):
    # 打开视频文件
    vidcap = cv2.VideoCapture(video_path)

    # 设置要截取的时间点（秒数）
    vidcap.set(cv2.CAP_PROP_POS_MSEC, second * 1000)

    # 读取视频的帧
    success, image = vidcap.read()

    if success:
        cv2.imencode('.png', image)[1].tofile(output_path)
        print(f"成功截取视频 {video_path} 中的第 {second} 秒的帧，并保存到 {output_path}。")
    else:
        print(f"截取视频 {video_path} 中的第 {second} 秒的帧失败。")

    # 释放资源
    vidcap.release()


def draw_file(video_folder, output_folder, second):
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
                        extract_frame(video_path, output_path, second)
                return True
            else:
                print('*****************文件夹内没有MP4文件*****************')
                return False

















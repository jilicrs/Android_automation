"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/1/19 15:20
@Author    :risheng.chen@lango-tech.cn
@File      :Cv2_Create_exe.py
__version__ = '2.0.0'
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
        # 保存图片
        # imwrite无法保存文件到中文路径
        # cv2.imwrite(output_path, image)

        # 使用imencode方法将文件保存到中文路径
        cv2.imencode('.png', image)[1].tofile(output_path)
        print(f"成功截取视频 {video_path} 中的第 {second} 秒的帧，并保存到 {output_path}。")
    else:
        print(f"截取视频 {video_path} 中的第 {second} 秒的帧失败。")

    # 释放资源
    vidcap.release()


def draw_file(video_folder, output_folder, second):
    for filename in os.listdir(video_folder):
        if filename.endswith(".mp4"):
            # 构建视频文件路径
            video_path = os.path.join(video_folder, filename)

            # 构建输出图片文件路径
            output_filename = f"{os.path.splitext(filename)[0]}_{second}s.jpg"
            output_path = os.path.join(output_folder, output_filename)

            # 调用函数截取图片
            extract_frame(video_path, output_path, second)
















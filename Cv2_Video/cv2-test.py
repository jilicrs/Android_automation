"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/1/19 10:20
@Author    :risheng.chen@lango-tech.cn
@File      :Cv2_Video-test.py
__version__ = '1.0.0'
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
        cv2.imwrite(output_path, image)
        print(f"成功截取视频 {video_path} 中的第 {second} 秒的帧，并保存到 {output_path}。")
    else:
        print(f"截取视频 {video_path} 中的第 {second} 秒的帧失败。")

    # 释放资源
    vidcap.release()



if __name__ == '__main__':
    test1 = '2024011716'
    test2 = '2024011717'
    test3 = '2024011718'
    test4 = '2024011719'
    test5 = '2024011720'
    test6 = '2024011721'
    test7 = '2024011722'
    test8 = '2024011723'
    test9 = '2024011800'
    test10 = '2024011801'
    test11 = '2024011802'
    test12 = '2024011803'
    test13 = '2024011804'
    test14 = '2024011805'
    test15 = '2024011806'
    test16 = '2024011807'
    test17 = '2024011808'
    test18 = '2024011809'
    test19 = '2024011810'
    test20 = '2024011811'
    test21 = '2024011812'
    test22 = '2024011813'
    test23 = '2024011814'
    test24 = '2024011815'

    output1 = 'output1'
    output2 = 'output2'
    output3 = 'output3'
    output4 = 'output4'
    output5 = 'output5'
    output6 = 'output6'
    output7 = 'output7'
    output8 = 'output8'
    output9 = 'output9'
    output10 = 'output10'
    output11 = 'output11'
    output12 = 'output12'
    output13 = 'output13'
    output14 = 'output14'
    output15 = 'output15'
    output16 = 'output16'
    output17 = 'output17'
    output18 = 'output18'
    output19 = 'output19'
    output20 = 'output20'
    output21 = 'output21'
    output22 = 'output22'
    output23 = 'output23'
    output24 = 'output24'


    start = 19
    end = 25

    while True:
        if start < end:

            if start == 19:
                print('==========')
                video_folder = 'E:\\MIJIA_RECORD_VIDEO\\' + test19
                output_folder = 'E:\\output\\' + output19
                second = 11

                for filename in os.listdir(video_folder):
                    if filename.endswith(".mp4"):
                        # 构建视频文件路径
                        video_path = os.path.join(video_folder, filename)

                        # 构建输出图片文件路径
                        output_filename = f"{os.path.splitext(filename)[0]}_{second}s.jpg"
                        output_path = os.path.join(output_folder, output_filename)

                        # 调用函数截取图片
                        extract_frame(video_path, output_path, second)

                        continue
                start += 1
                continue
            elif start == 20:
                print('===========')
                video_folder = 'E:\\MIJIA_RECORD_VIDEO\\' + test20
                output_folder = 'E:\\output\\' + output20
                second = 11

                for filename in os.listdir(video_folder):
                    if filename.endswith(".mp4"):
                        # 构建视频文件路径
                        video_path = os.path.join(video_folder, filename)

                        # 构建输出图片文件路径
                        output_filename = f"{os.path.splitext(filename)[0]}_{second}s.jpg"
                        output_path = os.path.join(output_folder, output_filename)

                        # 调用函数截取图片
                        extract_frame(video_path, output_path, second)

                        continue
                start += 1
                continue
            elif start == 21:
                print('===========')
                video_folder = 'E:\\MIJIA_RECORD_VIDEO\\' + test21
                output_folder = 'E:\\output\\' + output21
                second = 11

                for filename in os.listdir(video_folder):
                    if filename.endswith(".mp4"):
                        # 构建视频文件路径
                        video_path = os.path.join(video_folder, filename)

                        # 构建输出图片文件路径
                        output_filename = f"{os.path.splitext(filename)[0]}_{second}s.jpg"
                        output_path = os.path.join(output_folder, output_filename)

                        # 调用函数截取图片
                        extract_frame(video_path, output_path, second)

                        continue
                start += 1
                continue
            elif start == 22:
                print('=======')
                video_folder = 'E:\\MIJIA_RECORD_VIDEO\\' + test22
                output_folder = 'E:\\output\\' + output22
                second = 11

                for filename in os.listdir(video_folder):
                    if filename.endswith(".mp4"):
                        # 构建视频文件路径
                        video_path = os.path.join(video_folder, filename)

                        # 构建输出图片文件路径
                        output_filename = f"{os.path.splitext(filename)[0]}_{second}s.jpg"
                        output_path = os.path.join(output_folder, output_filename)

                        # 调用函数截取图片
                        extract_frame(video_path, output_path, second)

                        continue
                start += 1
                continue
            elif start == 23:
                print('=======')
                video_folder = 'E:\\MIJIA_RECORD_VIDEO\\' + test23
                output_folder = 'E:\\output\\' + output23
                second = 11

                for filename in os.listdir(video_folder):
                    if filename.endswith(".mp4"):
                        # 构建视频文件路径
                        video_path = os.path.join(video_folder, filename)

                        # 构建输出图片文件路径
                        output_filename = f"{os.path.splitext(filename)[0]}_{second}s.jpg"
                        output_path = os.path.join(output_folder, output_filename)

                        # 调用函数截取图片
                        extract_frame(video_path, output_path, second)

                        continue
                start += 1
                continue
            elif start == 24:
                print('===========')
                video_folder = 'E:\\MIJIA_RECORD_VIDEO\\' + test24
                output_folder = 'E:\\output\\' + output24
                second = 11

                for filename in os.listdir(video_folder):
                    if filename.endswith(".mp4"):
                        # 构建视频文件路径
                        video_path = os.path.join(video_folder, filename)

                        # 构建输出图片文件路径
                        output_filename = f"{os.path.splitext(filename)[0]}_{second}s.jpg"
                        output_path = os.path.join(output_folder, output_filename)

                        # 调用函数截取图片
                        extract_frame(video_path, output_path, second)

                        continue
                start += 1
                continue
            elif start >= end:
                print('输出完成')
                break














































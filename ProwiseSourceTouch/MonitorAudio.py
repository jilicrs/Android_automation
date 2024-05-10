#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/4/7 16:49
# @Author    :risheng.chen@lango-tech.com
# @File      :MonitorAudio.py
__version__ = '1.0.0'

import datetime
import subprocess
import time
import os
import pyaudio
import wave
from subprocess import Popen, PIPE, STDOUT
from moviepy.editor import *


CHUNK = 1024 # 每个缓冲区的帧数
FORMAT = pyaudio.paInt16 # 采样位数
CHANNELS = 2 # 双声道
RATE = 44100 # 采样频率

def record_audio(wave_out_path, record_second):
    """ 录音功能 """
    p = pyaudio.PyAudio() # 实例化对象
    stream = p.open(format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK) # 打开流，传入响应参数
    wf = wave.open(wave_out_path, 'wb') # 打开 wav 文件。
    wf.setnchannels(CHANNELS) # 声道设置
    wf.setsampwidth(p.get_sample_size(FORMAT)) # 采样位数设置
    wf.setframerate(RATE) # 采样频率设置

    for _ in range(0, int(RATE * record_second / CHUNK)):
        data = stream.read(CHUNK)
        wf.writeframes(data) # 写入数据
    stream.stop_stream() # 关闭流
    stream.close()
    p.terminate()
    wf.close()



def play_audio(wave_input_path):
    p = pyaudio.PyAudio() # 实例化
    wf = wave.open(wave_input_path, 'rb') # 读 wav 文件
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output=True)
    data = wf.readframes(CHUNK) # 读数据
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream() # 关闭资源
    stream.close()
    p.terminate()


class AndroidRecord(object):
    def __init__(self, save_path = 'D:\\record\\', adb_device = 'hht12345678',
                 record_path = '/sdcard'):
        self.save_path = save_path
        self.device = adb_device
        self.record_path = record_path

    def android_record(self):
        print('开始录音')
        Popen(r'adb -s {} shell screenrecord --time-limit 50 {}/record.mp4'.format(self.device, self.record_path))
        print('停止录音')
        time.sleep(2)
        filepath = os.path.exists(self.save_path)
        if not filepath:
            os.mkdir(self.save_path)
            time.sleep(2)
            # print('导出录音文件')
            # Popen(r'adb -s {} pull {}/record.mp4 {}'.format(self.device, self.record_path ,self.save_path))
            # exit(code=datetime.datetime.now().strftime('%H:%M:%S'))
        else:
            time.sleep(2)
            print('导出录音文件')
            Popen(r'adb -s {} pull /storage/emulated/0/Music/record.mp4 {}'.format(self.device, self.save_path))

            exit(code=datetime.datetime.now().strftime('%H:%M:%S'))






if __name__ == '__main__':
    # print(record_audio('test.mp3', 5))
    # print(play_audio('test.mp3'))

    # AndroidRecord().android_record()

    video = VideoFileClip('D:\\record\\test.mp4')
    audio = video.audio
    audio.write_audiofile('D:\\record\\demo.wav')
    audio.write_audiofile('D:\\record\\demo.mp3')
























#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/11/9 11:03
# @Author    :risheng.chen@lango-tech.com
# @File      :ProwiseTest2.py
__version__ = '1.0.0'

import os
import sys
import pygame
from Prowise.kun_png import img as pic
import base64

# 初始化pygame
pygame.init()

# 设置窗口
size = width, height = 640, 480
# 显示窗口
screen = pygame.display.set_mode(size)
pygame.display.set_caption('移动的ikun')
# 设置窗口颜色
black = (0, 0, 0)
white = (255, 255, 255)
gray = (230, 230, 230)

# 解码图片
tmp = open('ikun.png', 'wb')
tmp.write(base64.b64decode(pic))
tmp.close()



# 加载图片
ball = pygame.image.load('ikun.png').convert_alpha()
# 获取矩形区域
ball_rect = ball.get_rect()

# 设置移动的x， y轴距离
speed = [2, 2]
# 设置时钟
clock = pygame.time.Clock()

if __name__ == '__main__':
    while True:
        clock.tick(100) # 每秒执行次数
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.remove('ikun.png')
                pygame.quit()
                sys.exit()
        ball_rect = ball_rect.move(speed) # 移动图片
        if ball_rect.left < 0 or ball_rect.right > width: # 碰到左右边缘
            speed[0] = -speed[0]
        if ball_rect.top < 0 or ball_rect.bottom > height: # 碰到上下边缘
            speed[1] = -speed[1]
        screen.fill(black) # 填充颜色
        screen.blit(ball, ball_rect) # 将图片显示到窗口上

        pygame.display.flip() # 更新全部显示











































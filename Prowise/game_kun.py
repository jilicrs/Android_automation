"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2023/12/2 16:47
@Author    :risheng.chen@lango-tech.cn
@File      :game_kun.py
__version__ = '1.0.0'
"""

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

# 获取窗口矩形
screen_rect = screen.get_rect()

# 获取窗口的四边
screen_top = screen_rect.top
screen_bottom = screen_rect.bottom
screen_left = screen_rect.left
screen_right = screen_rect.right

# 窗口名称
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
ball = pygame.image.load('D:\\Img\\123.png').convert_alpha()
# 获取图片矩形区域
ball_rect = ball.get_rect()

# 设置移动的x， y轴距离
speed = [2, 2]

# 加载第二个图片
kun = pygame.image.load('ikun.png')
# 获取图片矩形，宽高
kun_rect = kun.get_rect()
kun_width = kun.get_width()
kun_height = kun.get_height()

x = width/2 - kun_width/2
y = height - kun_height

speed_kun = [5, 5]


# 设置时钟
clock = pygame.time.Clock()

pygame.key.set_repeat(10)

if __name__ == '__main__':
    while True:
        clock.tick(80) # 每秒执行次数
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.remove('ikun.png')
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= speed_kun[0]

                    if x <= screen_left - kun_width:
                        x = screen_right

                elif event.key == pygame.K_RIGHT:
                    x += speed_kun[0]

                    if x >= screen_rect.right:
                        x = screen_rect.left - kun_width

                elif event.key == pygame.K_UP:
                    y -= speed_kun[1]
                    if y <= screen_top - kun_height:
                        y = screen_bottom

                elif event.key == pygame.K_DOWN:
                    y += speed_kun[1]
                    if y >= screen_bottom:
                        y = screen_top - kun_height

                elif event.key:
                    continue

        ball_rect = ball_rect.move(speed) # 移动图片
        if ball_rect.left < 0 or ball_rect.right > width: # 碰到左右边缘
            speed[0] = -speed[0]
        if ball_rect.top < 0 or ball_rect.bottom > height: # 碰到上下边缘
            speed[1] = -speed[1]
        screen.fill(white) # 填充颜色
        screen.blit(ball, ball_rect) # 将图片显示到窗口上

        # 获取键值
        keys = pygame.key.get_pressed()
        print(keys)



        screen.blit(kun, (x, y))

        pygame.display.flip() # 更新全部显示







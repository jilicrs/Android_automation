#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/11/16 21:48
# @Author    :risheng.chen@lango-tech.com
# @File      :RecoverTest.py
__version__ = '1.0.0'

import os
import tkinter as tk
from tkinter import simpledialog
import pandas as pd
from tkinter import messagebox
import json

# 使用messagebox模块显示欢迎信息
messagebox.showinfo("欢迎", "欢迎使用家长手机监控系统！")


# 将用户注册的账号信息保存到一个名为 "用户账号.json" 的文件中
def save_credentials(credentials):
    with open("用户账号.json", "w") as file:
        # credentials 转换为 JSON 格式，并将其写入用户账号.json
        json.dump(credentials, file)


# 使用 open 函数打开一个名为 "用户账号.json" 的文件以进行读取操作
def load_credentials():
    try:
        with open("用户账号.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# 注册一个新用户
def register():
    username = simpledialog.askstring("注册", "请输入用户名：")
    password = simpledialog.askstring("注册", "请输入密码：")
    # 用户名和密码添加到 user_credentials 字典中，并调用 save_credentials() 函数保存
    user_credentials[username] = password
    save_credentials(user_credentials)
    messagebox.showinfo("注册成功", "注册成功！")


# 用户登录
def login():
    # 这里定义全局变量emulator_address，方便后面使用该地址
    global emulator_address
    username = simpledialog.askstring("登录", "请输入用户名：")
    password = simpledialog.askstring("登录", "请输入密码：")
    # 判断输入的用户名和密码是否正确
    # 输入的username是否在user_credentials字典中
    if username in user_credentials:
        # 输入的密码是否和字典中该用户名对应的密码相等
        if user_credentials[username] == password:
            messagebox.showinfo("登录成功", "登录成功！")
            # 调用该函数，跳转到下一个窗口
            Login_successful()
            # 在这里调用address()函数，是为了让用户登录成功后才能连接手机
            emulator_address = address()  # 调用函数，输入地址，赋值给全局变量
    else:
        messagebox.showerror("登录失败", "用户名或密码错误！")


# 加载保存的账号数据
user_credentials = load_credentials()

window = tk.Tk()  # 创建页面
window.geometry('300x300')  # 设置窗口大小
window.title("身份登录窗口")

# 这里是登录的窗口，创建注册和登录按钮
register_button = tk.Button(window, text="注册", command=register)
register_button.grid(row=0, column=0, padx=10, pady=10)

login_button = tk.Button(window, text="登录", command=login)
login_button.grid(row=2, column=0, padx=10, pady=10)


# emulator_address = "127.0.0.1:16386"  # 模拟器连接地址和端口
# 10.34.122.163:8888#手机的连接地址和端口

# 输入地址
def address():
    emulator_address = simpledialog.askstring("输入连接地址和端口", "请输入连接地址和端口：")
    return emulator_address


# 向连接的 Android 模拟器发送 adb 命令
def send_adb_command(command):
    os.system(f"adb -s {emulator_address} {command}")


# 截图
def take_screenshot():
    # 在设备上执行截屏操作，并将截图保存到 /sdcard/screenshot.png 文件中。
    send_adb_command('shell screencap -p /sdcard/screenshot.png')
    # 命令将设备上的截图文件下载到计算机本地。
    send_adb_command('pull /sdcard/screenshot.png')
    result = send_adb_command('pull /sdcard/screenshot.png')
    if result:
        print('截屏并成功保存')


# 锁屏
def lock_screen():
    send_adb_command('shell input keyevent 26')
    result = send_adb_command('shell input keyevent 26')
    if result:
        print('手机屏幕已经锁定')


# 亮屏
def light_up():
    send_adb_command('shell input keyevent 224')  # 黑屏状态下亮屏
    result = send_adb_command('shell input keyevent 224')
    if result:
        print('亮屏成功')


# 解锁屏幕
def unlock_screen():
    send_adb_command('shell input swipe 358 965 350 285 30')  # 前两个坐标是滑动起始点的坐标，后两个坐标，是滑动终点的坐标
    result = send_adb_command('shell input swipe 358 965 350 285 30')
    if result:
        print('手机屏幕开锁成功')


# 关机
def turn_off():
    send_adb_command('shell reboot -p')
    result = send_adb_command('shell reboot -p')
    if result:
        print('手机已关机')


# 开机
def turn_on():
    send_adb_command('shell reboot')
    result = send_adb_command('shell reboot')
    if result:
        print('手机已开机')


# 关闭wifi
def disable_wifi():
    send_adb_command('shell svc wifi disable')
    result = send_adb_command('shell svc wifi disable')
    if result:
        print('WiFi已关闭')


# 开启wifi
def enable_wifi():
    send_adb_command('shell svc wifi enable')
    result = send_adb_command('shell svc wifi enable')
    if result:
        print('WiFi已开启')


# 打电话号码
def make_phone_call():
    phone_number = simpledialog.askstring("输入电话号码", "请输入电话号码：")
    if phone_number:
        command = f"shell am start -a android.intent.action.CALL -d tel:{phone_number}"
        send_adb_command(command)
        result = send_adb_command(command)
        if result:
            print("电话拨打成功")


# 浏览网页
def browse_web():
    # 使用了simpledialog.askstring()函数创建了一个输入对话框，用户可以在其中输入网页地址
    web_address = simpledialog.askstring("输入网页地址", "请输入网页地址：")
    if web_address:
        send_adb_command(f'shell am start -a android.intent.action.VIEW -d {web_address}')
        print('正在浏览中')
        send_adb_command('shell screencap -p /sdcard/screenshot1.png')  # 截屏
        send_adb_command('pull /sdcard/screenshot1.png')  # 保存图片


# 滑屏
def Swipe_the_screen():
    command = 'shell input swipe 358 965 350 285 30'  # 前两个坐标是滑动起始点的坐标，后两个坐标，是滑动终点的坐标
    send_adb_command(command)


# 打开手机的GPS定位
def open_gps_location():
    # 执行adb命令打开GPS定位
    command = 'shell settings put secure location_providers_allowed +gps'
    result = send_adb_command(command)
    if result:
        print('GPS定位已开启')


# 对手机进行定位
def get_gps_location():
    command = 'adb shell dumpsys location'
    # 这里得到的输出结果里面，有当前手机的经纬度，是Last Known Locations:下面的内容
    # readlines() 方法用于读取os.popen(command)运行后，返回结果的的所有行，并以列表的形式返回结果
    result = os.popen(command).readlines()
    print('result:', result)
    # 将输出结果存入列表中
    gps_data = []
    for line in result:  # 读取返回结果
        stripped_line = line.strip()  # 使用 strip() 方法去除每一行的首尾空白字符
        # stripped_line不为空，则将其存入gps_data列表中
        if stripped_line:
            gps_data.append(stripped_line)

    # 这里需要对输出的内容进行处理
    start_tag = "Last Known Locations:"
    end_tag = "Last Known Locations Coarse Intervals:"
    # 设置start_index和end_index初始值为-1，表示还没有找到标记词
    start_index = -1
    end_index = -1
    # 遍历列表 result 中的每一行，enumerate(result)将result，转换为一个枚举对象，同时返回索引和对应的值，
    # i 表示当前元素的索引，line 表示当前元素的值
    for i, line in enumerate(gps_data):
        if start_tag in line:  # 查看该行是否有起始标记词
            start_index = i + 1  # 记录位置
        elif end_tag in line:  # 查看该行是否有结束标记词
            end_index = i  # 记录位置
            break  # 有则返回

    # 如果找到了起始标记词以及结束标记词
    if start_index != -1 and end_index != -1:
        locations = gps_data[start_index:end_index]  # 获取对应位置的内容
        # 对 locations 中的数据进行进一步处理，提取经纬度等信息
        # 返回处理后的位置信息列表
        print('未经处理的GPS的经纬度结果如下', locations)

        # 对得到的结果进行进一步处理
        # 查找 locations 列表中第一个包含 'fused' 字符串的元素，并将其赋值给 fused_location 变量
        # if 'fused' in x用来过滤出包含 'fused' 字符串的元素。
        fused_location = next((x for x in locations if 'fused' in x), None)
        if fused_location:
            # 从 fused_location 中提取经纬度信息
            # 用find（）查找'[fused'在字符串中的位置，再加上'[fused'的长度，即可得到经纬度的值的开始位置
            start_pos = fused_location.find('[fused') + len('[fused')
            end_pos = fused_location.find('acc')  # 经纬度结束位置
            coordinates = fused_location[start_pos:end_pos]  # 获取经纬度
            print('GPS的经纬度结果如下：', coordinates)

            # 得到处理好后的经纬度数据，可以使用命令来查找确切位置
            # 这条命令有一个要求，那就是需要安卓手机有可以处理 geo: Intent 的地图应用
            command = 'shell am start -a android.intent.action.VIEW -d "geo:{coordinates}"'
            out = send_adb_command(command)
            # print('GPS定位为:', out)
            return coordinates


# 获取当前手机的APP名称

def get_app_names():
    command = 'adb shell pm list packages'
    # 执行 command 命令，并将输出结果读取到 output 变量中，并去除其中的头部和尾部空格和换行符
    output = os.popen(command).readlines()

    app_names_data = []
    count = 0
    lines = []
    # 将 output 字符串按照换行符进行分割
    for line in output:
        stripped_line = line.strip()
        if stripped_line:
            lines.append(stripped_line)

    ##遍历line列表，找到符合条件的包名
    for line in lines:
        # 判断该行是否以 'package:com.android'开头
        if line.startswith('package:com.android'):
            # 因为这些包名每一行都有package:，这里需要去掉，通过 replace() 方法替换为空字符串，并使用 strip() 方法去除首尾的空白字符
            package_name = line.replace('package:', '')  # 去除 'package:' 字符串
            package_name = package_name.strip()  # 去除首尾空白字符
            app_names_data.append({'Package Name': package_name})

    # 将列表数据转换为一个 Pandas DataFrame 对象，以便保存在excle表中
    df = pd.DataFrame(app_names_data)

    # 将数据保存到 Excel 文件
    excel_file1 = 'app包名excle表'  # 文件名
    # df是上面包名数据，to_excel，是将数据保存到 Excel文件中，.xlsx表示保存为 Excel 格式的文件，index=False是去掉索引值
    df.to_excel(excel_file1 + '.xlsx', index=False)
    print(f"过滤后的应用名称已保存到 {excel_file1} 文件中。")
    return app_names_data


# 启动应用
def initiate_app():
    app_name = simpledialog.askstring("启动APP", "请输入要启动的APP的名称：")
    # 这里的APP名称，格式是com.android.xxx
    command = f'shell monkey -p {app_name} -c android.intent.category.LAUNCHER 1'
    send_adb_command(command)


# 关闭app
def close_app():
    app_name = simpledialog.askstring("关闭APP", "请输入要关闭的APP的名称：")
    # 这里的APP名称，格式是com.android.xxx
    command = f"shell am force-stop {app_name}"
    send_adb_command(command)


# 卸载app
def unload_app():
    app_name = simpledialog.askstring("卸载APP", "请输入要卸载的APP的名称：")
    command = f"uninstall {app_name}"
    send_adb_command(command)


# 下面是登录后的窗口
def Login_successful():
    new_window0 = tk.Toplevel(window)
    label = tk.Label(new_window0, text="使用界面")
    new_window0.geometry('300x300')
    label.grid()

    # 这里是对手机进行远程控制的窗口
    def Remote_control_window():
        new_window1 = tk.Toplevel(new_window0)
        label = tk.Label(new_window1, text="远程控制")
        new_window1.geometry('300x300')
        label.grid()

        # 返回函数
        def Remote_control_window():
            # 关闭当前窗口
            new_window1.destroy()
            # 打开 new_window0 窗口
            new_window0.deiconify()

        # 创建按钮并绑定对应的函数
        lock_screen_button = tk.Button(new_window1, text="锁定屏幕", command=lock_screen)
        # row=0 表示按钮所在的行索引为 0，column=0 表示按钮所在的列索引为 0
        # padx=10 和 pady=10 分别表示按钮与其他部件之间的水平和垂直间距为 10 像素
        lock_screen_button.grid(row=0, column=0, padx=10, pady=10)

        unlock_screen_button = tk.Button(new_window1, text="解锁屏幕", command=unlock_screen)
        unlock_screen_button.grid(row=0, column=10, padx=10, pady=10)

        turn_off_button = tk.Button(new_window1, text="关机", command=turn_off)
        turn_off_button.grid(row=2, column=0, padx=10, pady=10)

        turn_on_button = tk.Button(new_window1, text="开机", command=turn_on)
        turn_on_button.grid(row=2, column=10, padx=10, pady=10)

        disable_wifi_button = tk.Button(new_window1, text="关闭WiFi", command=disable_wifi)
        disable_wifi_button.grid(row=3, column=0, padx=10, pady=10)

        enable_wifi_button = tk.Button(new_window1, text="开启WiFi", command=enable_wifi)
        enable_wifi_button.grid(row=3, column=10, padx=10, pady=10)

        make_phone_call_button = tk.Button(new_window1, text="拨打电话", command=make_phone_call)
        make_phone_call_button.grid(row=4, column=0, padx=10, pady=10)

        browse_web_button = tk.Button(new_window1, text="浏览网页", command=browse_web)
        browse_web_button.grid(row=4, column=10, padx=10, pady=10)

        take_screenshot_button = tk.Button(new_window1, text="截屏", command=take_screenshot)
        take_screenshot_button.grid(row=5, column=0, padx=10, pady=10)

        light_up_button = tk.Button(new_window1, text="手机亮屏", command=light_up)
        light_up_button.grid(row=5, column=1, padx=10, pady=10)

        Swipe_the_screen_button = tk.Button(new_window1, text="手机滑屏", command=Swipe_the_screen)
        Swipe_the_screen_button.grid(row=5, column=2, padx=10, pady=10)

        return_button = tk.Button(new_window1, text="返回", command=Remote_control_window)
        return_button.grid(row=6, column=0, padx=10, pady=10)

    # 这里是对手机进行定位的窗口
    def Position_the_window():
        new_window2 = tk.Toplevel(new_window0)
        label = tk.Label(new_window2, text="对手机进行定位")
        new_window2.geometry('300x300')
        label.grid()

        # 返回函数
        def Remote_control_window1():
            # 关闭当前窗口
            new_window2.destroy()

            # 打开 new_window0 窗口
            new_window0.deiconify()

        # 定义点击按钮后的事件处理函数
        def display_result():
            # 调用运行代码的函数，获取结果
            result = get_gps_location()

            # 在文本框中显示结果
            text_box.insert(tk.END, f'GPS的经纬度结果如下: {result}')

        open_gps_location_button = tk.Button(new_window2, text="打开GPS定位", command=open_gps_location)
        open_gps_location_button.grid(row=0, column=0, padx=10, pady=10)

        take_screenshot_button = tk.Button(new_window2, text="开启手机定位", command=display_result)
        take_screenshot_button.grid(row=1, column=0, padx=10, pady=10)

        return_button = tk.Button(new_window2, text="返回", command=Remote_control_window1)
        return_button.grid(row=2, column=0, padx=10, pady=10)

        # 创建文本框组件
        text_box = tk.Text(new_window2, height=10, width=30)
        text_box.grid(row=1, column=1, padx=10, pady=10)

    # 这是要对手机APP进行管理的窗口
    def app_control():
        new_window3 = tk.Toplevel(new_window0)
        label = tk.Label(new_window3, text="对手机进行定位板")
        new_window3.geometry('300x300')
        label.grid()

        # 返回函数
        def Remote_control_window2():
            # 关闭当前窗口
            new_window3.destroy()
            # 打开 new_window0 窗口
            new_window0.deiconify()

        get_app_names_button = tk.Button(new_window3, text="获取app名称", command=get_app_names)
        get_app_names_button.grid(row=0, column=0, padx=10, pady=10)

        initiate_app_button = tk.Button(new_window3, text="启动app", command=initiate_app)
        initiate_app_button.grid(row=0, column=1, padx=10, pady=10)

        close_app_button = tk.Button(new_window3, text="关闭app", command=close_app)
        close_app_button.grid(row=1, column=0, padx=10, pady=10)

        unload_app_button = tk.Button(new_window3, text="卸载app", command=unload_app)
        unload_app_button.grid(row=1, column=1, padx=10, pady=10)

        take_screenshot_button = tk.Button(new_window3, text="截屏", command=take_screenshot)
        take_screenshot_button.grid(row=2, column=0, padx=10, pady=10)

        return_button = tk.Button(new_window3, text="返回", command=Remote_control_window2)
        return_button.grid(row=3, column=0, padx=10, pady=10)

    # 下面是设置跳转远程控制页面的按钮
    Remote_control_button = tk.Button(new_window0, text="远程控制", command=Remote_control_window)
    Remote_control_button.grid(row=0, column=0, padx=10, pady=10)

    # 下面是对跳转手机定位页面的按钮
    Position_button = tk.Button(new_window0, text="手机定位", command=Position_the_window)
    Position_button.grid(row=0, column=10, padx=10, pady=10)

    # 这里是跳转APP管理页面的窗口
    app_control_button = tk.Button(new_window0, text="APP管理", command=app_control)
    app_control_button.grid(row=2, column=0, padx=10, pady=10)


window.mainloop()












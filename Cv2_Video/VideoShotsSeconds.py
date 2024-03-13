import base64
import os
import cv2


def encode_image(image_path, output_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        encode_data = base64.b64encode(image_data)
        with open(output_path, 'w') as output_file:
            output_file.write(encode_data.decode('utf-8'))

def decode_image(encode_path, output_path):
    with open(encode_path, 'r') as encode_file:
        encode_data = encode_file.read()
        image_data = base64.b64decode(encode_data)
        with open(output_path, 'wb') as output_file:
            output_file.write(image_data)



# video_path = 'D:\\file\\test\\'  # 视频所在的路径
# f_save_path = 'D:\\file\\保存\\'  # 保存图片的上级目录

def cut_video(video_path, f_save_path, time_interval):  # 截取视频中图片
    mask = 2  # 不同方法：1 按照帧率截取；2 按照时间截取(单位：s)；
    frame_interval = 2  # 设置帧率间隔
      # 设置时间间隔(单位：s)

    if mask==1:
        print("当前模式：按照帧率截取视频\n帧率间隔：" + str(frame_interval))
    elif mask==2:
        print("当前模式：按照时间截取视频\n时间间隔：" + str(time_interval) + "s")

    for root, dirs, files in os.walk(video_path):
        if not files:
            print('*****************文件夹为空*****************')
            return False
        else:
            fm = ['.mp4']
            # 获取列表中符合条件的字符串
            elem = list(filter(lambda text: all([word in text for word in fm]), files))
            print(elem)
            if elem:
                videos = os.listdir(video_path)
                for video_name in videos:
                    file_name = video_name.split('.')[0]  # 拆分视频文件名称 ，剔除后缀
                    folder_name = f_save_path + file_name  # 保存图片的上级目录+对应每条视频名称 构成新的目录存放每个视频
                    os.makedirs(folder_name, exist_ok=True)  # 创建存放视频的对应目录
                    vc = cv2.VideoCapture(video_path + video_name)  # 读入视频文件
                    fps = vc.get(cv2.CAP_PROP_FPS)  # 获取当前视频帧率
                    rval = vc.isOpened()  # 判断视频是否打开
                    print(video_path + video_name)
                    c = 1
                    while rval:  # 循环读取视频帧
                        rval, frame = vc.read()  # videoCapture.read() 函数，第一个返回值为是否成功获取视频帧，第二个返回值为返回的视频帧；
                        pic_path = folder_name + '/'
                        if rval:
                            if mask == 1:
                                if c % round(frame_interval) == 0:  # 每隔frame_interval帧存储一次

                                    cv2.imencode('.jpg', frame)[1].tofile(
                                        pic_path + file_name + '_' + str(round(c / frame_interval)) + '.jpg')  # 中文路径也可以保存

                                    # print(file_name + '_' + str(round(c / frame_interval)) + '.jpg')
                                cv2.waitKey(1)
                                c = c + 1
                            elif mask == 2:
                                if c % (round(fps) * time_interval) == 0:  # 每隔time_interval秒存储一次
                                    cv2.imencode('.jpg', frame)[1].tofile(
                                        pic_path + file_name + '_' + str(round(c / fps)) + '.jpg')
                                    print(file_name + '_' + str(round(c / fps)) + '.jpg')
                                cv2.waitKey(1)
                                c = c + 1
                        else:
                            break
                    vc.release()
                    print('save_success: ' + folder_name)
                return True
            else:
                print('*****************文件夹内没有MP4文件*****************')
                return False


























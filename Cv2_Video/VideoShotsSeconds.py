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



def cut_video(video_path, f_save_path, time_interval):  # 截取视频中图片
    mask = 2
    frame_interval = 2

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
                    file_name = video_name.split('.')[0]
                    folder_name = f_save_path + file_name
                    os.makedirs(folder_name, exist_ok=True)
                    vc = cv2.VideoCapture(video_path + video_name)
                    fps = vc.get(cv2.CAP_PROP_FPS)
                    rval = vc.isOpened()
                    print(video_path + video_name)
                    c = 1
                    while rval:
                        rval, frame = vc.read()
                        pic_path = folder_name + '/'
                        if rval:
                            if mask == 1:
                                if c % round(frame_interval) == 0:
                                    cv2.imencode('.jpg', frame)[1].tofile(
                                        pic_path + file_name + '_' + str(round(c / frame_interval)) + '.jpg')


                                cv2.waitKey(1)
                                c = c + 1
                            elif mask == 2:
                                if c % (round(fps) * time_interval) == 0:
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


























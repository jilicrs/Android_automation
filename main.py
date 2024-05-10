from alive_progress import alive_bar
import time



def file_Byte_comparison(file_1, file_2):
    with open(file_1, 'rb') as f1, open(file_2, 'rb') as f2:
        byte1 = f1.read(1)
        byte2 = f2.read(1)
    if byte1 == byte2:
        result = True
    else:
        result = False

    print(result)
    return result


def progress_bar():
    with alive_bar(100, force_tty=True) as bar:
        for i in range(100):
            time.sleep(0.01)
            bar(1)


if __name__ == '__main__':
    # file_Byte_comparison(input('文件1路径：'), input('对比文件2路径：'))

    progress_bar()






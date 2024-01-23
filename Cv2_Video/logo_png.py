import base64

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


if __name__ == '__main__':
    encode_image('D:\\Android automation\\Cv2_Video\\logo.png',
                 'D:\\Android automation\\Cv2_Video\\encode.txt')
    decode_image('D:\\Android automation\\Cv2_Video\\encode.txt',
                 'D:\\Android automation\\Cv2_Video\\decode.png')

















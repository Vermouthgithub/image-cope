import cv2
import os


def io_img(image_path):
    i = 0
    for fileName in os.listdir(os.path.abspath(image_path)):
        fileFirstName = fileName.split('.')[0]
        img = image_path +fileFirstName + '.jpg'
        img = cv2.imread(img)
        cv2.imwrite(image_path + fileFirstName + '.jpg', img)
        i += 1
    print(i)


if __name__ == '__main__':
    img_path = './images/'
    io_img(img_path)

import os
import random
from pip._vendor.distlib._backport import shutil


def get_test_img(img_path, path, data_path):
    result_list = []
    for fileName in os.listdir(os.path.abspath(img_path)):
        result_list.append(fileName)
    max_num = len(result_list)
    print(max_num)
    list_offset = random.sample(range(0, max_num), 10)
    for offset in list_offset:
        use_file = result_list[offset]
        shutil.copy(os.path.join(img_path, use_file), path + data_path + '/test_img')
    # for imgName in os.listdir(os.path.abspath(path + data_path + '/test_img')):
    #     print(imgName)


if __name__ == '__main__':
    path = './test/'
    path_list = os.listdir(os.path.abspath(path))
    for data_path in path_list:
        img_path = path + data_path + '/images'
        os.mkdir(path + data_path + '/test_img')
        if os.path.isdir(img_path):
            get_test_img(img_path, path, data_path)
        else:
            print("error path")

    for data_path in path_list:
        shutil.move(path + data_path + '/test_img', path + '/test_img/' + data_path + '/test_img')


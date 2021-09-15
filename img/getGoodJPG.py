import os
import shutil

from pip._vendor.distlib.compat import raw_input

def remove(path1,path2):
    for fileName in os.listdir(os.path.abspath(path1)):
        if fileName in os.listdir(os.path.abspath(path2)):
            shutil.move(path1+'\\'+fileName, 'C:\\Users\\XX\\Desktop\\linshi')


if __name__ == '__main__':
    path1 = raw_input('input the allData path:')
    path2 = raw_input('input the removeData path:')


    if os.path.isdir(path1) and os.path.isdir(path2):
        remove(path1, path2)
    else:
        print("error path")

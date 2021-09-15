import string
import os
import sys
import xml.dom.minidom
from warnings import catch_warnings
import re
from pip._vendor.distlib._backport import shutil


if __name__ == '__main__':

    path1 = './ImageSets/Main/test.txt'

    trainfile = open(path1)
    lines = trainfile.read().splitlines()
    print(len(lines))
    for line in lines:
        fileName = line+'.jpg'
        shutil.move(os.path.join('./images', fileName), os.path.join('./test_dir/images', fileName))
        fileName = line+'.xml'
        shutil.move(os.path.join('./Annotations', fileName), os.path.join('./test_dir/Annotations', fileName))
    trainfile.close()
    

    



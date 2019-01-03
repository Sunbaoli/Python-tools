#coding:utf-8
import cv2
import scipy.stats as st
import os
import numpy as np
from PIL import Image
import time
import scipy
from scipy import misc
import scipy.misc
from glob import glob
import numpy as np
from six.moves import xrange
import scipy.io as sio

def mkdir(paths):
    if not isinstance(paths, (list, tuple)):
        paths = [paths]
    for path in paths:
        if not os.path.isdir(path):
            os.makedirs(path)


train_dataset = './color_png_train/'
train_data = sorted(glob(os.path.join(
                train_dataset, "*.png")))
#print(depth_data)
mkdir('./color_train_HR_x8_256')


for filename in train_data:
    
    i = int(filename.split('/')[-1].split('.')[0])
    print(i,'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

    img = cv2.imread(filename)

    img_w = img.shape[1]
    img_h = img.shape[0]
    # print(img_w,img_h,img_w-96,img_h-96,i)
    stride = 20
    h = 256
    w = 256
    x = 0
    y =0
    count = 1
    for y in range(0,img_h-h-1,stride):
        # while x <= (img_w-w):
        for x in range(0,img_w-w-1,stride):
            crop_img = img[(y):(y+h),(x):(x+w)]
            print(crop_img.shape)
            print(x,y,i)
            if crop_img.shape[0]==h and crop_img.shape[1]==w:
                cv2.imwrite('color_train_HR_x8_256/'+ str(i) + '_'+ str(count) +'.png', crop_img)
            # y+=stride
            x+=stride
            count+=1

import cv2
import os
from glob import glob
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


rgb_file = '/home/sunbaoli/DBPN-Pytorch/data/color_png_train/'
d_file = '/home/sunbaoli/DBPN-Pytorch/data/train/png_train/'
def mkdir(paths):
    if not isinstance(paths, (list, tuple)):
        paths = [paths]
    for path in paths:
        if not os.path.isdir(path):
            os.makedirs(path)
mkdir('./train_rgb')
mkdir('./train_d')

rgb_data = sorted(glob(os.path.join(rgb_file, "*.png")))
d_data = sorted(glob(os.path.join(d_file,"*.png")))

for filename_rgb in rgb_data:
    for filename_d in d_data:
        i = int(filename_rgb.split('/')[-1].split('.')[0])
        j = int(filename_d.split('/')[-1].split('.')[0])
        if i==j:
            img1 = cv2.imread(filename_rgb)
            img2 = cv2.imread(filename_d,0)
#####
            img1_w = img1.shape[1]
            img1_h = img1.shape[0]

            img2_w = img2.shape[1]
            img2_h = img2.shape[0]
                # print(img_w,img_h,img_w-96,img_h-96,i)
            stride = 20
            h = 256
            w = 256
            x = 0
            y =0
            count1 = 1
            for y in range(0,img1_h-h-1,stride):
            # while x <= (img_w-w):
                for x in range(0,img1_w-w-1,stride):
                    crop_img1 = img1[(y):(y+h),(x):(x+w)]
                    print(crop_img1.shape)
                    print(x,y,i)
                    if crop_img1.shape[0]==h and crop_img1.shape[1]==w:
                        cv2.imwrite('train_rgb/'+ str(i) + '_'+ str(count1) +'.png', crop_img1)
            # y+=stride
                    x+=stride
                    count1+=1

            x2 = 0
            y2 = 0
            count2 =1
            for y2 in range(0,img2_h-h-1,stride):
            # while x <= (img_w-w):
                for x2 in range(0,img2_w-w-1,stride):
                    crop_img2 = img2[(y2):(y2+h),(x2):(x2+w)]
                    print(crop_img2.shape)
                    print(x2,y2,j)
                    if crop_img2.shape[0]==h and crop_img2.shape[1]==w:
                        cv2.imwrite('train_d/'+ str(j) + '_'+ str(count2) +'.png', crop_img2)
            # y+=stride
                    x2+=stride
                    count2+=1 
#####

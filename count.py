#coding:utf-8
import cv2
import os
import scipy.misc
from glob import glob


dataset = './train_rgbd_32'
data = sorted(glob(os.path.join(
                dataset, "*.png")))
count = 1
for filename in data:
    #i = filename.split('/')[-1].split('.')[0]
    #print(i,'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    #img = cv2.imread(filename,0)
    #print(img.shape)
    count+=1
print(count)

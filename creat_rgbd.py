import cv2
import os
from glob import glob
import numpy as np


rgb_file = '/home/sunbaoli/DBPN-Pytorch/new/train_rgb_32/'
d_file = '/home/sunbaoli/DBPN-Pytorch/new/train_d_32/'
def mkdir(paths):
    if not isinstance(paths, (list, tuple)):
        paths = [paths]
    for path in paths:
        if not os.path.isdir(path):
            os.makedirs(path)
mkdir('./train_rgbd_32')


rgb_data = sorted(glob(os.path.join(rgb_file, "*.png")))
d_data = sorted(glob(os.path.join(d_file,"*.png")))

for filename_rgb in rgb_data:
    for filename_d in d_data:
        i = filename_rgb.split('/')[-1].split('.')[0]
        j = filename_d.split('/')[-1].split('.')[0]
        if i==j:
            img_rgb = cv2.imread(filename_rgb)
            img_d = cv2.imread(filename_d,0)

            img_rgb = np.array(img_rgb)
            img_d = np.array(img_d)

            w = img_d.shape[0]
            h = img_d.shape[1]

            img_rgbd = np.zeros((w,h,4),dtype=np.uint8)####???
            img_rgbd[:, :, 0] = img_rgb[:, :, 0]
            img_rgbd[:, :, 1] = img_rgb[:, :, 1]
            img_rgbd[:, :, 2] = img_rgb[:, :, 2]
            img_rgbd[:, :, 3] = img_d

            cv2.imwrite('train_rgbd_32/'+ i +'.png', img_rgbd)
            print(img_rgbd.shape)

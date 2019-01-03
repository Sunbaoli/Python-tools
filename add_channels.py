import cv2
import os
from glob import glob
import numpy as np



d_file = '/home/sunbaoli/DBPN-Pytorch/new/data/testx8/'

def mkdir(paths):
    if not isinstance(paths, (list, tuple)):
        paths = [paths]
    for path in paths:
        if not os.path.isdir(path):
            os.makedirs(path)
mkdir('./test_4channels')

d_data = sorted(glob(os.path.join(d_file,"*.png")))

for filename_d in d_data:
    i = filename_d.split('/')[-1].split('.')[0]
    img_d = cv2.imread(filename_d,0)
    img_d = np.array(img_d)
    w = img_d.shape[0]
    h = img_d.shape[1]
    
    img_4channels = np.zeros((w,h,4),dtype=np.uint8)
    img_4channels[:, :, 3] = img_d

    cv2.imwrite('test_4channels/' + i + '.png',img_4channels)
    print(img_4channels.shape)

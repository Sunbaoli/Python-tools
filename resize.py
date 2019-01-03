import scipy.stats as st
import os
import numpy as np
from PIL import Image
import time
import scipy
from scipy import misc
import scipy.misc
from glob import glob
#import tensorflow as tf
import numpy as np
from six.moves import xrange
import scipy.io as sio
import cv2

def mkdir(paths):
    if not isinstance(paths, (list, tuple)):
        paths = [paths]
    for path in paths:
        if not os.path.isdir(path):
            os.makedirs(path)


depth_dataset = './train_rgb'
depth_data = sorted(glob(os.path.join(
                depth_dataset, "*.png")))
#print(depth_data)
mkdir('./train_rgb_32')


for filename in depth_data:
    
    #i = int(filename.split('/')[-1].split('.')[0])
    i = filename.split('/')[-1].split('.')[0]
    print(i)

    
    img = cv2.imread(filename)
    print(img.shape) 
    height, width = img.shape[:2]
    size = (int(width*0.125), int(height*0.125))
    shrink = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)
    print(shrink.shape)
    cv2.imwrite('train_rgb_32/'+ str(i) + '.png',shrink)


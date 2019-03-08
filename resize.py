import os
from glob import glob
import cv2
# make dir
def mkdir(paths):
    if not isinstance(paths, (list, tuple)):
        paths = [paths]
    for path in paths:
        if not os.path.isdir(path):
            os.makedirs(path)
mkdir('./train_rgb_32')

#dataset
dataset_dir = './train_rgb'
data = sorted(glob(os.path.join(
                dataset_dir, "*.png")))

for filename in data:    
    #i = int(filename.split('/')[-1].split('.')[0])
    i = filename.split('/')[-1].split('.')[0]
# read iamge
    img = cv2.imread(filename) 
    height, width = img.shape[:2]
#resize   
    size = (int(width*0.125), int(height*0.125))
    shrink = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)
#save image
    cv2.imwrite('train_rgb_32/'+ str(i) + '.png',shrink)


import os
from glob import glob
import cv2
import numpy as np
from PIL import Image
import scipy.io as scio
import matplotlib.pyplot as plt

def mkdir(paths):

    if not isinstance(paths, (list, tuple)):
        paths = [paths]
    for path in paths:
        if not os.path.isdir(path):
            os.makedirs(path)


def resize(input_dir, scale):

    dataset_dir = input_dir
    data = sorted(glob(os.path.join(input_dir, "*.png")))
    for filename in data:
        # i = int(filename.split('/')[-1].split('.')[0])
        i = filename.split('/')[-1].split('.')[0]
        # read iamge
        img = cv2.imread(filename)
        height, width = img.shape[:2]
        print(height, width)
        # resize
        size = (int(width * scale), int(height * scale))
        print(size)
        shrink = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)
        #print(shrink.size())
        # save image
        cv2.imwrite(str(i) + '.png', shrink)


def slide_crop(input_dir, scale_h, scale_w, input_stride):

    dataset_dir = input_dir
    data = sorted(glob(os.path.join(dataset_dir, "*.png")))
    for filename in data:
        i = int(filename.split('/')[-1].split('.')[0])
        img = cv2.imread(filename)
        img_w = img.shape[1]
        img_h = img.shape[0]

        stride = input_stride
        h = scale_h
        w = scale_w
        x = 0
        y =0
        count = 1
        for y in range(0,img_h-h-1,stride):
            for x in range(0,img_w-w-1,stride):
                crop_img = img[(y):(y+h),(x):(x+w)]
                #print(crop_img.shape)
                #print(x,y,i)
                if crop_img.shape[0]==h and crop_img.shape[1]==w:
                    cv2.imwrite( str(i) + '_'+ str(count) +'.png', crop_img)
                x+=stride
                count+=1
        print('p', str(i), " totol resize'iamge: ",count-1)


def creat_rgbd_4channels(rgb_dir, d_dir):

    rgb_file = rgb_dir
    d_file = d_dir
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

                img_rgbd = np.zeros((w,h,4),dtype=np.uint8)
                img_rgbd[:, :, 0] = img_rgb[:, :, 0]
                img_rgbd[:, :, 1] = img_rgb[:, :, 1]
                img_rgbd[:, :, 2] = img_rgb[:, :, 2]
                img_rgbd[:, :, 3] = img_d

                cv2.imwrite(i +'.png', img_rgbd)
                print(img_rgbd.shape)


def MatrixToImage(data):
    data = data*255
    new_im = Image.fromarray(data.astype(np.uint8))
    return new_im
def matToimage(mat_dir, mat_variable):

    folder = mat_dir
    path = os.listdir(folder)

    for each_mat in path:
        if each_mat == '.DS_Store':
            pass
        else:
            first_name, second_name = os.path.splitext(each_mat)
            each_mat = os.path.join(folder, each_mat)
            array_struct = scio.loadmat(each_mat)

            array_data = array_struct[mat_variable]
            new_im = MatrixToImage(array_data)
            #plt.imshow(array_data, cmap=plt.cm.gray, interpolation='nearest')
            #new_im.show()
            new_im.save(first_name + '.png')

def count_image(input_dir):

    data_dir = input_dir
    data = sorted(glob(os.path.join(
                data_dir, "*.png")))
    count = 1
    for filename in data:
        count+=1
    print(data_dir, 'has', count-1, 'images!')


#coding:utf-8
#一，加载或读取图片的方法与保存图片的方法
#1，cv2
import cv2
from glob import glob
depth_dataset = './train_256'
depth_data = sorted(glob(os.path.join(
                depth_dataset, "*.png")))
for filename in depth_data:
    img = cv2.imread(filename,0)#第二个参数0是读为灰度，没有（defualt）为rgb

	cv2.imwrite('train_32/'+ str(i) + '.png',img)

#2，Image
from PIL import Image
train_dataset = './all_mpimid/'
train_data = sorted(glob(os.path.join(
                train_dataset, "*.png")))
for filename in train_data:
	img = Image.open(filename)
	foamat = img.format()# 图像的格式png，gif。。。
	model = img.mode()#图像的模式“1”，“L”，“RGB”或“CMYK”
	img.size()#图像的尺寸。二元组宽高

	img = Image.fromarray(img, mode='RGB')
    img.save(path_and_name)

#二，图像resize
	img = cv2.imread(filename,0) 
    height, width = img.shape[:2]
    size = (int(width*0.125), int(height*0.125))
    shrink = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('train_0306_32/'+ str(i) + '.png',shrink)

#三，图像裁剪
img = cv2.imread(filename)
img_crop = img[h:h+d, w:w+d]

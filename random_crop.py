#coding:utf-8
import cv2
import random

#read image
img = cv2.imread('./depth_png_train/38.png')

#h is the height, w is the width
h = 256
w = 256

count = 961
while 1:
	x = random.randint(1,img.shape[1])
	y = random.randint(1,img.shape[0])
	if(x<(img.shape[1]-h) and y<(img.shape[0]-w)):
		print(x,y)
		corpimg = img[(y):(y+h),(x):(x+w)]
		cv2.imwrite('pic256/'+ str(count) + '.png',corpimg)
		count+=1

	if count==1001:
		break

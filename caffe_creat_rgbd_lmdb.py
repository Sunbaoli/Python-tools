import numpy as np
import lmdb
from PIL import Image
import sys
 
# import caffe module
caffe_root = '/data1/mcs/other/WaterGAN-color-correction-net/'
sys.path.insert(0, caffe_root + 'python')
import caffe
 
# # read file
train_file = open('/data1/mcs/other/WaterGAN-color-correction-net/myfile/RGBD_code/rgbd.txt')
inputs_data_train = train_file.readlines()
train_file.close()
 
print("Creating Training Data LMDB File ..... ")
in_db = lmdb.open('/data1/mcs/other/WaterGAN-color-correction-net/myfile/build_lmdb/train_rgbd_lmdb', map_size=int(1e12))
with in_db.begin(write=True) as in_txn:
    for in_idx, in_ in enumerate(inputs_data_train):
        # print in_idx
        in_ = in_.strip()
        im = np.array(Image.open(in_))
        Dtype = im.dtype
        if im.shape[2]== 3:
            print('The image has 3 channel')
            # RGB to BGR
            im = im[:, :, ::-1]
        if im.shape[2]==4:
            print('The image has 4 channels')
            im3 = im[:,:,0:3]
            im3 = np.array(im3)
            #RGB to BGR
            im3 = im3[:,:,::-1]
            im[:, :, 0] = im3[:, :, 0]
            im[:, :, 1] = im3[:, :, 1]
            im[:, :, 2] = im3[:, :, 2]
        im = Image.fromarray(im)
        im = np.array(im, Dtype)
        im = im.transpose((2, 0, 1))
        im_dat = caffe.io.array_to_datum(im)
        in_txn.put('{:0>10d}'.format(in_idx), im_dat.SerializeToString())
in_db.close()
 
print("Finish creating lmdb file ......")

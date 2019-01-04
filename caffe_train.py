#!/usr/bin/env python
import os, sys
import subprocess

caffe_bin = '/data1/mcs/other/WaterGAN-color-correction-net/.build_release/tools/caffe'
#'/data8T/slchen/WaterGAN-color-correction-net/.build_release/tools/caffe'

# =========================================================

if not os.path.isfile(caffe_bin):
    print('Caffe tool binaries not found. Did you compile caffe with tools (make all tools)?')
    sys.exit(1)

print('args:', sys.argv[1:])

args = [caffe_bin, 'train', '-solver', '/data1/mcs/other/WaterGAN-color-correction-net/myfile/solver.prototxt','-gpu', '0'] + sys.argv[1:]
cmd = str.join(' ', args)
print('Executing %s' % cmd)

subprocess.call(args)


#'-model','/data1/mcs/other/WaterGAN-color-correction-net/myfile/caffemodel/depth-estimation-mhl.caffemodel',

import os
import re

path_train = "E:\\水下数据集1029\\darkgreen\\water"  # 建议是用绝对路径
path_val = "val文件夹路径"
path_label = "E:\\水下数据集1029\\darkgreen\\in-air"
if not os.path.exists(path_train):
    print("path_train not exist!!!")
else:
    print("path_train exist!!!")

if not os.path.exists(path_val):
    print("path_val not exist!!!")
else:
    print("path_val exist!!!")

file_train = open('E:\\水下数据集1029\\darkgreen\\train.txt', 'wt')
#file_val = open('val.txt', 'wt')

file_train.truncate()
#file_val.truncate()

pa = r".+(?=\.)"
pattern = re.compile(pa)

print("now,creating train.txt...")

for (filename, labelname) in zip(os.listdir(path_train), os.listdir(path_label)):
    train_abspath = os.path.join(path_train, filename)
    label_abspath = os.path.join(path_label, labelname)
    file_train.write(train_abspath + ' ' + label_abspath + '\n')

print("function over!!!")

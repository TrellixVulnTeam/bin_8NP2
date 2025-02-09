#!/usr/bin/env python
# https://blog.csdn.net/Houchaoqun_XMU/article/details/79624329
# -*- coding: utf-8 -*-
 
 
from PIL import Image
import struct
 
 
def read_image(filename):
    f = open(filename, 'rb')
    index = 0
    buf = f.read()
    f.close()
 
    magic, images, rows, columns = struct.unpack_from('>IIII' , buf , index)
    index += struct.calcsize('>IIII')
 
    # xrange has become range in python 3
    for i in range(images):
        # for i in xrange(2000):
        # 创建一张空白的图片，其中的’L’代表这张图片是灰度图
        image = Image.new('L', (columns, rows))
        for x in range(rows):
            for y in range(columns):
                image.putpixel((y, x), int(struct.unpack_from('>B', buf, index)[0]))
                index += struct.calcsize('>B')
    
        print('save ' + str(i) + ' image')
        image.save('test_data/' + str(i) + '.png')
 
 
def read_label(filename, saveFilename):
    f = open(filename, 'rb')
    index = 0
    buf = f.read()
    
    f.close()
 
    magic, labels = struct.unpack_from('>II' , buf , index)
    index += struct.calcsize('>II')
  
    labelArr = [0] * labels
     #labelArr = [0] * 2000
 
 
    for x in range(labels):
    #for x in xrange(2000):
        labelArr[x] = int(struct.unpack_from('>B', buf, index)[0])
        index += struct.calcsize('>B')
 
    save = open(saveFilename, 'w')
 
    save.write(','.join(map(lambda x: str(x), labelArr)))
    save.write('\n')
 
    save.close()
    print('save labels success')
 
 
if __name__ == '__main__':
    read_image('t10k-images.idx3-ubyte')
    read_label('t10k-labels.idx1-ubyte', 'test_data/label.txt')

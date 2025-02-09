#!/usr/bin/env python3

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

annFile='instances_val2017.json'

# 初始化标注数据的 COCO api 
coco=COCO(annFile)

# display COCO categories and supercategories
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))

nms = set([cat['supercategory'] for cat in cats])
#print(nms, len(nms))
print('COCO supercategories: \n{}'.format(' '.join(nms)))

def loadCats(self, ids=[]):
    """
    Load cats with the specified ids.
    :param ids (int array)       : integer ids specifying cats
    :return: cats (object array) : loaded cat objects
    """
    if _isArrayLike(ids):
        return [self.cats[id] for id in ids]
    elif type(ids) == int:
        return [self.cats[ids]]

# get all images containing given categories, select one at random
catIds = coco.getCatIds(catNms=['person','dog','skateboard']);
imgIds = coco.getImgIds(catIds=catIds );
#imgIds = coco.getImgIds(imgIds = [324158])
imgIds = coco.getImgIds(imgIds = [324158])
# loadImgs() 返回的是只有一个元素的列表, 使用[0]来访问这个元素
# 列表中的这个元素又是字典类型, 关键字有: ["license", "file_name", 
#  "coco_url", "height", "width", "date_captured", "id"]
img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
print('img: ', img, img['id'])
print('catIds: ', catIds)

# 加载并显示图片,可以使用两种方式: 1) 加载本地图片, 2) 在线加载远程图片
# 1) 使用本地路径, 对应关键字 "file_name"
#I = io.imread('%s/images/%s/%s'%(dataDir,dataType,img['file_name']))  
I = io.imread('000000324158.jpg')  

# 2) 使用 url, 对应关键字 "coco_url"
#I = io.imread(img['coco_url'])        
#plt.axis('off')
#plt.imshow(I)
#plt.show()

# 加载并显示标注信息
plt.imshow(I); plt.axis('off')
#annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
print('annIds: ', annIds)
anns = coco.loadAnns(annIds)
print('anns: ', anns[0], type(anns[0]))
coco.showAnns([anns[0]])
plt.show()


#coco_caps=COCO(annFile)
# 加载并打印 caption 标注信息
#annIds = coco_caps.getAnnIds(imgIds=img['id']);
#anns = coco_caps.loadAnns(annIds)
#coco_caps.showAnns(anns)
#plt.imshow(I); plt.axis('off'); plt.show()

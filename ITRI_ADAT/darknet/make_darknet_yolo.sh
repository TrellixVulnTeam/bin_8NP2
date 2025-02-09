#!/bin/bash

darknet='/home/hugh/pkg/local/darknet_yolov3_cuda10/darknet'
workdir='./'

num_class=3
num_anchor=9
num_yolo_layer=3
filter=`echo $num_class+4+1 | bc`
filters=`echo '('"$num_anchor"'/'"$num_yolo_layer"')*'"$filter" | bc`

cd $workdir
mkdir backup
cp ~/bin/ITRI_ADAT/darknet/train.sh .
cp -r ~/bin/ITRI_ADAT/darknet/cfg .
cp -r ~/bin/ITRI_ADAT/darknet/data .

sed -i 's/num_class/'"$num_class"'/g' cfg/yolov3.cfg
sed -i 's/num_filters/'"$filters"'/g' cfg/yolov3.cfg
sed -i 's/num_class/'"$num_class"'/g' cfg/adat.data

sed -i 's/num_class/'"$num_class"'/g' cfg/yolov3_test.cfg
sed -i 's/num_filters/'"$filters"'/g' cfg/yolov3_test.cfg

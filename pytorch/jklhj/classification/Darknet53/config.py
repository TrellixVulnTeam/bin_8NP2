#!/urs/bin/env python3
from torchvision import transforms as T

class DefaultConfig():
    
    use_gpu = True 
    num_workers = 2
    num_classes = 2

    input_size = 32

    normalize = T.Normalize(mean=[0.503285495691, 0.451637785218, 0.467750980149],
                             std=[0.151216848168, 0.139701434141, 0.153258293707])
    
    # for training setting
    train_gpu_id = 0
    pretrained = False
    load_model = ''
    train_dir = '/home/hugh/tmp/train_data'
#    train_dir = '/mnt/sdc1/work/kaggle/Aerial_Cactus_Identification/train_data'
    train_batch_size = 8
    base_lr = 0.001
    lr_decay_step = 120
    max_epoch = 300
    show_iter = 50 
    save_iter = 200000

    # for validation setting
    val_in_train = True
    val_gpu_id = 0
#    val_dir   = '/home/hugh/Dropbox/tmp-PC/pytorch/val_data'
    val_dir   = '/home/hugh/tmp/val_data'
    val_model = 'Darknet53-iter5.pth'
    val_iter = 50
    val_batch_size = 1

    # for testing setting
    test_gpu_id = 0
    test_model = 'ResNet152-iter150000.pth'
#    test_dir  = '/home/hugh/Dropbox/tmp-PC/pytorch/test'
    test_dir  = '/home/jklhj/Dropbox/tmp-PC/pytorch/test'
    title_output = 'id,has_cactus'


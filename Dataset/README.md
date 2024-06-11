## Preparing Datasets

We provide the processed and labeled data. Please download [This](https://outlookuga-my.sharepoint.com/:f:/g/personal/fl79416_uga_edu/EhtmuP6IOTpErtRhcVR3s-oBegeA4cOb46Bkpel6eyMDFg?e=C1dewu).  
For the labels, please note that there are two folders named `labels_classification` and `labels_living_detection`. You should use them accordingly and not use them together. The labels are built in YOLO format, so if you want to use any other format, please adjust as needed. 

### Folder structure
In general, we need to create datasets following the structures below

    datasets
    │   README.md
    └───Ground_truth_jpg
    │       | chaeto_1.jpg
    |       | chaeto_2.jpg
    │       │   ...
    |   
    └───Marine_3_depths
    |       └───Marine_yolo_10m_only
    │           └───images
    │               └───train
    │                   |train_images.jpg
    │                   │   ...
    │               └───test
    │                   |test_images.jpg
    │                   │   ...
    │           └───labels
    │               └───train
    │                   |train_label.txt
    │                   │   ...
    │               └───test
    │                   |test_label.txt
    │                   │   ...    │           
    |       └───Marine_yolo_25m_only
    |       └───Marine_yolo_35m_only
    |        ...
    └───Video
    |       └───images
    │           └───train
    │               |train_images.jpg
    │               │   ...
    │           └───test
    │               |test_images.jpg
    │               │   ...
    │       └───labels
    │           └───train
    │               |train_label.txt
    │               │   ...
    │           └───test
    │               |test_label.txt
    │               │   ...


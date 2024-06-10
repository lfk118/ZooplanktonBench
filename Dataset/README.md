## Preparing Datasets

We provide the processed and labeled data. Please download [This]().  
For the labels, please note that there are two folders named `labels_classification` and `labels_living_detection`. Use them accordingly and do not use them together.

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


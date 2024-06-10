## Preparing Datasets

We provide the processed and labeled data.

For GPT-4V, please download [This]()

For YOLOv8 and GroundingDINO, please download[This]()



### Folder structure
In general, we need to create datasets following the structures below

    datasets
    │   README.md
    └───GPT-4V
    │       | chaeto_1.jpg
    |       | chaeto_2.jpg
    │       │   ...
    |   
    └───Marine_3_depths
    |       └───Marine_yolo_10m
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
    |       └───Marine_yolo_25m
    |       └───Marine_yolo_35m
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


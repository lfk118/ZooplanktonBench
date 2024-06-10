## Finetuned model

If you want to use the finetuned model we have, please download [Model]()

## Usage of notebook
1. For [`VALIDATION.ipynb`](https://github.com/lfk118/ZooplanktonCV/blob/main/YOLOv8/VALIDATION.ipynb). Please make sure you already have the dataset prepared.
Change the path for the model and the yaml file based on your settings.
2. For [`image+videl.ipynb`](https://github.com/lfk118/ZooplanktonCV/blob/main/YOLOv8/image%2Bvideo.ipynb). This notebook is for generating the labeled images from video.
Change the path for saving based on your settings.
3. For [`Training.ipynb`](https://github.com/lfk118/ZooplanktonCV/blob/main/YOLOv8/Training.ipynb). This notebook is for training the YOLOv8 model.
Change the path of yaml file based on your settings.

## Reproduce the results in our paper
1. For validation, please use the corresponding yaml file in the `config` folder. For example, if you want to get the result for model traning on 10 meters and testing on 25 meters, please use the `config 10_25.yaml` (You still need to adjust the path inside the file based on your settings.)
2. For training, please follow the same rule as 1. For example, if you would like to train a model on all 3 depths to do the classification, use the `config_all_mix.yaml`

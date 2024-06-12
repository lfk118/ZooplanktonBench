## Data preparation
Please make sure you download the [dataset](https://outlookuga-my.sharepoint.com/:f:/g/personal/fl79416_uga_edu/EhtmuP6IOTpErtRhcVR3s-oBegeA4cOb46Bkpel6eyMDFg?e=gbNeaE) before any experiments.

## Finetuned model

If you want to use the finetuned model we have, please download [Model](https://outlookuga-my.sharepoint.com/:f:/g/personal/fl79416_uga_edu/EhtmuP6IOTpErtRhcVR3s-oBegeA4cOb46Bkpel6eyMDFg?e=C1dewu)

## Usage of notebook
1. For [`VALIDATION.ipynb`](https://github.com/lfk118/ZooplanktonCV/blob/main/YOLOv8/VALIDATION.ipynb). Please make sure you already have the dataset prepared.
Change the path for the model and the yaml file based on your settings.
2. For [`image+video.ipynb`](https://github.com/lfk118/ZooplanktonCV/blob/main/YOLOv8/image%2Bvideo.ipynb). This notebook is for generating the labeled images from video. We already provided the labeled image data in our dataset, if you only want to train the model with video, please go to [`Training.ipynb`](https://github.com/lfk118/ZooplanktonCV/blob/main/YOLOv8/Training.ipynb)
Change the path based on your settings. The video dataset is located in `"Marine_dataset.zip/Video"`.
3. For [`Training.ipynb`](https://github.com/lfk118/ZooplanktonCV/blob/main/YOLOv8/Training.ipynb). This notebook is for training the YOLOv8 model.
Change the path of yaml file based on your settings.

## Reproduce the results in our paper
1. Ensure that you check the config folder to select the appropriate settings for both validation and training. The configuration files are named based on the dataset. For instance, `config_10.yaml` in the `config/Training` folder indicates the settings for training a model on 10 meters of data. Note that YAML files containing "living" in their names are intended for zooplankton detection rather than classification. When performing the corresponding task, please use the correct labels.
2. For validation, use the corresponding YAML file located in the `config/Validation` folder. For example, if you intend to obtain results for a model trained on 10 meters and tested on 25 meters, use the fine-tuned model from 10 meters and use the `config_25.yaml` as the data configuration file. Ensure to adjust the file path based on your settings.
3. Follow the same rules as outlined in point 1 for training. For instance, if you plan to train a model on data from all three depths for classification purposes, use the `config_all_mix.yaml` file.

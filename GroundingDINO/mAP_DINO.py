import torch
import cv2
import os
import ot
import numpy as np
from PIL import Image
from tqdm import tqdm
import supervision as sv
import matplotlib.pyplot as plt
from groundingdino.util.inference import load_model, load_image, predict, annotate
from torchvision.ops import box_convert,nms,box_iou, box_area


def mAP_result(Ground_truth_train, Label_train,model,threshold):
    
    categories={
    0: "chaetognath",
    1: "larval fish",
    2: "Hydromedusa",
    3: "lobate ctenophore",
    4: "Pleurobrachia",
    5: "shrimp",
    6: "Siphonophore",
    7: "stomatopod larva",
    8: "Unknown",
    9: "Thaliac",
    10: "polychaete worm",
    11: "Cumacean",
    12:"ctenophore"
}
    im_file = os.listdir(Ground_truth_train)
    detector_result = {}
    for io in np.arange(0.50, 1.00, 0.05):
        iou_threshold = io
        detector_result[io] = {}
        count = {}
        for i in tqdm(im_file):
            temp = i.split(".jpg")[0]
            label = np.loadtxt(Label_train + temp + ".txt")
            ground_boxes = {}
            if type(label[0]) == np.float64 :
                if label[0] in ground_boxes.keys():
                    ground_boxes[label[0]] = np.vstack((ground_boxes[label[0]],label[1:5]))
                else:
                    ground_boxes[label[0]] = {}
                    ground_boxes[label[0]] = label[1:5]
            else:
                for j in label:
                    if j[0] in ground_boxes.keys():
                        ground_boxes[j[0]] = np.vstack((ground_boxes[j[0]],j[1:5]))
                    else:
                        ground_boxes[j[0]] = {}
                        ground_boxes[j[0]] = j[1:5]


            #print(i, ground_boxes)
            for key in ground_boxes.keys():
                if categories[key] not in detector_result[io].keys():
                    count[categories[key]] = 0
                    detector_result[io][categories[key]] = {}
                    detector_result[io][categories[key]]['TP'] = 0
                    detector_result[io][categories[key]]['FP'] = 0
                    detector_result[io][categories[key]]['FN'] = 0
                    detector_result[io][categories[key]]['P'] = 0

                count[categories[key]] += 1

                Temp = ground_boxes[key]
                Temp_xyxy =box_convert(boxes=torch.from_numpy(Temp), in_fmt='xywh', out_fmt='xyxy')
                Temp_cxcywh = box_convert(boxes=torch.from_numpy(Temp), in_fmt='xywh', out_fmt='cxcywh')

                classes = categories[key]
                ori_img_path = os.path.join(Ground_truth_train,i)
                if len(Temp.shape) == 1:
                    num_truth = 1
                else:
                    num_truth = Temp.shape[0]

                TEXT_PROMPT = classes
                BOX_TRESHOLD = threshold
                TEXT_TRESHOLD = threshold

                image_source, image = load_image(ori_img_path)

                boxes, logits, phrases = predict(
                    model=model,
                    image=image,
                    caption=TEXT_PROMPT,
                    box_threshold=BOX_TRESHOLD,
                    text_threshold=TEXT_TRESHOLD
                )



                boxes_nms =box_convert(boxes=boxes, in_fmt='xywh', out_fmt='xyxy')
                index_nms = nms(boxes_nms, logits, 0.1)
                index_nms = index_nms.sort().values
                boxes = boxes[index_nms]


                detected_truth = 0
                detected_false = 0
                for l in boxes:
                    if l[3] >= 0.8: continue #filtering for abnormal result
                    box_xyxy =box_convert(boxes=l, in_fmt='xywh', out_fmt='xyxy')
                    iou_result = np.asarray(box_iou(box_xyxy.view([1,4]),Temp_xyxy.view([num_truth,4]))).max(axis = 1)  
                    if iou_result >= iou_threshold:
                        detected_truth += 1
                        detector_result[io][categories[key]]['TP'] += 1
                    else:
                        detected_false += 1
                        detector_result[io][categories[key]]['FP'] += 1

                if num_truth - detected_truth < 0:
                    print(num_truth - detected_truth)
                detector_result[io][categories[key]]['FN'] += (num_truth - detected_truth)
                if (detected_truth + detected_false)  != 0:
                    detector_result[io][categories[key]]['P'] += detected_truth / (detected_truth + detected_false)        


        for key in detector_result[io].keys():
            detector_result[io][key]['P'] /= count[key]

    return detector_result


def mAP_cal(diction):
    mAP = 0
    length = len(diction.keys())
    for key in diction:
        mAP += diction[key]['P']
    mAP /= length
    return mAP


def mAP50_95(diction):
    mAP = 0
    for key in diction.keys():
        mAP += mAP_cal(diction[key])
    return mAP/10

def result(Ground_truth_train, Label_train,model,threshold):
    result = mAP_result(Ground_truth_train, Label_train,model,threshold)
    mAP = mAP_cal(result[0.5])
    mAP50_95 = mAP50_95(result)
    return mAP, mAP50_95

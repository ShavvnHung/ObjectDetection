# Report

## Introduction

An simple object detection task to detect 10 different creatures. There are 690 images in my dataset. and I split train, test, validation dataset with ratio 80%/10%/10%, respectively.

![](https://i.imgur.com/VDIh2DD.png)


## Results and Models

Run on RTX3090

| Model | Epochs | mAP | mAP<sub>50</sub> | mAP~75~|
| -------- | ------- | -------- | -------- | -------- |
| YOLOv3  | 273    | 0.43 | 0.768 | 0.461 |
| YOLOX   | 300    | 0.343| 0.646 | 0.308 |

## Usage 

``$ python inference.py [config file] [checkpoint file] [image name file]``

will output the detection result. The detection result of my own test dataset is in yolov3_result and yolox_result, respectively.

## Running

``$ python inference.py yolov3_model/yolov3_d53_mstrain-608_273e_coco.py yolov3_model/epoch_273.pth test_image_list``

## Reference

* [mmdetection](https://github.com/open-mmlab/mmdetection)
* [yolov3](https://arxiv.org/pdf/1804.02767)
* [yoloX](https://github.com/Megvii-BaseDetection/YOLOX)

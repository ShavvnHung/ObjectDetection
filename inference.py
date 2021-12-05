from mmdet.apis import inference_detector, init_detector, show_result_pyplot
import sys

# Choose to use a config and initialize the detector
config = str(sys.argv[1])
# Setup a checkpoint file to load
checkpoint = str(sys.argv[2])
# initialize the detector
model = init_detector(config, checkpoint, device='cuda:0')

with open(str(sys.argv[3]), 'r') as f1:
    for img in f1.read().splitlines():
        result = inference_detector(model, img)
        model.show_result(img, result, out_file='val/' + img.split('/')[-1])
# -*- coding: utf-8 -*-
"""Part 3 - Deployment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MVKBZdQB-a8pmu0FObgI67O1-D6riYl4

# 1. Google Drive Connection and Setup
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/content/drive')

# Installing and importing libraries
# %cd '/content/drive/MyDrive/RDD_Final/yolov5'
# %pip install -qr requirements.txt  # install

import torch
from PIL import Image, ImageDraw
import os

# Path to the best model name you chose - here third_training_5l_100e_scrlow
model_name='/content/drive/MyDrive/RDD_Final/yolov5/RDD - Yolov5/third_training_5l_100e_scrlow/weights/best.pt'
model = torch.hub.load(os.getcwd(), 'custom', source='local', path = model_name, force_reload = True)
model.conf = 0.2

"""# 2. Deployment"""

!pip install gradio

import gradio as gr
def yolo(im, size=732):
    g = (size / max(im.size))  # gain
    im = im.resize((int(x * g) for x in im.size), Image.ANTIALIAS)  # resize

    results = model(im)  # inference
    results.render()  # updates results.imgs with boxes and labels
    return Image.fromarray(results.imgs[0])


inputs = gr.inputs.Image(type='pil', label="Original Image")
outputs = gr.outputs.Image(type="pil", label="Output Image")

title = 'Road Damage Detection Tool'
description = "Choose a picture"

#examples = ['/content/drive/MyDrive/RDD/LN/yolov5/RDD - Yolov5/4_training_5s_100e_scrlow/weights/image_test/Czech_000002.jpg']
gr.Interface(yolo, inputs, outputs, title=title, description=description, analytics_enabled=False).launch(
    debug=True)
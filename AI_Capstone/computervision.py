import cv2
import torch
import numpy as np
import pandas as pd
import time as t

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, etc.
model = torch.hub.load('ultralytics/yolov5', 'custom','bestv2.pt',force_reload=True,trust_repo=True)  # custom trained model

def Model_detection():
    vid = cv2.VideoCapture(1)
    Class_detected = [] 
    Confidence_detected = []  
    #vid = cv2.VideoCapture(0)
    # define a video capture object
    


    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    results =  model(frame)
   
    im = 'Sam.jpg'  # or file, Path, URL, PIL, OpenCV, numpy, list

# Inference
    # results = model(im)
    results.show()
    results.xyxy[0]
    df=results.pandas().xyxy[0]
    Class_detected = df['class'].tolist()
    Confidence_detected = df['confidence'].tolist()
    
    Class_detected = df['class'].tolist()
    print(df)
    Confidence_detected = df['confidence'].tolist()
  
    return Class_detected, Confidence_detected


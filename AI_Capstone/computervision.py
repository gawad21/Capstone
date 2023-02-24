import cv2
import torch
import numpy as np
import pandas as pd
import time as t

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, etc.
model = torch.hub.load('ultralytics/yolov5', 'custom','bestv2.pt',force_reload=True,trust_repo=True)  # custom trained model
#vid = cv2.VideoCapture(0)
im = 'C:\\Users\\goule\\OneDrive\\Desktop\\YOLO\\leaf.jpg'
'''
def Model_detection():
    Class_detected = [] 
    Confidence_detected = []  
    vid = cv2.VideoCapture(0)
    # define a video capture object
    

    while(True):
      
    # Capture the video frame
    # by frame
        #ret, frame = vid.read()
        results =  model(im)
        results.show()
        results.xyxy[0]
        df=results.pandas().xyxy[0]

        Class_detected = df['class'].tolist()
        Confidence_detected = df['confidence'].tolist()
    # Display the resulting frame
        #cv2.imshow('frame', frame)
        if  df.empty:
            print("The DataFrame is empty. Breaking out of the loop.")
            break
        Class_detected = df['class'].tolist()
        Confidence_detected = df['confidence'].tolist()
        break

    return Class_detected, Confidence_detected

'''
# After the loop release the cap object
#vid.release()
# Destroy all the windows
#v2.destroyAllWindows()
#vid = cv2.VideoCapture("C:\\Users\\goule\\OneDrive\\Documents\\Courses\\Winter 2023\\Capstone2\\Test\\test.mp4")
path="C:\\Users\\goule\\OneDrive\\Documents\\Courses\\Winter 2023\\Capstone2\\Test\\test.mp4"
def Model_detection():
    vid = cv2.VideoCapture(path)
    Class_detected = [] 
    Confidence_detected = []  
    vid = cv2.VideoCapture(0)
    # define a video capture object
    


    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    results =  model(frame)
    #results.show()
    results.xyxy[0]
    df=results.pandas().xyxy[0]
    Class_detected = df['class'].tolist()
    Confidence_detected = df['confidence'].tolist()
    
    Class_detected = df['class'].tolist()
    print(df)
    Confidence_detected = df['confidence'].tolist()
  
    return Class_detected, Confidence_detected

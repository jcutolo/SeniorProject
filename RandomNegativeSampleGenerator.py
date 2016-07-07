import os
import cv2
import numpy as np
import random

# Enter current working directory in here
dir = "C:\\Users\\Joshua\\Desktop\\Senior\\Negative\\"
videoname = "neg2.mp4"

xdim = 480
ydim = 360
os.chdir(dir)
cap = cv2.VideoCapture(videoname)
l1 = videoname.split(".")
frame = 0
ret, img = cap.read()
while(ret):
    x1 = random.randint(0, xdim-64)
    y1 = random.randint(0, ydim-128)
    x2 = random.randint(0, xdim-64)
    y2 = random.randint(0, ydim-128)
    x3 = random.randint(0, xdim-64)
    y3 = random.randint(0, ydim-128)
    v1 = l1[0] + str(frame)+"_1.jpeg"
    v2 = l1[0] + str(frame)+"_2.jpeg"
    v3 = l1[0] + str(frame)+"_3.jpeg"
    cv2.imwrite(v1,img[y1:y1+128,x1:x1+64])
    cv2.imwrite(v2,img[y2:y2+128,x2:x2+64])
    cv2.imwrite(v3,img[y3:y3+128,x3:x3+64])
    ret,img = cap.read()
    frame=frame+1
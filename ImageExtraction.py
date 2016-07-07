#ImageExtraction.py

#This file extracts images from a specific video in the UCF Dataset according to the x,y,width,height values
#that were extracted from the parsed viper files.

#import statements
import numpy as np
import cv2
import os

#ucfFile is the parsed text file that was created from the shell scripting of each video in the UCF Dataset
ucfFile = open('C:\\Users\\Joshua\\Desktop\\New Folder\\AerialTape3part1\\tape3_part1_parsed.txt', 'r')
N = np.loadtxt(ucfFile,dtype=int, delimiter=",")

#Open the video to begin extracting the images
cap = cv2.VideoCapture('C:\\Users\\Joshua\\Desktop\\New Folder\\AerialTape3part1\\aerial_tape3_part1.mpg')
frame = 1
i = 0
j = 0

#Opens the specific directory we want the images to be placed
dirName = 'C:\\Users\\Joshua\\Desktop\\New Folder\\AerialTape3part1\\'

#Begin reading in each frame from the video and extracting each image
while(True):
    ret, img = cap.read()
    while (N[i][0] == frame):
        if(N[i][1]<0 or N[i][2]<0 or N[i][3]<0 or N[i][4]<0):
            i = i + 1
        else:
            tmp_img = img[N[i][4]:N[i][4]+N[i][1], N[i][3]:N[i][3]+N[i][2]]
            
            print(N[i])
            if (tmp_img.size!=0):
                save_img = cv2.resize(tmp_img,(64,128))
                tmpStr = "aerialtape3_"+str(j)+".jpeg"
                cv2.imwrite(os.path.join(dirName,tmpStr),save_img)
            i = i + 1
            j = j + 1
    frame = frame+1
cap.release()
cv2.destroyAllWindows()

    
    





from fileinput import filename
import os
from os import listdir
import cv2 as cv
import numpy as np

count=0
folder_dir = "kaggleset/train_zip/train"

for images in os.listdir(folder_dir):
   
    # check if the image ends with png
    if (images.endswith(".jpg")):
        count=count+1
        img1=cv.imread(os.path.join(folder_dir,images))
        print("format ",type(img1.shape[0]))
        img1=np.array(img1,dtype='uint8')
        
        gray=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
        
        output_dir="resultimages"
        filename=str(count) + ".png"
        #cv.imwrite(os.path.join(output_dir,filename),gray)

print("number of images",count)
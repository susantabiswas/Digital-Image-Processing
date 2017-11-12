#read 5 imgs from folder A and 5 imgs from folder B,convert them to binary and save in folder C

import cv2
import numpy as np

def doOperation( filename, folder):
    if folder == 'A':
        path = "A/" + filename  
    elif folder == 'B':     
        path = "B/" + filename
    else:
        print ("Invalid file")
        return
            
    thresh = 127
    #read the image
    img = cv2.imread(path,0)
    
    prop = img.shape
    row = prop[0]
    col = prop[1]
    
   #convert to binary
    for i in range(0,row):
        for j in range(0,col):
            if img[i][j] > 127:
                img[i][j] = 255
            else:
                img[i][j] = 0
    
    destFilename = "C/" + "sol" + filename 
    #save the img
    cv2.imwrite(destFilename,img)

for i in range(1,6):    
    doOperation( str(i) + '.tif', 'A')  

for i in range(1,6):    
    doOperation( str(i) + '.tif', 'B')  
    


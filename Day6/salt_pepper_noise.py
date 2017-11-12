'''  remove salt and pepper noise from an image  
by applying median filter of size 3x3 and 5x5 '''

import cv2
import numpy as np 

img = cv2.imread('sap.png',0)
new_img = cv2.imread('sap.png', 0)
prop = img.shape

#we take a window and find the median of intensity values 
#in that window and assigned it to the current pixel

############### 3x3 window ############### 
for i in range(1, prop[0] - 1):
    for j in range(1, prop[1] - 1):
        
        win = []
        for x in range(i-1, i + 2):
            for y in range(j-1, j+2):
                win.append( img[x][y] )
        #sort the values
        win.sort()

        new_img[i][j] = win[4]

cv2.imwrite('3x3_median.jpg', new_img)


############### 5x5 window ###############
new_img = cv2.imread('sap.png', 0)

for i in range(1, prop[0] - 2):
    for j in range(1, prop[1] - 2):
        win = []
        for x in range(i - 2, i + 3):
            for y in range(j - 2, j + 3):
                win.append(img[x][y])
        #sort the values
        win.sort()

        new_img[i][j] = win[12]

cv2.imwrite('5x5_median.jpg', new_img)


        

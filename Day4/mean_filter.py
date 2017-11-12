''' Apply mean filter on an image '''

import cv2
import numpy as np 

img = cv2.imread('lenna.jpg', 0)
new_img = np.copy(img)
prop = img.shape

#we take a 3x3 mask
'''
mask:
0 1 0
1 2 1
0 1 0 
 '''
for i in range(1, prop[0] - 1):
    for j in range(1, prop[1] - 1):
        new_img[i][j] = ( img[i-1][j] + img[i][j-1] + img[i][j]*2 + img[i][j+1] + img[i+1][j])/6

cv2.imwrite('mean_filtered.jpg', new_img)           

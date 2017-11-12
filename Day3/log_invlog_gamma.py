'''
point processing based image enhancement using:
1. Log and Inverse log transformations
2. Gamma corrections(Power law transformation) with +ve and -ve values
'''

import cv2
import numpy as np 

############## log transform ############
img = cv2.imread('transformation.png', -1)
prop = img.shape
c = 20

for i in range(0, prop[0]):
    for j in range(0, prop[1]):
        img[i][j] = c* np.log(img[i][j] + 1)

cv2.imshow('log_img',img)
cv2.waitKey(0)
cv2.imwrite('log_img.png', img)

############### Inverse Log ################
 
img = cv2.imread('transformation.png', -1)
prop = img.shape

for i in range(0, prop[0]):
    for j in range(0, prop[1]):
        img[i][j] = np.exp( img[i][j] ) * ( np.log(255)/ (255 - 1) - 1)


cv2.imshow('invlog_img',img)
cv2.waitKey(0)
cv2.imwrite('invlog_img.png', img)

############ Power law ############
img = cv2.imread('transformation.png', -1)
prop = img.shape

c = 20
gamma = 8

for i in range(0, prop[0]):
    for j in range(0, prop[1]):
        img[i][j] = c * img[i][j]** gamma

cv2.imshow('powlaw_img', img)
cv2.waitKey(0)
cv2.imwrite('powlaw_img.png', img)

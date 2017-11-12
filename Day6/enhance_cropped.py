'''Crop a portion of the image,
enhance it and place it back in the original image  
'''
import cv2
import numpy as np 

img = cv2.imread('lenna.jpg', 0)

crop = np.copy(img[ 200:300, 200: 300])

#apply histogram equilization
eq = cv2.equalizeHist( crop )

img[200:300, 200: 300] = np.copy( eq )

cv2.imwrite('cropped_enhanced.jpg', img)

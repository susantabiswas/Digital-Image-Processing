'''
program to detect horizontal and vertical line 
'''
import cv2
import numpy as np 

#read the image in greyscale
img = cv2.imread('hori_ver.jpg', 0)

#we will use sobel operator for this task

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

#detecting horizontal edges
hor_img = cv2.addWeighted(sobelx, 0, sobely, 1, 0)
cv2.imwrite('hor_edge.jpg', hor_img)


#detecting horizontal edges
ver_img = cv2.addWeighted(sobelx, 1, sobely, 0, 0)
cv2.imwrite('ver_edge.jpg', ver_img)

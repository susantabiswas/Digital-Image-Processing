#crop a given image
import cv2
import numpy as np 
from matplotlib import pyplot as plt

img = cv2.imread('lenna.jpg',-1)

#get dimension of image
prop = img.shape

print('Enter Top left coordinates')
lx = int(input())
ly = int(input())

print('Enter Bottom Right coordinates')
rx = int(input())
ry = int(input())

#make a matrix of given size
h = rx - lx + 1
w = ry - ly + 1
new_img = np.zeros( (h,w, 3), np.uint8) 

#fill the new cropped dimesion matrix
for i in range(lx, rx + 1):
    for j in range(ly, ry + 1):
        new_img[i - lx][j - ly] = img[i][j]

cv2.imwrite('cropped_img.jpg', new_img)
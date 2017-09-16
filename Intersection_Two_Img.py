'''
a.Compute the intersection of two imgs
b.merge two grayscale imgs using XOR and XNOR op
'''
import cv2
import numpy as np

img1 = cv2.imread("p1.jpg",0)
img2 = cv2.imread("p2.jpeg",0)
#resize the imgs
img3 = cv2.resize(img1,(400,400))
img4 = cv2.resize(img2,(400,400))

#create a new img
img5 = np.zeros(shape=(400,400))
#find the intersection
for i in range(400):
    for j in range(400):
        img5[i][j] = img3[i][j] & img4[i][j]
        
cv2.imwrite("p3_intersection.jpg",img5)

#create a new img
img6 = np.zeros(shape=(400,400))
#create a img using XOR
for i in range(400):
    for j in range(400):
        img6[i][j] = img3[i][j] ^ img4[i][j]
        
cv2.imwrite("p3_xor.jpg",img6)

#create a new img
img7 = np.zeros(shape=(400,400))
#create a img using XNOR
for i in range(400):
    for j in range(400):
        img7[i][j] = ~(img3[i][j] ^ img4[i][j])
        
cv2.imwrite("p3_xnor.jpg",img7)

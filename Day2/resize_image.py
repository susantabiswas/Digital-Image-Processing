#resize a given image

import cv2
from matplotlib import pyplot as plt

#read the image
img = cv2.imread('lenna.jpg',-1)

#zoomed picture
zoom_img = cv2.resize(img, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)
cv2.imwrite('zoomed.jpg', zoom_img)

#diminished picture
dimin_img = cv2.resize(img, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_LINEAR)
cv2.imwrite('diminished.jpg', dimin_img)

cv2.imshow('pic',img)
cv2.waitKey(0)

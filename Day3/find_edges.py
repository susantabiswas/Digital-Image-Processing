''' Find edges in an image using Sobel Operator
'''

import cv2
import numpy as np 

img = cv2.imread('transformation.png', -1)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

new_img = cv2.addWeighted( sobelx, 0.5, sobely, 0.5, 0)
cv2.imwrite('edge_detection.jpg', new_img)
''' remove gaussian noise using gaussian filter '''

import cv2
import numpy as np 

img = cv2.imread('gauss.png', 0)

gauss = cv2.GaussianBlur(img, (5,5), 0)

res = np.hstack( (img, gauss))
cv2.imwrite('gauss_filtered.jpg', res)
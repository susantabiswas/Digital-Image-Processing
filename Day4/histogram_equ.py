''' perform histogram equilisation on an image '''

import cv2
import numpy as np 

img = cv2.imread('lenna.jpg', 0)
eq = cv2.equalizeHist( img )
cv2.imwrite('t1.jpg', eq)
result = np.hstack(( img, eq) )
cv2.imwrite('equliz.jpg', result)

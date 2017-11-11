#Convert a grayscale image to a colour image with the following adjustments:
# if I>245 then R=I-60,G=I-40,B=I-5
# else R=I+60,G=I+40,B=I+5

import cv2
import numpy as np

#open the image
img = cv2.imread('lenna.tif',0)

#get the image dimensions
prop = img.shape

#make a new image of exact dimesions with eaech element being a tuple
rgb_img = np.zeros( (prop[0], prop[1], 3), np.uint8)
#in a color image each value is represented as a tuple with 3 elements(rbg)
for i in range( prop[0] ):
    for j in range( prop[1] ):
        if img[i][j] > 245:
            rgb = [img[i][j] - 60, img[i][j] - 40, img[i][j] - 5]
            rgb_img[i][j] = rgb
        else:
            rgb = [img[i][j] + 60, img[i][j] + 40, img[i][j] + 5]
            rgb_img[i][j] =  rgb

#save the file
cv2.imwrite('grey_to_color.jpg',rgb_img)
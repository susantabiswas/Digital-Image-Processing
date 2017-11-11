#convert a color image to greyscale image without using any library function
import cv2

#we will use the following formula for converting 
#intensity = 0.21*r + 0.71*g + 0.07*b
img = cv2.imread('lenna.tif',-1)

prop = img.shape

for i in range(prop[0]):
    for j in range( prop[1]):
        img[i][j] = 0.07*img[i][j][2] + 0.71*img[i][j][1] + 0.21*img[i][j][0]

cv2.imshow('greyscale',img)
cv2.waitKey(0)
cv2.imwrite('greyscale_lenna.jpg',img)

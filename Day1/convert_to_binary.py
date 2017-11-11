#convert an image to binary image
import cv2

#open the image in greyscale
img = cv2.imread('lenna.tif',0)

#if the intensity is lesser than equal to 127,make it black else white

prop = img.shape

for i in range(prop[0]):
    for j in range( prop[1]):
        if img[i][j] <= 127:
            img[i][j] = 0
        else:
            img[i][j] = 255

cv2.imwrite('lenna_binary.jpg',img)
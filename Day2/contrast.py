#adjust the contrast of an image
#This code increases the contrast of an image
import cv2

#open the imaege in greyscale
img = cv2.imread('lenna.jpg',0)
cv2.imwrite('grey.jpg', img)
#get dimensions
prop = img.shape

#we select a threshold and see if the intensity is below it or greater than that threshold
for i in range(0, prop[0]):
    for j in range(0, prop[1]):
        if img[i][j] <= 127:
            if img[i][j] - 50 >= 0:
                img[i][j] = img[i][j] -50 
           
            #img[i][j] = 250
        else:
            if img[i][j] + 50 <= 255:
                img[i][j] = img[i][j] + 50 
           #img[i][j] = 15

#save the image
cv2.imwrite('contrast.jpg',img)
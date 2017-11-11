#open an image and save it in different formats,also display their sizes
import cv2
import os

#open the file
img = cv2.imread("lenna.tif",-1)

#jpeg file
jpg = cv2.imwrite('lenna_jpg.jpg')
print( 'file size jpeg:' + os.path.getsize('lenna_jpg.jpg'))

#png file
png = cv2.imwrite('lenna_png.png')
print( 'file size png:' + os.path.getsize('lenna_png.png'))

#tif file 
print('file size tif' + os.path.getsize('lenna.tif'))
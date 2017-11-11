#open an image and save it in different formats,also display their sizes
import cv2
import os

#open the file
img = cv2.imread("lenna.tif",-1)

#jpeg file
jpg = cv2.imwrite('lenna_jpg.jpg',img)
print( 'file size jpeg:' + str(os.path.getsize('lenna_jpg.jpg')/1024**2) + "MB" ) 

#png file
png = cv2.imwrite('lenna_png.png',img)
print( 'file size png:' + str(os.path.getsize('lenna_png.png')/1024**2) + "MB")

#tif file 
print('file size tif' + str(os.path.getsize('lenna.tif')/1024**2) + "MB")
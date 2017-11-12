#multiply two images
import cv2
import numpy as np 

#apply sobel to image and find its fft
img1 = cv2.imread('lenna.jpg', 0)
sobelx = cv2.Sobel(img1, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img1, cv2.CV_64F, 0, 1, ksize=5)

#edge detected image
img2 = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

#do fft on first 
f = np.fft.fft2( img1 )
fshift = np.fft.fftshift( f )
mag_spec1 = 20 * np.log( np.abs(fshift) )

#do fft on sobel operated image
f = np.fft.fft2( img2 )
fshift = np.fft.fftshift(f)
mag_spec2 = 20 * np.log(np.abs(fshift))

mat = np.copy(mag_spec1)
prop = mag_spec1.shape
for i in range(0, prop[0]):
    for j in range(0, prop[1]):
        mat[i][j] = (mag_spec1[i][j] * mag_spec2[i][j]) / 255

cv2.imwrite('multiply.jpg', mat)
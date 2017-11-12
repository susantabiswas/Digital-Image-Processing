''' Do fast fourier transform on an image '''

import cv2
import numpy as np 

img = cv2.imread('lenna.jpg', 0)
rows, cols = img.shape

#convert to frequency domain
f = np.fft.fft2(img)
#bring the dc component( 0 freq) to the center by 
#shifting by n/2 in both directions
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log( np.abs(fshift) )

cv2.imwrite('fft.jpg', magnitude_spectrum)

''' ## inverse fft
crow = rows / 2
ccol = cols / 2
fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
cv2.imwrite('orignal_fft.jpg', img_back)
 '''
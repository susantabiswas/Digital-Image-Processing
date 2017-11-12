''' apply DST transformation on an image '''
import cv2
import numpy as np


#### In DST we are taking imaginary value ####

img = cv2.imread('lenna.jpg', 0)
f1 = np.fft.fft2(img)
fshift = np.fft.fftshift(f1)
magnitude_spectrum = 20 * np.log(np.imag(fshift))
cv2.imwrite('dst.png', magnitude_spectrum)

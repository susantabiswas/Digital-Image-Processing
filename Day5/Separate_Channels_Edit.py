#Separate the diff. channels from an img
#a.enhance the R plane by 30
#b.enhance the G plane by -30
#c. enhance the B plane by 20.
import numpy as np
import cv2

#read the img
img = cv2.imread("p1.tif",-1)

#get the row and col size
prop = img.shape
row = prop[0]
col = prop[1]

#split the img
b,g,r = cv2.split(img)


#modify the values to enhance
for x in range(1,row):
	for y in range(1,col):
		b[x][y] = min(255,b[x][y]+30)
		
for x in range(1,row):
	for y in range(1,col):
		g[x][y] = max(0,g[x][y] - 30)

for x in range(1,row):
	for y in range(1,col):
		r[x][y] = min(255,r[x][y] + 20)

#merge the channels
img = cv2.merge((b,g,r))
cv2.imwrite("Enhanced.jpg",img)


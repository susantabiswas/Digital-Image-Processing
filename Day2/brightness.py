#adjust brightness of an image

#when the user enters 'i' key then increase the brightness and when 'd' decrease the brightness
#brightness can be adjusted just by increasing / decreasing the intensity values of RGB
import cv2 

#open image file
img = cv2.imread( 'lenna.jpg',-1)

#get image dimesions
prop = img.shape

#increase each value by 50
def increaseBrightness(img, prop):
    for i in range( 0, prop[0] ):
        for j in range( 0, prop[1] ):
            for k in range(0, 3):
                try:
                    if img[i][j][k] + 50 <= 255: 
                        img[i][j][k] =  img[i][j][k] + 50
                except IndexError:
                    continue
                 
#decrease each value by 50
def decreaseBrightness(img, prop):
    for i in range( 0, prop[0] ):
        for j in range( 0, prop[1] ):
            for k in range(0, 3):
                try:
                    if img[i][j][k] - 50 >= 0: 
                        img[i][j][k] =  img[i][j][k] - 50
                except IndexError:
                    continue

key = 'e'  
                  
while( key != ord('q')):
    cv2.imshow('pic',img)
    key = cv2.waitKey(0)

    #increase brightness
    if key == ord('i'):
        print('Working')
        increaseBrightness(img, prop)
        print("Done\n")

    #decrease brightness
    elif key == ord('d'):
        print('Working')
        decreaseBrightness(img, prop)
        print("Done\n")

    #exit and save the image
    elif key ==  ord('q'):
        cv2.imwrite('brightness.jpg',img)
        cv2.destroyAllWindows()
        break

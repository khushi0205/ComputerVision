#import numpy as np
import cv2

img = cv2.imread('messi.png')

#print(img.shape) #returns tuple of no of rows, columns and channels
#print(img.size) #returns total number of pixel is accessed
#print(img.dtype) #returns image datatype is obtained
#b,g,r = cv2.split(img)
#img = cv2.merge((b,g,r))


"""def click_event(event, x, y, flags, para):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'x: ' + str(x) + ' y: ' + str(y)
        cv2.putText(img, text, (x,y) , font, 0.5, (0,0,255), 1)
        cv2.imshow('img', img)"""

ball = img[200:300, 300: 400]
img[500:600, 600: 700] = ball

cv2.imshow('img', img)
#cv2.setMouseCallback('img', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
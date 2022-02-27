import numpy as np
import cv2

#create img using numpy zeros
#Black image     H    W       datatype
img = np.zeros([512, 512, 3], np.uint8)

#img = cv2.imread('F4.png', 1)
#                                        B, G ,R
image = cv2.line(img, (0,0), (255,255), (0,255,0), 5)
            #    name  pt1     pt2       colour    thickness
imag= cv2.arrowedLine(img, (0,255), (255,255), (0,0,255), 5)
im=cv2.rectangle(img, (384,0), (510,128), (0,0,255), -1)
#                      topleft bottomright       fillscolour
i = cv2.circle(img, (447,63), 63, (255,0,0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
pic = cv2.putText(img, 'opencv', (10,500), font, 4, (255, 255, 255),10, cv2.LINE_AA)
#                 name  namedisp  point     f  fsize    fcolour     t   linetype

cv2.imshow('line', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
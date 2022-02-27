import cv2
from torch import q_per_channel_scales

""" img = cv2.imread('F4.png', -1)
#print(img)

cv2.imshow('car1', img)
k = cv2.waitKey(0)

if k == 27: #27 = escape key
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('F4_py.png', img) """

img = cv2.VideoCapture(0)

while (True):
    ret, frame = img.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video', gray)
    if cv2.waitKey(1) == ord('q'):
        break

img.release()
cv2.destroyAllWindows()
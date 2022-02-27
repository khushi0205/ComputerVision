import numpy as np
import cv2

#prints all the event func present in cv2 directory
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event, x, y, flags, para):
    """ if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'x: ' + str(x) + ' y: ' + str(y)
        cv2.putText(img, text, (x,y) , font, 0.5, (0,0,255), 1)
        cv2.imshow('img', img) """
    
    """ if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x, 0]
        green = img[y,x, 1]
        red = img[y,x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        Text = 'B: ' + str(blue) + ' G: ' + str(green) + ' R: ' + str(red)
        cv2.putText(img, Text, (x,y) , font, 0.5, (0,255,255), 1)
        cv2.imshow('img', img) """
###########################################################################################

# code to join points
    """if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0,255,0), 5)
        cv2.imshow('img', img)"""

    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x, 0]
        green = img[y,x, 1]
        red = img[y,x, 2]
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        mycolorimg = np.zeros((512,512,3), np.uint8)
        mycolorimg[:] = [blue, green, red]
        cv2.imshow('img', mycolorimg)





#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('F4.png')
cv2.imshow('img', img)
points = []
#window name should be same everywhere
cv2.setMouseCallback('img', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
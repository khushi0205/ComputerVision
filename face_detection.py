import cv2
from random import randrange
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#DETECT FACES FROM PHOTOS

#img = cv2.imread('multi.png')
#img = cv2.imread('F3.png',0)

# gs_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# face_coordinates = trained_face_data.detectMultiScale(gs_img)
#                    topleft     x+width,y+height   B, G ,R , thickness
#cv2.rectangle(img, (123, 215), (123+353,215+353), (0,255,0), 2)
#(x, y, w, h) = face_coordinates[0] #index represents number of face
# for (x,y,w,h) in face_coordinates:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 7)
#cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,randrange(255)), 7)

# print(face_coordinates)
# cv2.imshow("FD", img)
# cv2.waitKey()
# print("hello")


#DETECT FACES FROM VIDEO
webcam = cv2.VideoCapture('park.mp4')
key = cv2.waitKey(1)

#iterate forever over frames
while True:
    #read current frame
    successful_frame_read, frame = webcam.read()
    gs_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(gs_img)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 7)
    cv2.imshow("FD", frame)
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break
webcam.release()
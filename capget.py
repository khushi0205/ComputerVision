import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #property no: 3
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #property no: 4
#every property has number associated with it

#cap.set(3, 3000)
#cap.set(4, 3000)


#print(cap.get(3)) #property no: 3
#print(cap.get(4)) #property no: 3


while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_SIMPLEX
        date = str(datetime.datetime.now())
        text = 'W: ' + str(cap.get(3)) + ' H: ' + str(cap.get(4))
        frame = cv2.putText(frame, date, (10,50), font, 1, (0,0,255), 1, cv2.LINE_AA)
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
        

cap.release()
cv2.destroyAllWindows()
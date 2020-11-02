import cv2
import datetime

cap= cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    if(ret==True):
        font=cv2.FONT_HERSHEY_DUPLEX
        date=datetime.datetime.now()
        date=date.strftime("%D")
        date=str(date)
        text = 'Width: ' + str(cap.get(3)) + " Height: " + str(cap.get(4))
        frame= cv2.putText(frame, date, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
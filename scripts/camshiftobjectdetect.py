import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("../videos/object_track.3gp")
_, first_frame = cap.read()
first_frame = cv2.resize(first_frame, (720, 512))
x,y, w, h = 300, 170, 250, 190
window = x, y, w, h
# plt.imshow(first_frame)
# plt.show()

ROI = first_frame[y:y+h, x:x+w]
hsv_roi = cv2.cvtColor(ROI, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))

roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
# cv2.imshow("roi", ROI)

term_criteria = (cv2.TERM_CRITERIA_EPS| cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    _, frame = cap.read()
    if frame is None:
        break
    frame = cv2.resize(frame, (720, 512))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    backproject = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
    ret, window = cv2.CamShift(backproject, window, term_criteria)
    # print(ret)
    # x, y, w, h = window
    # cv2.rectangle(frame, (x, y), (x+w, y+h), (255,255, 0), 3)

    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    print(pts)
    
    cv2.polylines(frame, [pts], True, (255,255,0), 3)
    cv2.imshow("Frame", frame)
    # print(frame.shape)
    # cv2.imshow("BackProject", backproject)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

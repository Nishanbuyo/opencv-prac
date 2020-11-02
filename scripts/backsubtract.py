import cv2
import numpy as np

cap = cv2.VideoCapture("../videos/walking.avi")
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
# fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows= True)
# fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
# fgbg = cv2.createBackgroundSubtractorKNN(detectShadows= False)
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
while cap.isOpened():
    ret, frame = cap.read()
    if frame is None:
        break
    print(frame.shape)
    fgmask= fgbg.apply(frame)
    fgmask = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR) 
    # fgmask = cv2. morphologyEx(fgmask, cv2.MORPH_OPEN, kernel= kernel) # for GMG
    img = cv2.bitwise_and(frame, fgmask)



    cv2.imshow("Image", frame)
    cv2.imshow("FGmask", fgmask)
    cv2.imshow("FGmasked", img)

    k= cv2.waitKey(40) & 0xFF
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

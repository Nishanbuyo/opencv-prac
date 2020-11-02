import cv2 
import numpy as np

img=cv2.imread('images/shapes.png')
img= cv2.resize(img,(512,512))
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imggray, 10, 255 , cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.018 * cv2.arcLength(contour, closed=True), closed=True)
    cv2.drawContours(img, [approx], 0, (0,0,255), 3)
    x= approx.ravel()[0]
    y= approx.ravel()[1]
    
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_SIMPLEX, .4, (255,255,255), 1)
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        if (aspectRatio >=0.80 and aspectRatio <=1.20):
            cv2.putText(img, "Square", (x,y), cv2.FONT_HERSHEY_SIMPLEX, .4, (255,255,255), 1)
        else:
            cv2.putText(img, "Rectangle", (x,y), cv2.FONT_HERSHEY_SIMPLEX, .4, (255,255,255),1)
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x,y), cv2.FONT_HERSHEY_SIMPLEX, .4, (255,255,255), 1)
    elif len(approx) == 6:
        cv2.putText(img, "Hexagon", (x,y), cv2.FONT_HERSHEY_SIMPLEX, .4, (255,255,255), 1)
    # elif len(approx) == 8:
    #     cv2.putText(img, "Octagon", (x,y), cv2.FONT_HERSHEY_SIMPLEX, .4, (255,255,255), 1)
    elif len(approx) == 10:
        cv2.putText(img, "Star", (x,y), cv2.FONT_HERSHEY_SIMPLEX, .4, (255,255,255), 1)
    else:
        cv2.putText(img, "Circle", (x,y), cv2.FONT_HERSHEY_SIMPLEX, .4, (255,255,255), 1)
cv2.imshow("Shapes", img)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

cv2.destroyAllWindows()
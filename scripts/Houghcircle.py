import cv2
import numpy as np

img= cv2.imread("../images/shapes.png")
cv2.imshow("Gry", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
gray= cv2. medianBlur(gray, 5)

circles=cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1= 50, param2= 30, minRadius= 0, maxRadius=0)

detected_circle = np.uint16(np.around(circles))

for circle in detected_circle:
    for x, y, r in circle:
        cv2.circle(img, (x,y), r, (0,255,255), 1)
        cv2.circle(img, (x,y), 2, (0,255,0), 3)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

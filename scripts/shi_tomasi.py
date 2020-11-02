import cv2
import numpy as np

img= cv2.imread("../images/shapes.png")
cv2.imshow("Original Image", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)  # harris corner method takes float32 
corners = cv2.goodFeaturesToTrack(gray, 35, 0.01, 10)
corners = np.int64(corners)
print(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (255,255,255), -1 )

cv2.imshow("Cornered Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

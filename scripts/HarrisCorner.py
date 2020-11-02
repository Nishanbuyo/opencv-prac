import cv2
import numpy as np

img= cv2.imread("../images/shapes.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)  # harris corner method takes float32 
output = cv2.cornerHarris(gray, 3, 3, 0.04)
print(output)

output = cv2.dilate(output, None)
img[output >0.01 * output.max()] = [0, 255, 0]

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

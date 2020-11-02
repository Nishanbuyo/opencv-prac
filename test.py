import cv2
import numpy as np

# img= cv2.imread("../images/img")
img = np.zeros((255,255), dtype = np.uint8)
print(img.shape)
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print(color.shape)


cv2.imshow("Image", img)
cv2.imshow("Imagee", color)

cv2.waitKey(0)
cv2.destroyAllWindows()

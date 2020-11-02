import cv2 
import numpy as np
from matplotlib import pyplot as plt

# img = np.zeros((200, 200), np.uint8)
img= cv2.imread("images/lena.jpg", 0)
# b, g, r = cv2.split(img)
# cv2.imshow("Image", img)
# cv2.imshow("Blue", b)
# cv2.imshow("Green", g)
# cv2.imshow("Red", r)
# # cv2.rectangle(img, (10,20), (100, 100), (255,255,255), -1)
# # cv2.rectangle(img, (10,20), (100, 100), (0,255,255), 10)


# # plt.hist(img.ravel(), 256, [0,256])
# plt.hist(b.ravel(), 256, [0,256])
# plt.hist(g.ravel(), 256, [0,256])
# plt.hist(r.ravel(), 256, [0,256])

hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
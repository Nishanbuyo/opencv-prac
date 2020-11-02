import cv2
import numpy as np

img= cv2.imread("../images/photo.jpg")
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread("../images/photo_face.jpg", 0)
cv2.imshow("Image", img)
cv2.imshow("Template", template)
w, h = template.shape [::-1]

# res = cv2.matchTemplate(grey, template, cv2.TM_CCOEFF_NORMED)
res = cv2.matchTemplate(grey, template, cv2.TM_CCORR_NORMED)
print(res)
threshold = 0.999
pos = np.where(res >=threshold)
print(pos)
for point in zip(*pos[::-1]):
    cv2.rectangle(img, point, (point[0]+ w, point[1]+h), (0, 255,0), 3)


cv2.imshow("Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

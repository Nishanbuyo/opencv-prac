import cv2
import numpy as np

img1=cv2.imread("images/face.jpeg")
img2=cv2.imread("images/photo.jpg")
img1=cv2.resize(img1, (512,512))
img2=cv2.resize(img2, (512,512))

r=cv2.selectROI(img1, fromCenter=False)
imCrop = img1[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

# img=cv2.add(img1, img2)
img=cv2.addWeighted(img1,.7, img2, .8, 0)
cv2.imshow("Roi", imCrop)
cv2.imshow("Merged image", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
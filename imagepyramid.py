import cv2 
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('images/lena.jpg')
layer= img.copy()
gp = [layer]

for i in range(5):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)
# lr1 = cv2.pyrDown(img)
# lr2=cv2.pyrDown(lr1)
# hr2=cv2.pyrUp(lr2)
 
# cv2.imshow("Original Image", img)
# cv2.imshow("pyrDown1", lr1)
# cv2.imshow("pyrDown2", lr2)
# cv2.imshow("pyrUp2", hr2)

layer= gp[-1]
cv2.imshow('upper level Gaussian Pyramid', layer)
lp= [layer]
for i in range(4, 0, -1):
    size = (gp[i - 1].shape[1], gp[i - 1].shape[0])
    gaussian_extended = cv2.pyrUp(gp[i], dstsize=size)
    laplacian= cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian) 

cv2.waitKey(0)
cv2.destroyAllWindows() 
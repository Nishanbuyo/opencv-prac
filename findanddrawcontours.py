import cv2 
import numpy as np

img=cv2.imread('images/lena.jpg')
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imggray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0,255,255), 1) # -1 means draw all contours

cv2.imshow('Image', img)
cv2.imshow('Image Gray', imggray)
cv2.waitKey(0)
cv2.destroyAllWindows()
import numpy as np
import cv2

def nothing(x):
    pass


cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("US", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 0, 255, nothing)

while True:
    img=cv2.imread('images/balls.jpg')

    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    l_h= cv2.getTrackbarPos("LH", "Tracking")
    l_s= cv2.getTrackbarPos("LS", "Tracking")
    l_v= cv2.getTrackbarPos("LV", "Tracking")
    u_h= cv2.getTrackbarPos("UH", "Tracking")
    u_s= cv2.getTrackbarPos("US", "Tracking")
    u_v= cv2.getTrackbarPos("UV", "Tracking")

    l_b=np.array([l_h, l_s, l_v])
    # l_b=np.array([110, 50, 50])
    u_b=np.array([u_h, u_s, u_v])
    # u_b=np.array([130, 255, 255])

    mask=cv2.inRange(hsv, l_b, u_b)

    res=cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('image', img)
    cv2.imshow('res', res)
    cv2.imshow('mask', mask)

    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
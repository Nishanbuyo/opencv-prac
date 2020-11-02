import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('image')
switch= "0: default  1: gray" 
cv2.createTrackbar(switch, 'image', 0,1, nothing)
while(1):
    img= cv2.imread("images/butterfly.jpg")
    s=cv2.getTrackbarPos(switch, 'image')
    print(s)
    
    if(s==0):
        pass
    else:
        img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('image', img)

    k= cv2.waitKey(1) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()

import numpy as np
import cv2

def click_event(event, x, y, flag, param):
    if event== cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 3, (255,255,0), -1)
        points.append((x,y))
        if(len(points)>=2):
            cv2.line(img, points[-1], points[-2], (255,0,0), 5)
        # font= cv2.FONT_HERSHEY_SIMPLEX
        cv2.imshow('image', img)

    if event== cv2.EVENT_RBUTTONDOWN:
        blue= img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font= cv2.FONT_HERSHEY_SIMPLEX
        text = '(' + str(blue) + ',' + str(green) + ',' + str(red) +')'
        cv2.putText(img, text, (x,y), font, .4, (0,255,0), 1)
        cv2.imshow('image', img)
    if event == cv2.EVENT_MBUTTONDOWN:
        blue= img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        color=np.zeros((512,512,3), dtype=np.uint8)
        color[:] = [blue, green, red]

        cv2.imshow("color", color)

# img=np.zeros([512,512,3], dtype=np.uint8)
img = cv2.imread("images/photo.jpg")
cv2.imshow('image', img)
points=[]
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
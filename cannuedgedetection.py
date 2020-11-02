import cv2 
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    pass


cv2.namedWindow("Tracking Bar")
cv2.createTrackbar("threshold1", "Tracking Bar", 0, 100, nothing)
cv2.createTrackbar("threshold2", "Tracking Bar", 0, 100, nothing)
while True:
    img=cv2.imread('images/sudoku.png', cv2.IMREAD_GRAYSCALE)
    
    th1= cv2.getTrackbarPos("threshold1", "Tracking Bar")
    th2= cv2.getTrackbarPos("threshold2", "Tracking Bar")
    print(th1, th2)
    canny= cv2.Canny(img, th1, th2)
    titles= ["image", "Canny"]
    images= [img, canny]
    for i in range(2):
        # cv2.imshow("image",images[i])
        plt.subplot(1,2, i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()
    



cv2.destroyAllWindows()
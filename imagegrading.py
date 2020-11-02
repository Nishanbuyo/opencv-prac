import cv2 
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('images/photo.jpg', cv2.IMREAD_GRAYSCALE)
lap= cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap= np.uint8(np.absolute(lap))
sobelX= cv2.Sobel(img, cv2.CV_64F, dx=1, dy=0, ksize=3)
sobelY= cv2.Sobel(img, cv2.CV_64F, dx=0, dy=1, ksize=3)
canny= cv2.Canny(img, threshold1=100, threshold2=200)

sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))

combinedsobel = cv2.bitwise_or(sobelX, sobelY)

titles= ["image", "laplacian", "sobleX", "sobelY", "sobel Combined", "Canny"]
images= [img, lap, sobelX, sobelY, combinedsobel, canny]
for i in range(6):
    plt.subplot(2,3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.destroyAllWindows()

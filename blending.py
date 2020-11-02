import cv2 
import numpy as np
from matplotlib import pyplot as plt

apple=cv2.imread('images/apple.jpg')
orange=cv2.imread('images/orange.jpg')

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

#Generate Gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy= cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

#Generate Gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy= cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

#Generate Laplacian pyramid for apple
apple_copy= gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0,-1):
    size = (gp_apple[i - 1].shape[1], gp_apple[i - 1].shape[0])
    gaussian_expanded = cv2.pyrUp(gp_apple[i], size)
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_expanded)
    lp_apple.append(laplacian)

#Generate Laplacian pyramid for orange
orange_copy= gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0,-1):
    size = (gp_orange[i - 1].shape[1], gp_orange[i - 1].shape[0])
    gaussian_expanded = cv2.pyrUp(gp_orange[i], size)
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_expanded)
    lp_orange.append(laplacian)

#Add left and right halves of images
apple_orange_pyramid = []
n=0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n+=1
    cols, rows, ch = apple_lap.shape
    laplacian=np.hstack((apple_lap[:, 0: int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# Reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    size= (apple_orange_pyramid[i].shape[1], apple_orange_pyramid[i].shape[0])
    # print(size)
    apple_orange_reconstruct= cv2.pyrUp(apple_orange_reconstruct, dstsize=size)
    apple_orange_reconstruct=cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)
print(apple_orange_reconstruct.shape)
cv2.imshow("Apple", apple)
cv2.imshow("Orange", orange)
cv2.imshow("Apple_orange", apple_orange)
cv2.imshow("Apple_orange Reconstruct", apple_orange_reconstruct)



cv2.waitKey(0)
cv2.destroyAllWindows() 

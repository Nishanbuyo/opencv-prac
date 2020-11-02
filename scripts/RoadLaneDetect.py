import cv2
import numpy as np
import matplotlib.pyplot as plt

def ROI(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def drawline(image, lines):
    if lines is None:
        return
    img = np.copy(image)
    blank_image = np.zeros_like(img)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0,255,0), 6)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img


img= cv2.imread("../images/Lane2.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img.shape)
height = img.shape[0]
width = img.shape[1]

ROI_vertices= [ (0, height), (width/2, 5/7 * height), (width, height)]


gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(gray_image, 100, 200)
cropped_image = ROI(canny_image, np.array([ROI_vertices], np.int32))

lines = cv2.HoughLinesP(cropped_image, rho= 6, theta= np.pi/180, threshold= 160, lines= np.array([]), minLineLength= 40, maxLineGap=25)

image_with_line = drawline(img, lines) 

image = [img, canny_image, cropped_image, image_with_line]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(image[i])

plt.figure()
plt.imshow(image_with_line)

plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()

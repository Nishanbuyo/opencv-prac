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
            cv2.line(blank_image, (x1, y1), (x2, y2), (0,255,0), 10)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

def process(img):
    height = img.shape[0]
    width = img.shape[1]

    ROI_vertices= [ (100, height), (width/2, 2.97/4 * height), (width-100, height)]


    gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 120)
    cv2.imshow("Canny", canny_image)
    cropped_image = ROI(canny_image, np.array([ROI_vertices], np.int32))
    cv2.imshow("Cropped", cropped_image)

    lines = cv2.HoughLinesP(cropped_image, rho= 6, theta= np.pi/60, threshold= 120, lines= np.array([]), minLineLength= 20, maxLineGap=50)

    image_with_line = drawline(img, lines) 
    return image_with_line

cap = cv2. VideoCapture("../videos/LaneDetection.mp4")
while(cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    if frame is None:
        continue
    cv2.imshow("Lane Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

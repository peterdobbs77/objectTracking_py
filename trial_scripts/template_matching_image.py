import cv2.cv2 as cv2
import numpy as np

img = cv2.imread('full1.jpg', cv2.IMREAD_GRAYSCALE)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('temp12.jpg', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
loc = np.where(res >= 0.7)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)
cv2.imshow("Frame", img)

import cv2.cv2 as cv2
import sys
import numpy as np
import glob


def filter_white_only(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 120])
    upper = np.array([255, 80, 255])
    # Threshold the HSV image to get only white colors
    white_threshold = cv2.inRange(hsv, lower, upper)
    #cv2.imshow("white_threshold", white_threshold)
    return white_threshold


video = cv2.VideoCapture('vid/handblock_30fps.mp4')
backSub = cv2.createBackgroundSubtractorMOG2()
templates = [cv2.imread(file, cv2.IMREAD_GRAYSCALE)
             for file in glob.glob('templates/temp*.jpg')]

while True:
    ok, frame = video.read()
    if not ok:
        break

    # # WHITE FILTERING - does not work :(
    # #     maybe because the color thresholds are bad...
    # #     OR the template needs to be filtered...
    # #     OR background subtraction should come before...
    # whMask = filter_white_only(frame)
    # frame2 = cv2.bitwise_and(frame, frame, mask=whMask)
    # #cv2.imshow("whMask", whMask)

    # BACKGROUND SUBTRACTION
    fgMask = backSub.apply(frame)
    #cv2.imshow("fgMask", fgMask)
    frame2 = cv2.bitwise_and(frame, frame, mask=fgMask)

    # TEMPLATE MATCHING
    gray_frame = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    for tmp in templates:
        w, h = tmp.shape[::-1]
        res = cv2.matchTemplate(gray_frame, tmp, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.7)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()

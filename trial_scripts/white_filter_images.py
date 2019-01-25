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


templates = [cv2.imread(file)
             for file in glob.glob('templates/temp*.jpg')]

for tmp in templates:
    mask = filter_white_only(tmp)
    img = cv2.bitwise_and(tmp, tmp, mask=mask)
    cv2.imshow('img', img)

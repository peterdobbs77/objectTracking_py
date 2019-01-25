from __future__ import print_function
import cv2.cv2 as cv2
# this uses 3.4.5
import argparse
import numpy as np


def filter_white_only(frame):
    global res
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of white color in HSV
    #   To get white:
    #       Hue doesn't matter
    #       Saturation should be a low number
    #       Value should be a high number
    lower = np.array([0, 0, 135])
    upper = np.array([255, 70, 255])

    # Threshold the HSV image to get only white colors
    mask = cv2.inRange(hsv, lower, upper)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('res', res)


backSub = cv2.createBackgroundSubtractorMOG2()
#backSub = cv.createBackgroundSubtractorKNN()

capture = cv2.VideoCapture('vid/handblock.mp4')

while True:
    ret, frame = capture.read()
    if frame is None:
        break

    cv2.imshow('Frame', frame)

    # [apply]
    # update the background model
    #fgMask = backSub.apply(frame)
    fgMask = backSub.apply(frame)
    cv2.imshow('FG Mask', fgMask)
    frame2 = cv2.bitwise_and(frame, frame, mask=fgMask)
    # [apply]

    filter_white_only(frame2)

    # [display_frame_number]
    # get the frame number and write it on the current frame
    cv2.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
    cv2.putText(frame, str(capture.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    # [display_frame_number]

    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

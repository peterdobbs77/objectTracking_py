from __future__ import print_function
import cv2 as cv
import argparse

backSub = cv.createBackgroundSubtractorMOG2()
#backSub = cv.createBackgroundSubtractorKNN()

capture = cv.VideoCapture('vid/trimed.mp4')

while True:
    ret, frame = capture.read()
    if frame is None:
        break

    # [apply]
    # update the background model
    fgMask = backSub.apply(frame)
    # [apply]

    # [display_frame_number]
    # get the frame number and write it on the current frame
    cv.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    # [display_frame_number]

    # [show]
    # show the current frame and the fg masks
    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)
    # [show]

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

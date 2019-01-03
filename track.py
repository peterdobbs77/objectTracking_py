from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import numpy as np
import time
import sys
import cv2.cv2 as cv2


def filter_white_only(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 120])
    upper = np.array([255, 80, 255])

    # Threshold the HSV image to get only white colors
    white_threshold = cv2.inRange(hsv, lower, upper)
    return white_threshold


def make_mask(frame):
    #fgMask = backSub.apply(frame)
    #frame = cv2.bitwise_and(frame, frame, mask=fgMask)
    mask = filter_white_only(frame)
    return mask


backSub = cv2.createBackgroundSubtractorMOG2()
tracker = cv2.TrackerTLD_create()
# if errors here, run > pip install opencv-contrib-python

video = cv2.VideoCapture('vid/pickup_and_go.mp4')

ok, frame = video.read()
if not ok:
    print('Cannot read video file')
    sys.exit()

frame = imutils.resize(frame, width=1200)
mask = make_mask(frame)
bbox = cv2.selectROI(frame, False)
tracker.init(mask, bbox)

# loop over frames from video
while True:
    ok, frame = video.read()
    if not ok:
        break

    frame = imutils.resize(frame, width=1200)
    mask = make_mask(frame)

    # grab the new bounding box coordinates of the object
    (success, box) = tracker.update(mask)

    # check to see if the tracking was a success
    if success:
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # template matching

    # show the output frame
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()

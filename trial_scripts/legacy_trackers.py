from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import numpy as np
import time
import sys
import cv2 as cv

TRACKER_TYPES = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
def GET_TRACKER(tracker_type):
    if tracker_type == 'BOOSTING':
        tracker = cv.legacy.TrackerBoosting_create() # requires grayscale
    elif tracker_type == 'MIL':
        tracker = cv.legacy.TrackerMIL_create()
    elif tracker_type == 'KCF':
        tracker = cv.legacy.TrackerKCF_create()
    elif tracker_type == 'TLD':
        tracker = cv.legacy.TrackerTLD_create()
    elif tracker_type == 'MEDIANFLOW':
        tracker = cv.legacy.TrackerMedianFlow_create()
    elif tracker_type == 'GOTURN':
        tracker = cv.legacy.TrackerGOTURN_create()
    elif tracker_type == 'MOSSE':
        tracker = cv.legacy.TrackerMOSSE_create()
    elif tracker_type == "CSRT":
        tracker = cv.legacy.TrackerCSRT_create()
    else:
        raise ValueError(f"Invalid tracker choice. Please select from {TRACKER_TYPES}.")
    return tracker

def filter_white_only(frame):
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower = np.array([0, 0, 120])
    upper = np.array([255, 80, 255])

    # Threshold the HSV image to get only white colors
    white_threshold = cv.inRange(hsv, lower, upper)
    return white_threshold


def make_mask(frame):
    #fgMask = backSub.apply(frame)
    #frame = cv.bitwise_and(frame, frame, mask=fgMask)
    mask = filter_white_only(frame)
    return mask


# backSub = cv.createBackgroundSubtractorMOG2()

# if errors here, run > pip install opencv-contrib-python

video = cv.VideoCapture('vid/pickup_and_go_30fps.mp4')

ok, frame = video.read()
if not ok:
    print('Cannot read video file')
    sys.exit()

frame = imutils.resize(frame, width=1200)

# User: Select ROI
#   disc should be around (872, 535, 32, 28) for 'vid/pickup_and_go_30fps.mp4'
bbox = cv.selectROI("Select ROI", frame, False)
cv.destroyWindow("Select ROI")
print(bbox)

mask = make_mask(frame)
tracker_type = TRACKER_TYPES[7]
print(f"Using tracker type: {tracker_type}")
tracker = GET_TRACKER(tracker_type)
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
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        # tracking failure
        cv.putText(frame, "Tracking failure detected", (100,80), cv.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

    # TODO: template matching

    # show the output frame
    cv.imshow("Tracking", frame)

    key = cv.waitKey(1) & 0xFF
    if key == ord("q"):
        break

video.release()
cv.destroyAllWindows()

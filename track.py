# based on https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/
#   author: Adrian Rosebrock
#   date:   30 July 2018
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import numpy as np
import time
# get opencv: https://stackoverflow.com/questions/24415069/is-opencv-supported-on-python-3-yet
import cv2  # https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv
# we are using OpenCV version 3.4.5

tracker = cv2.TrackerCSRT_create()
# if errors here, run > pip install opencv-contrib-python

# initialize some stuff
initBB = None  # bounding box
fps = None    # frames per second throughput estimator

#
vs = cv2.VideoCapture('vid/handblock.mp4')

# loop over frames from video
while True:
    frame = vs.read()

    if frame is None:
        break

    print(frame)

    frame = imutils.resize(frame, width=500)
    (Ht, Wd) = np.array(frame, dtype=object).shape[:2]

    # check to see if we are currently tracking an object
    if initBB is not None:
        # grab the new bounding box coordinates of the object
        (success, box) = tracker.update(frame)

        # check to see if the tracking was a success
        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h),
                          (0, 255, 0), 2)

        # update the FPS counter
        fps.update()
        fps.stop()

        # initialize the set of information we'll be displaying on
        # the frame
        info = [
            ("Tracker", "CSRT"),
            ("Success", "Yes" if success else "No"),
            ("FPS", "{:.2f}".format(fps.fps())),
        ]

        # loop over the info tuples and draw them on our frame
        for (i, (k, v)) in enumerate(info):
            text = "{}: {}".format(k, v)
            cv2.putText(frame, text, (10, Ht - ((i * 20) + 20)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

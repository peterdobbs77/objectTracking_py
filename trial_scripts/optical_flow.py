import numpy as np
import cv2 as cv
# from ultralytics import YOLO
import argparse

parser = argparse.ArgumentParser(description='This sample demonstrates Lucas-Kanade Optical Flow calculation.')
parser.add_argument('video', type=str, help='path to video file')
args = parser.parse_args()

# random colors for tracing
color = np.random.randint(0, 255, (100, 3))

# Load the video
cap = cv.VideoCapture(args.video)

# check that first frame
ret, old_frame = cap.read()
if not ret:
    print("Failed to read video")
    cap.release()
    exit()

# User: select ROI
roi = cv.selectROI("Select ROI", old_frame, False)
cv.destroyWindow("Select ROI")

# setup ROI
x, y, w, h = roi
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
roi_gray = old_gray[y:y+h, x:x+w]

# find good features to track in user selected ROI
p0 = cv.goodFeaturesToTrack(
    roi_gray,
    mask = None,
    maxCorners = 100,
    qualityLevel = 0.3,
    minDistance = 7,
    blockSize = 7
)
if p0 is not None:
    p0 += np.array([[x, y]], dtype = np.float32)
print(p0)

# # params for lucas kanade optical flow
# lk_params = dict(winSize  = (15, 15),
#                  maxLevel = 2,
#                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

# Create an image mask for drawing
mask = np.zeros_like(old_frame)

while True:
    ret, frame = cap.read()
    if not ret:
        print('No frames grabbed! :(')
        break

    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    if p0 is not None:
        # calculate optical flow
        p1, status, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None)#, **lk_params)

        # Select good points
        if p1 is not None:
            good_new = p1[status==1]
            good_old = p0[status==1]

        # draw the tracks
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv.line(mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2)
            frame = cv.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)
        
        frame = cv.add(frame, mask)

    cv.imshow('frame', frame)
    k = cv.waitKey(30) & 0xff
    if k == 27: # ESC to exit
        break

    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)

cap.release()
cv.destroyAllWindows()
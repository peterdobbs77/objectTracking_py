import cv2.cv2 as cv2


video = cv2.VideoCapture('./vid/eye.mp4')

while True:
    ok, frame = video.read()

    if not ok:
        break

    cv2.imshow("Original", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

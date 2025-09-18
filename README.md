# objectTracking_py

Built on Python 3.12.0 64-bit <br>
Uses OpenCV 4.5<br>

## Introduction

Start out with [detection_demo](./detection_demo.ipynb) to get a sense of what's going on here.

## Setup
Use pip to install the full, OpenCV package

'''
[py -m] pip install opencv-contrib-python
'''

Disclaimer: Make sure that you do not have it installed along with other distributions or versions of OpenCV.

## Examples

### Find Frisbee after Handblock
* Original, cropped and resized to 60% and 15 fps
![Frisbee Detection Demo](demo/handblock.gif)

* User-selected ROI (region of interest) detection and white filtering from [track.py](track.py)
![ROI Detection](demo/pickup_and_go_30fps_track_py_annotated.gif)

## Works Consulted (References):

Mohamed Samir<br>
https://github.com/mohamedsamirx/Real-time-object-tracking-demo

Harrison [at] pythonprogramming [dot] net
https://pythonprogramming.net/template-matching-python-opencv-tutorial/

Adrian Rosebrock<br>
https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/

Satya Mallick<br>
https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/
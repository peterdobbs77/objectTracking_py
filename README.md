# objectTracking_py

Built on Python 3.7.0 64-bit <br>
Uses OpenCV 3.4.5<br>

## Setup
Use pip to install the full, **unofficial** OpenCV package

'''
[py -m] pip install opencv-contrib-python
'''

Disclaimer: this **unofficial** distribution is not approved or supported by the creators of OpenCV. Make sure that you do not have it installed along with other distributions or versions of OpenCV.


## Examples

### Find Frisbee after Handblock
* Original, cropped and resized to 60% and 15 fps
![Frisbee Detection Demo](demo/handblock.gif)

* User-selected ROI (region of interest) detection and white filtering from [track.py](track.py)
![ROI Detection](demo/pickup_and_go_30fps_track_py_annotated.gif)

## Works Consulted (References):
Harrison [at] pythonprogramming [dot] net
https://pythonprogramming.net/template-matching-python-opencv-tutorial/

Adrian Rosebrock<br>
https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/

Satya Mallick<br>
https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.patches import Polygon

from skimage.measure import find_contours
from sklearn.model_selection import train_test_split
from imgaug import augmenters as iaa

import numpy as np

import os
import sys
import random
import copy
import math
import cv2
import collections
import json
import glob

%matplotlib inline

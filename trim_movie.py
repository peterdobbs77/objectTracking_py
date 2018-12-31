from moviepy.editor import *
import sys

video = VideoFileClip('vid/example.mp4').subclip(8.5, 15)

video.write_videofile('vid/trimed.mp4')

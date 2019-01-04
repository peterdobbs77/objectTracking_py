from moviepy.editor import *
import sys

video = VideoFileClip('vid/example.mp4').subclip(5, 10)
video.write_videofile('vid/trimed.mp4', fps=30)

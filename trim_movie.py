from moviepy.editor import *

video = VideoFileClip('vid/example.mp4').subclip(0, 15)
video.write_videofile('vid/trimed.mp4')

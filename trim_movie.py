from moviepy.editor import *
import sys

video = VideoFileClip('vid/example.mp4').subclip(5, 10)
video.write_videofile('vid/trimed.mp4', fps=30)

# cropped = moviepy.video.fx.all.crop(video, x1=100, x2=950, y1=100, y2=900)
# cropped.write_videofile('./video_output.mp4')

# audio = video.audio
# audio.write_audiofile('./audio_output.mp3')

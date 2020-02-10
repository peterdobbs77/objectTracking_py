from moviepy.editor import *

clip = (VideoFileClip("vid/handblock_60fps.mp4")
        .crop(x1=600, y1=300)
        .resize(0.6))
clip.write_gif('demo/handblock.gif', fps=15)

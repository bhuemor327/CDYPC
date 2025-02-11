from moviepy.editor import *

video = VideoFileClip("video_ejemplo.mp4").rotate(180)
video.write_videofile("rotado.mp4")

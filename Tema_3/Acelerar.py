from moviepy.editor import *

#El número 2 hace referencia al factor de velocidad
video = VideoFileClip("video_ejemplo.mp4").fx(vfx.speedx, 2)
video.write_videofile("video_rapido.mp4")
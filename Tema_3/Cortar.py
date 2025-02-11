from moviepy.editor import *

video = VideoFileClip("video_ejemplo.mp4")

#Los números 1 y 2 representan los segundos del video donde se realiza el corte.
cortado = video.subclip(1, 2)
cortado.write_videofile("video_cortado.mp4")
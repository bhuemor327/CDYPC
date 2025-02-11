from moviepy.editor import *
#Cargamos el primer video
clip1 = VideoFileClip("video1.mp4")

#Cargamos el segundo video cortado
clip2 = VideoFileClip("video2.mp4").subclip(5,20)

#Cargamos el tercer video
clip3 = VideoFileClip("video3.mp4")

#Concatenamos los 3
final_clip = concatenate_videoclips([clip1,clip2,clip3])
final_clip.write_videofile("resultado.mp4")
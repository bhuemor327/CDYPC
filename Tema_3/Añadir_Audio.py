from moviepy.editor import *

video = VideoFileClip("video_ejemplo.mp4")
audio_fondo = AudioFileClip("intro.mp3").subclip(0, video.duration)  # Ajustar la duración del audio
video_con_audio = video.set_audio(audio_fondo)
video_con_audio.write_videofile("video_final_con_audio.mp4")


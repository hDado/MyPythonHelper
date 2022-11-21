#   This script set a new audio to original video of presentation :
''' This script is used to generate a new audio for a video clip, sounds is modified original audio from mp4 video'''
from moviepy.editor import *
videoclip = VideoFileClip("filename.mp4")
audioclip = AudioFileClip("sounds.mp3")

new_audioclip = CompositeAudioClip([audioclip])
videoclip.audio = new_audioclip
videoclip.write_videofile("new_filename.mp4")
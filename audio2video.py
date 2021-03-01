from moviepy.editor import *

# Import the audio(Insert to location of your audio instead of audioClip.mp3)
audio = AudioFileClip(r"C:\Users\91998\Documents\abc.mp3")
# Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)
clip = ImageClip(r"C:\Users\91998\Documents\abc.jpg").set_duration(audio.duration)
# Set the audio of the clip
clip = clip.set_audio(audio)
# Export the clip
clip.write_videofile(r"C:\Users\91998\Documents\abc.mp4", fps=0.1)

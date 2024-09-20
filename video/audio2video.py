from moviepy.editor import *
from os import listdir
from os.path import isfile, join

def convert(inDir, imagePath, outDir):

    onlyfiles = [f for f in listdir(inDir) if isfile(join(inDir, f))]

    for mp3File in onlyfiles:
        if(mp3File.endswith(".mp3")):
            filePath = inDir + mp3File
            audio = AudioFileClip(filePath)
            clip = ImageClip(imagePath).set_duration(audio.duration)        
            fileName = outDir + os.path.splitext(mp3File)[0] + '.mp4'
            clip = clip.set_audio(audio)
            clip.write_videofile(fileName, fps=0.1)

def joinVideo(inputdirectory):

    onlyfiles = [f for f in listdir(inputdirectory) if isfile(join(inputdirectory, f))]

    clips = []
    for videofile in onlyfiles:
        if(videofile.endswith(".mp4")):
            filepath = inputdirectory + videofile
            clip = VideoFileClip(filepath)
            clips.append(clip)
    
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(inputdirectory+'joined-video.mp4')

if __name__=="__main__":    
    inDir = r"C:\Users\anshul\Documents\\"
    imagePath = r"C:\Users\anshul\Documents\myimage.jpg"
    outDir = r"C:\Users\anshul\Documents\\"
    convert(inDir, imagePath, outDir)
    joinVideo(outDir)

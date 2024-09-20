#!/usr/bin/env python
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os, re, argparse

def main():    
    inputFile = "/Users/anshul/Downloads/output/to-cut.mp4"    
    outputLocation = "/Users/anshul/Downloads/output/"
    # split(inputFile, outputLocation)
    join()


def split(vidfile, output):
    clip = VideoFileClip(vidfile).subclip(55,135)    
    output = output + 'part.mp4'
    clip.write_videofile(output, audio=False)
    

def join():    
    folder_prefix = '/Users/anshul/Downloads/output/'
    # numbers = re.compile(r'(\d+)')

    # this two lines are for loading the videos. In this case the video are named as: cut1.mp4, cut2.mp4, ..., cut15.mp4
    videofiles = [n for n in os.listdir(folder_prefix) if n[0]=='o' and n[-4:]=='.avi']
    # videofiles = sorted(videofiles, key=numericalSort)
    print(videofiles)
    video_index = 0

    clips = []
    while(video_index < len(videofiles)):
        print('processing file: {}'.format(videofiles[video_index]))    
        clips.append(VideoFileClip(folder_prefix+videofiles[video_index]))
        video_index += 1

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(folder_prefix+'joined-video.mp4')
    print("end.")


def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

if __name__=="__main__":
    main()
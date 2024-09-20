#!/usr/bin/env python

from pytube import YouTube
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--link", type=str, required=True, help="You Tube Link")
args = vars(ap.parse_args())

youtube_link = args["link"]

# YouTube(youtube_link).streams.first().download()
yt = YouTube(youtube_link)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first().download()
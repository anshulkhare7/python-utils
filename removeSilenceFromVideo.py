from auto_everything.video import video
import os

video = Video()

video.humanly_remove_silence_parts_from_video("/ap.mp4", "/ap-silence.mp4", 25, minimum_interval=0.7)
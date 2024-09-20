from moviepy.editor import *
  
# getting subclip as video is large
clip1 = VideoFileClip("/Users/anshul/Downloads/fal-aur-bandariya.mp4")
# clip2 = VideoFileClip("/Users/anshul/Downloads/fal-aur-bandariya.mp4")
# clip3 = VideoFileClip("/Users/anshul/Downloads/PAF_new_web_arch_training_part-3.mp4")
# clip4 = VideoFileClip("/Users/anshul/Downloads/output/large-4k-video-4.mp4")
 
# concatenating both the clips
final = concatenate_videoclips([clip1, clip1])
#writing the video into a file / saving the combined video
final.write_videofile("/Users/anshul/Downloads/fal-aur-bandariya-long.mp4")
import cv2, argparse, os, sys, ntpath

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="video file name")
args = vars(ap.parse_args())

input_path = args["input"]
video_file_name = ntpath.basename(input_path)
folder_location = ntpath.dirname(input_path)
video_file_location = input_path
output_path = folder_location + "/frames/" + video_file_name.split(".avi")[0]

vidcap01 = cv2.VideoCapture(video_file_location)

image_present,image = vidcap01.read()
count = 1
frames_captured = 0
while image_present:  
  print('Read a new frame: ', count)    
  if(image_present):
    output_file = output_path + "" + str("-%d.jpg" % count)
    cv2.imwrite(output_file, image)
    frames_captured += 1
    print('Captured a new frame: ', frames_captured)    
  image_present,image = vidcap01.read()
  count += 1

print('Frames found: '+str(count))
print('Frames captured: '+str(frames_captured))

vidcap01.release()
import cv2, time

def main():
    checkVideoFPS()
    checkCamFPS()

def checkVideoFPS():
     
    video = cv2.VideoCapture("/Users/anshul/Freelancing/Innocule/data/dumping-webcamshots/North-15Apr-1600hrs/North-15Apr-1600hrs.mp4");
     
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
     
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print('Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): ', str(fps))
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print('Frames per second using video.get(cv2.CAP_PROP_FPS): ', str(fps))        
     
    video.release()

def checkCamFPS():
    # Start default camera
    video = cv2.VideoCapture(0);
     
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
     
    # With webcam get(CV_CAP_PROP_FPS) does not work.
    # Let's see for ourselves.
     
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print('Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): ', str(fps))
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print('Frames per second using video.get(cv2.CAP_PROP_FPS) : ', str(fps))
     
 
    # Number of frames to capture
    num_frames = 120;
     
     
    print('Capturing ', str(num_frames), ' frames') 
 
    # Start time
    start = time.time()
     
    # Grab a few frames
    for i in range(0, num_frames) :
        ret, frame = video.read()
 
     
    # End time
    end = time.time()
 
    # Time elapsed
    seconds = end - start
    print('Time taken : ', str(seconds) ,'seconds')
 
    # Calculate frames per second
    fps  = num_frames / seconds;
    print('Estimated frames per second : ', str(fps));
 
    # Release video
    video.release()    

if __name__=="__main__":
    main()
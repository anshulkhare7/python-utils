import cv2, base64, requests, json, os, re, argparse, threading, logging
from logging.handlers import RotatingFileHandler
from os.path import expanduser

import numpy as np
from time import sleep

formatter = logging.Formatter("[%(levelname)s] (%(asctime)s) {%(filename)s:%(lineno)d} | %(name)s | %(message)s")
log_file_path = expanduser("~") + '/logs/ipcam.log'
handler = RotatingFileHandler(log_file_path, maxBytes=1000000, backupCount=2)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logger = logging.getLogger('IPCam')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


#url = 'http://localhost:8888/image/base64/'
url = 'http://one.innocule.tech/image/base64/'

def main(delay):
    ipcamThread01 = threading.Thread(target=ipcam_1, args=("rtsp://admin:innocule7@192.168.1.64", "cam_01", delay))
    ipcamThread02 = threading.Thread(target=ipcam_1, args=("rtsp://admin:innocule7@192.168.1.64", "cam_02", delay))
    ipcamThread01.start()
    ipcamThread02.start()

def ipcam_1(camUrl, camName, delay):
    logger.debug('Thread started for '+camName)
    cap = cv2.VideoCapture(camUrl)
    while(True):
        cap = cv2.VideoCapture(camUrl)
        retval, image = cap.read()
        _, im_arr = cv2.imencode('.jpg', image)
        jpg_as_text = base64.b64encode(np.array(im_arr).tostring()).decode('utf-8')
        #print(jpg_as_text[0:50])
        data = { 'image' : str(jpg_as_text), 'source' : camName}
        headers = {'Content-type': 'application/json', 'Authorization':'Basic YWRtaW46SW5ub2NAMTIz'}
        try:
            response = requests.post(url, json = data, headers = headers)
            logger.debug('Response from cloud '+response.text+ 'for cam: ' +camName)            
        except:
            logger.error("Error in sending request for cam: "+camName, exc_info=1)
        sleep(int(delay))

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    logger.debug('='*5+" Starting Applicaiton "+'='*5)
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--framedelay", required=True, type=str, help="Take frame every these many seconds")
    args = vars(ap.parse_args())
    delay = args["framedelay"]
    main(delay)
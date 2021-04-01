import cv2, base64, requests, json, os, re, argparse
import numpy as np
from time import sleep

def main(camIp, camName):    
    print(camIp)
    print(camName)
    cap = cv2.VideoCapture("rtsp://"+camIp)
    #url = 'http://localhost:8888/image/base64/'
    url = 'http://one.innocule.tech/image/base64/'

    while(cap.isOpened()):
        retval, image = cap.read()
        _, im_arr = cv2.imencode('.jpg', image)
        jpg_as_text = base64.b64encode(np.array(im_arr).tostring()).decode('utf-8')
        #print(jpg_as_text[0:50])        
        data = { 'image' : str(jpg_as_text), 'source' : camName}
        headers = {'Content-type': 'application/json', 'Authorization':'Basic YWRtaW46SW5ub2NAMTIz'}
        response = requests.post(url, json = data, headers = headers)
        print(response.text)
        break

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--cameraip", required=True, type=str, help="IP Camera host")
    ap.add_argument("-n", "--cameraname", type=str, required=True, help="Camera identifier name")
    args = vars(ap.parse_args())
    
    camIP = args["cameraip"]
    camName = args["cameraname"]

    main(camIP, camName)

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
#im_bytes = im_arr.tobytes()
# mydata = np.fromstring(image, dtype=np.uint8)     
# cv2.imwrite("abc.jpg", cap.read()[1])
#from onvif import ONVIFCamera
#mycam = ONVIFCamera('192.168.1.64', 80, 'anshul', 'innocule7', '/etc/onvif/python-onvif/wsdl')

# Get Hostname
#resp = mycam.devicemgmt.GetHostname()
#print 'My camera`s hostname: ' + str(resp.Name)
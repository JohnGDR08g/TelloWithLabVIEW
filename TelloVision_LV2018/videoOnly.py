import cv2,time

udpAdd='udp://@192.168.10.1:11111'
cap=cv2.VideoCapture(udpAdd)

if  not cap.isOpened():
    print('VideoCapture not opened, try again...')
    cap.open(udpAdd)

start=time.time()
        
while time.time()-start<25:
    print('trying to grab a frame...')
    ret, frame=cap.read()
    if frame is not None:
        break
    time.sleep(0.2)

def startcap():    
    ret, frame=cap.read()
    frame=cv2.resize(frame,(640,480),interpolation=cv2.INTER_NEAREST)
#    frame=cv2.GaussianBlur(frame,(1,1),0)
    return frame

def stopcap():    
    cap.release()
    return 0

    
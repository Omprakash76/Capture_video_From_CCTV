import cv2
import numpy as np

cam = cv2.VideoCapture("http://192.168.43.1:7777/video?x.mjpg") #use your own IP address or
#for webcam use 0 or other external camera use 1
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
vid = cv2.VideoWriter('output.avi', fourcc, 10, (width,height))
print(width)
print(height)

while(True):
    tf, frame = cam.read()
    vid.write(frame)
    cv2.imshow('Single Frame',frame)
    key = cv2.waitKey(1)
    if key == 27: #esc key
        break
    elif key == ord('x'):
        print("You have pressed the letter X")

cam.release()
vid.release()
cv2.destroyAllWindows()


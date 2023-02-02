import cv2
import numpy as np

def nothing(x):
    pass

cap=cv2.VideoCapture("hsv.mp4")
cv2.createTracbar("LH","Tracbar",0,179,nothing)
cv2.createTracbar("LS","Tracbar",0,255,nothing)
cv2.createTracbar("LV","Tracbar",0,255,nothing)
cv2.createTracbar("UH","Tracbar",0,179,nothing)
cv2.createTracbar("US","Tracbar",0,255,nothing)
cv2.createTracbar("UV","Tracbar",0,255,nothing)

while 1:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    
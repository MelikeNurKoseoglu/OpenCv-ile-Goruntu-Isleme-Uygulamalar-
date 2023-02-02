from tkinter import font
import cv2
import numpy as np


canvas=np.zeros((512,512,3),dtype=np.uint8)+255
font=cv2.FONT_HERSHEY_COMPLEX
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
font=cv2.QT_FONT_NORMAL
cv2.putText(canvas,"OpenCv",(30,50),font,3,(0,0,200),cv2.LINE_AA)


cv2.imshow("kanvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

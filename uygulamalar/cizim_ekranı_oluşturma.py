import cv2
import numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8)+255#belli alanda  tuval oluşturur


cv2.imshow("Canvas",canvas)
cv2.waitkey(0)
cv2.destroyAllWindows()
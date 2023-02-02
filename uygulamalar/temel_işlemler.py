import cv2
import numpy as np

img=cv2.imread("klon.jpg")

dimension=img.shape
print(dimension)


color=img[150,200]
print("BGR:",color)

blue=img[420,500,0]
print("blue:",blue)

red=img[420,500,2]
print("red:",red)

green=img[420,500,1]
print("green:",green)


img[420,500,2]=250
print("new blue:",img[420,500,0])

blue1=img.item(150,200,0)
print("blue1:",blue1)

img.itemset((150,200,0),172)
print("new blue1:",img[150,200,0])


cv2.imshow("klon",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
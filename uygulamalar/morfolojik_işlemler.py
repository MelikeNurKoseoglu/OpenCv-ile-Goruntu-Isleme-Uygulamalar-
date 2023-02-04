import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('samsun.jpeg')

kernel = np.ones((3,3),np.uint8)

erosion = cv2.erode(img,kernel)

dilation = cv2.dilate(img,kernel)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

titles = ["Original Image", "Erosion","Dilation", "Opening", "Closing", "Gradient" ]

images = [img, erosion, dilation,opening, closing,gradient ]

for i in range(6):
    plt.subplot(3,3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

"""
cv2.imshow('iamge',img)
cv2.imshow('diate',dilation)
cv2.imshow('erosion',erosion)
cv2.imshow('openşng',opening)
cv2.imshow('closing',closing)
cv2.imshow('titles',titles)
"""

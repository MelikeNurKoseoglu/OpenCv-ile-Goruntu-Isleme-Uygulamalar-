import cv2
import numpy as np
from matplotlib import pyplot as plt  

img = cv2.imread("klon.jpg")


b,g,r = cv2.split(img)
cv2.imshow("img",img)

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])

plt.show()

img2=np.zeros((500,500),np.uint8)
cv2.imshow("img2",img2)
plt.hist(img2.ravel(),256,[0,256])
plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

cv2.namedWindow("klon",cv2.WINDOW_NORMAL) 
img=cv2.imread("klon.jpg")

img=cv2.resize(img,(640,480)) #resim boyutlandırmak için

cv2.imshow("klon",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


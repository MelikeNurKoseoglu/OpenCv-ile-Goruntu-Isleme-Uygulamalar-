import cv2
import numpy
import matplotlib

img = cv2.imread("klon.jpg")#Resmi okur !!! Aynı dosya içinde değilse dosya yolunu ver)
#print(img)
cv2.namedWindow("Img",cv2.WINDOW_NORMAL)#Pencerenin büyümesi ve küçülmesi için
cv2.imshow("Img",img)#Resmin pencerede açılmasını sağlar
cv2.imwrite("klon1.jpg",img)# Yapılan değişiklikten sonra resmin yeni halini kaydeder
cv2.waitKey(0)#Pencerenin ekranda kalmasını sağlar
cv2.destroyAllWindows()#Tüm pencereleri kapatır

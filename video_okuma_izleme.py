import cv2


#video dosyası
cap=cv2.VideoCapture("video.mp4")
#webcam
cap=cv2.VideoCapture(0)# video okuma 0 ise webcamdam görüntü ,dosya uzantısı ise vidodan okuma

while True:
    ret,frame=cap.read()#read fonkisyonu framleri doğru okursa ret true ,yanlış okuduysa false
    if ret==0:#döngü bittiyse veya video bittiyse
        break
    frame=cv2.flip(frame,1)#alınan görüntüyü istenilen eksene göre yansıtır !!! 1 y eksnine göre yansıtma
    cv2.imshow("webcam",frame)
    if cv2.waitKey(1)& 0xFF==ord("q"):#waitkey herbir frame 1 milisaniye okunup diğer frame geçer !!! 0 olursa frame bir kez alınır
        break#q harfine basınca döngüyü kır

cap.relase()#işlemi kapatmak için
cv2.destroyAllWindows()

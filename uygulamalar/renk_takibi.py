import cv2

#renk aralıkları belirlenen renge göre değişir
bluelower=(75,100,100)
blueupper=(130,255,255)
cap=cv2.VideoCapture(0)
cap.set(3,960)
cap.set(4,480)

while True:
    success,imgOriginal=cap.read()
    if success:
        #blur
        blurred=cv2.GaussianBlur(imgOriginal,(11,11),0)
        hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV",hsv)
        mask=cv2.inRange(hsv,bluelower,blueupper)
        cv2.imshow("mask image",mask)
        mask=cv2.erode(mask,None,iterations=2)
        mask=cv2.dilate(mask,None,iterations=2)
        cv2.imshow("Mask+erozyon ve genisleme,son hal",mask)
    cv2.imshow("orjinal tespit",imgOriginal)
    if cv2.waitKey(1) & 0xFF == ord("q"):break


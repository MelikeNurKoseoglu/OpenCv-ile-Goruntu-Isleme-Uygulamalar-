import cv2

cap=cv2.VideoCapture(0)

fileName="D:\pythonOpencv\webcem.avi" # videonun kayıt ismi ve uzantısı
codec=cv2.VideoWriter_fourcc("W","M","V","2")
frameRate=30
resolution=(640,480)
VideoFileOutput=cv2.VideoWriter(fileName,codec,frameRate,resolution)#fileName video kaydedilceği yer uzantısnı verir

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    VideoFileOutput.write(frame)#okuduğu her frame değişkene yazar

    
    cv2.imshow("Webcam Live",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
VideoFileOutput.release()
cap.relase()
cv2.destroyAllWindow()

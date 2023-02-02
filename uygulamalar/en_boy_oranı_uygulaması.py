import cv2

def resizewithAspectRatio(img,witdth=None,height=None,inter=cv2.INTER_AREA):# inter=cv2.INTER_AREA default değeri
    dimension=None #resmin yeni boyutu
    (h,w)=img.shape[:2]#resim boyutuna ulaşma
    if witdth is None and height is None: #none değerde resim boyutunun aynısını döndürür
        return img
    if witdth is None:#en değerini girmezse
        r=height/float(h)
        dimension=(int(w*r),height)
    else:#boy değeri verilirse
        r=witdth/float(w)
        dimension=(witdth,int(h*r))

    return cv2.resize(img,dimension,interpolation=inter)

img=cv2.imread("klon.jpg")
img1=resizewithAspectRatio(img,witdth=None,height=600,inter=cv2.INTER_AREA)
cv2.imshow("klon",img)


cv2.waitKey(0)
cv2.destroyAllWindows

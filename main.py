import cv2
import numpy as np
#  kamerayı aç (kamera indeksi 0)

cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()    # Kameradan bir kare oku

    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)    # BGR karesini HSV renk uzayına dönüştür

    # HSV'deki kırmızı rengi belirt
    low_red=np.array([160,155,84])
    high_red=np.array([179,255,255])
    # Belirtilen aralıkta kırmızı rengi içeren bir maske oluştur
    red_mask=cv2.inRange(hsv_frame,low_red,high_red)
    # Orijinal kareye kırmızı maskesini uygula, bitwise AND işlemi kullanarak
    red=cv2.bitwise_and(frame,frame,mask=red_mask)
    # Orijinal kareyi, kırmızı filtrelenmiş kareyi ve kırmızı maskesini görüntüle
    cv2.imshow("frame",frame)
    cv2.imshow("red", red)
    cv2.imshow("maske", red_mask)
    # Döngüden çıkmak için 'Esc' tuşu kontrol et
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()

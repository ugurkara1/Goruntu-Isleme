import numpy as np
import cv2

I=cv2.imread("gri_resim.png", cv2.IMREAD_GRAYSCALE)# Gri tonlamalı resmi oku

Hist=np.zeros(256,dtype=int) # Histogram dizisini başlat


w, h = I.shape # Resmin genişliği ve yüksekliğini al
# Histogramı hesapla
for v in range(h):

    for u in range(w):
        i = I[u, v]
        Hist[i] += 1
# Histogram değerlerini yazdır
for i in range(256):
    print(i,':',Hist[i])

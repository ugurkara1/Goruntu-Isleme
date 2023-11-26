import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    # Gürültüyü azaltmak için blurlama uygula
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)

    #gri tonlamaya çevir
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray:",gray)
    #kenarları belirleme
    edges=cv2.Canny(gray,50,150)
    # Morfolojik operasyonlar uygula
    kernel = np.ones((5, 5), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)
    edges = cv2.erode(edges, kernel, iterations=1)
    #konturları bulma
    contours,_=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # Belirli bir alanın altındaki konturları göz ardı et
    min_contour_area = 500  # Belirlediğiniz bir değer
    max_contour_area = 1000  # Belirlediğiniz bir değer
    filtered_contours = [cnt for cnt in contours if min_contour_area < cv2.contourArea(cnt) < max_contour_area]

    #pirinç sayısını ekrana yazdırma
    print(f"fıstık sayısı:{len(contours)}")

    #konturları orjinal kare üzerine çiz
    cv2.drawContours(frame,contours,-1,(0,255,0),2)
    #kareyi göster
    cv2.imshow("webcam",frame)
    #çikış için q tuşuna bas
    if cv2.waitKey(1)& 0xFF ==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
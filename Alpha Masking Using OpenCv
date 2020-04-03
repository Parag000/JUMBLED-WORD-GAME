import cv2
import numpy as np

w1=0

img1 = cv2.imread("sky.jpg",1)
img2 = cv2.imread("moon.jpg",1)

while(w1<=1):
    
    img3 = cv2.addWeighted(img1,w1,img2,1-w1,0)
    w1+=0.1
    cv2.imshow("sky and moon",img3)
    cv2.waitKey(1000)  #CHANGES EVERY 1 SECOND

cv2.destroyAllWindows()

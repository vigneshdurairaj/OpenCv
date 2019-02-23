import numpy as np
import cv2

canvas = np.zeros((300,300,3) , dtype = "uint8") # datatype needto be specified unsignesd int 8bits
green = (0,255,0)

cv2.line(canvas , (0,0) , (300,300) , green)


cv2.rectangle(canvas , (10,10) , (60,60) , green)

cv2.rectangle(canvas , (50,200) , (200,255) , green , 5) # increase Thickness

cv2.rectangle(canvas, (200,50) , (255,125), green , -1) # fills the mass

(centerX , centerY) = (canvas.shape[1] // 2 , canvas.shape[0] // 2)
white = (255,255,255)


cv2.circle(canvas , (centerX , centerY) , 20 ,white)

for i in range (0 , 100 ,20):
    cv2.circle(canvas, (centerX,centerY), i ,white)


cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
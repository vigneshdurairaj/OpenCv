#Acessing a pixel

from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True , help ="Path to Image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
 
cv2.imshow("Before",image)
cv2.waitKey(0)

(b,g,r) = image[0,0]
print("pixel at (0,0) - Red{} Green{} Blue{}".format(r,g,b))


image[0,0] = (0,0,255)
(b,g,r) = image[0,0]
print("pixel at (0,0) - Red{} Green{} Blue{}".format(r,g,b))
cv2.imshow("After",image)
cv2.waitKey(0)

corner = image[0:100 , 0:100]  #(y1:y2 , x1:x2)
cv2.imshow("Corner" , corner)


image[0:100 , 100:0] = (0, 0, 255)
cv2.imshow ("Updated" , image)
cv2.waitKey(0)





# Image Processing Intro

import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True, help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)


(h,w) = image.shape[:2]
center = (w//2 , h//2)

M = cv2.getRotationMatrix2D(center,45,1.0) # (point of rotation, degrees , 1.0 is actulsize of image [2.0 doubles size] [half the size of actual image])
rotated = cv2.warpAffine(image,M,(w,h))
cv2.imshow("Rotated by 45 degree",rotated)
cv2.waitKey(0)

M = cv2.getRotationMatrix2D(center,-90,1.0)
rotated = cv2.warpAffine(image,M,(w,h))
cv2.imshow("Rotated 90deg",rotated)
cv2.waitKey(0)


rotated = imutils.rotate(image,180)
cv2.imshow("Rotated Last" , rotated)
cv2.waitKey(0)

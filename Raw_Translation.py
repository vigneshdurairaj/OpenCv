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

M = np.float32([[1,0,25], [0,1,50]])  #Declaring a numpy array with [1,0,tx] [0,1,ty]
shifted = cv2.warpAffine(image, M, (image.shape[1],image.shape[0])) # wrap affine is the translation predefined
cv2.imshow("Shifted down and right",shifted)
cv2.waitKey(0)

M = np.float32([[1,0,-50],[0,1,-90]])
shifted2 = cv2.warpAffine(image,M, (image.shape[1],image.shape[0]))
cv2.imshow("Shifted to up and left" , shifted2)
cv2.waitKey(0)

shifted3 = imutils.translate(image,25,50) #predifined function in imutils for translate
cv2.imshow("haha",shifted3)
cv2.waitKey(0)
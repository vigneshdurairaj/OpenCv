# Image Processing Intro

import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True, help= "Path to the imagee")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original",image)
cv2.waitKey(0)

flipped = cv2.flip(image,1) # 0 filps vertically ,,, -1 flips bothways
cv2.imshow("FLipped Horizantally",flipped)
cv2.waitKey(0)

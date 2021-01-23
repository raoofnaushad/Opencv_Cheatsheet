
import cv2 as cv
import numpy as np


## Creating a blank image

## Creating an nnumpy array with 500,500 dimension and \
   # dtype as uint8 which is basically datatype of image
blank_img = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow("Blank Image", blank_img)
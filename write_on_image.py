import cv2 as cv
import numpy as np

## Creating a blank image
blank_img = np.zeros((500, 500, 3), dtype="uint8")

## Writing text on image
cv.putText(blank_img, "Hello World", (225, 225), cv.FONT_HERSHEY_PLAIN, \
    2.0, (255, 255, 255), 2)

cv.imshow("Texte in image", blank_img)


cv.waitKey(0)
import cv2 as cv

## Reading an image
img = cv.imread('Images/1.jpeg')

## Displaying image
cv.imshow("Travel", img)

## Waiting for a keyboard input
cv.waitKey(0)
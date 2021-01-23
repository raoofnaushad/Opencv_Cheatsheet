import cv2 as cv
import numpy as np

img = cv.imread("Images/photography.jpeg")
cv.imshow("Balloons", img)


# ## Translation
# def translation(img, x, y):
#     transMAT = np.float32([[1, 0, x], [0, 1, y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMAT, dimensions)

# translated = translation(img, -100, 100)      ## -ve for x, y =>> Left, Up
# cv.imshow("Translated", translated)         


# ## Rotation
# def rotate(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]
    
#     if rotPoint is None:
#         rotPoint = (width//2, height//2)
#     ## Creating a rotation matrix with <rotation point,
#     ## angle, and scale which we give us 1.0.
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimension = (width, height)    
#     return cv.warpAffine(img, rotMat, dimension)

# rotated = rotate(img, 20)
# cv.imshow("Rotated", rotated)


# ## Resize
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
# cv.imshow("resized", resized)

# ## Flipping
# flipped = cv.flip(img, 0) ## Image, flipcode
# cv.imshow("Flipped", flipped)

## Cropping
cropped = img[100:200, 100:200]
cv.imshow("Cropped", cropped)


cv.waitKey(0) 
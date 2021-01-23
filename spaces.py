import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Images/camera.jpeg")
cv.imshow("Camera",img)


# ## Seing an image outside opencv
# plt.imshow(img)
# plt.show()


## BGR to Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

## BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

## BGR to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

## BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)
# plt.imshow(rgb)
# plt.show()


cv.waitKey(0)


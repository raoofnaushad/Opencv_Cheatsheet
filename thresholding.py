import cv2 as cv


img = cv.imread("Images/cats.jpg")
cv.imshow("Image", img)

## Converting to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

## Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Thresholding", thresh)

## Simple Thresholding Inverse
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Inverse Thresholding", thresh_inv)

## Adaptive Thresholding  Mean
adaptive_thresh = cv. adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive threshold Mean", adaptive_thresh)

## Adaptive Thresholding  Mean
adaptive_thresh_gauss = cv. adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive threshold Gaussian", adaptive_thresh_gauss)

cv.waitKey(0)
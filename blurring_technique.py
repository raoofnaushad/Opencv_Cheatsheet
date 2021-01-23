import cv2 as cv


img = cv.imread("Images/dog.jpg")

## Averaging 
average = cv.blur(img, (3,3))
cv.imshow("Blurred", average)


## Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian", gauss)

## Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median", median)

## Bilaterial
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow("Bilateral", bilateral)

cv.imshow("Image", img)
cv.waitKey(0)
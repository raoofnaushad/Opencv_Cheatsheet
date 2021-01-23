import cv2 as cv


img = cv.imread("Images/dog.jpg")
cv.imshow("Image", img)



cv.waitKey(0)
import cv2 as cv


img = cv.imread("Images/2.jpeg")

cv.imshow("Image", img)

# ## 1. Converting to gray scale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Camera Gray", gray)


# ## 2. Blur
# ## Using gaussian blur with a kernel of (3,3)
# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow("Blur image", blur)


# ## 3. Edge detector
# canny = cv.Canny(blur, 125, 175)
# cv.imshow("canny", canny)

# ## 4. Dialattion
# dialated = cv.dilate(canny, (7, 7), iterations=3)
# cv.imshow("Dialated", dialated)

# ## 4. Erode
# eroded = cv.erode(dialated, (7, 7), iterations=3)
# cv.imshow("Eroded", eroded)

# ## 5. Resize
# resized = cv.resize(img, (300, 300)) # Add interpolation if needed
# cv.imshow("Resized", resized)

## 6. Cropping
cropped = img[150:450, 150:450]
cv.imshow("Cropped", cropped)


cv.waitKey(0)
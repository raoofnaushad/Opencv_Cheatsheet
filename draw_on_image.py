import cv2 as cv
import numpy as np

## Creating a blank image
blank_img = np.zeros((500, 500, 3), dtype="uint8")

# ## 1. Painting image
# blank_img [200:300, 100:200] = 255, 0, 0  #B<G<R
# cv.imshow("Painted Image", blank_img)
           
## 2. Draw a rectangle
# cv.rectangle(blank_img, (0,0), (100, 100), (255, 0, 0), thickness=2 )
# cv.imshow("Rectangle", blank_img)

# cv.rectangle(blank_img, (0,0), (100, 100), (255, 0, 0), thickness=cv.FILLED)  # Alternatively -1
# cv.imshow("Rectangle Filled", blank_img)

## 3. Drawing a circle
# cv.circle(blank_img, (blank_img.shape[1]//2, blank_img.shape[0]//2), \
#     40, (0,0,255), thickness=-1)
# cv.imshow("Cirlce in image", blank_img)

## 4. Drawing a line
cv.line(blank_img, (0,0), (blank_img.shape[1]//2, blank_img.shape[0]//2), \
    (255,0,255), thickness=3)
cv.imshow("Line in image", blank_img)


cv.waitKey(0)
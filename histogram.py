import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread("Images/dog.jpg")
# cv.imshow("Image", img)

## Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# ## Gray Scale Histogram
# histogram = cv.calcHist([gray], [0], None, [256], [0,256])
# plt.figure()
# plt.title("Histogram Plotting")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(histogram)
# plt.xlim([0,256])
# plt.show()



## Color Histogram

plt.figure()
plt.title("Color Histogram Plotting")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors = ("r", "g", "b")
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()



# cv.waitKey(0)
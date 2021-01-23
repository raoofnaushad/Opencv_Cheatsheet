import cv2 as cv


## Rescaling function
def rescaleFrame(frame, scale=0.75):
    ## Getting width and height to new values
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    ## Setting new dimension
    dimension = (width, height)
    
    ## Returning rescaled
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

## Reading an image
img = cv.imread('Images/1.jpeg')

## Displaying image
cv.imshow("Travel", img)
## Rescaled Image
rescaled_image = rescaleFrame(img)
## Displaying image
cv.imshow("Travel Rescaled", rescaled_image)

## Waiting for a keyboard input
cv.waitKey(0)
import cv2 as cv

## Creating a capture object
capture = cv.VideoCapture("Videos/2.mp4")

## Enter loop for displaying
while True:
    ## Reading both frame and boolean value if a frame is present
    IsTrue, frames = capture.read()

    ## Displaying
    cv.imshow("Motivation", frames)
    
    ## Conditions for breaking up from loop
    if cv.waitKey(20) & 0xFF==ord("d"):
        break

## Releasing capture object
capture.release()
## Destroying all windows
cv.destroyAllWindows()
    
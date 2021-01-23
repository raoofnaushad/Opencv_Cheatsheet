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

## Creating a capture object
capture = cv.VideoCapture("Videos/2.mp4")


## Enter loop for displaying
while True:
    ## Reading both frame and boolean value if a frame is present
    IsTrue, frames = capture.read()
    ##resized_frame
    resized_frames = rescaleFrame(frames)
    ## Displaying
    cv.imshow("Motivation", frames)
    ## Displaying Resized
    cv.imshow("Motivation Resized", resized_frames)
    
    ## Conditions for breaking up from loop
    if cv.waitKey(20) & 0xFF==ord("d"):
        break
## Releasing capture object
capture.release()
## Destroying all windows
cv.destroyAllWindows()
    
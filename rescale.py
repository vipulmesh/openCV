import cv2 as cv

# rescaling means modifying its height and width 
# genrelly we downscale than the original value 
#

# img = cv.imread('image.png')
# cv.imshow('Image', img)

def rescaleFrame(frame, scale=0.75): 
    #for images, videos and live videos
    width =int(frame.shape[1]*scale)
    height =int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #for live videos only
    capture.set(3, width) 
    capture.set(4, height)

#reading videos
capture = cv.VideoCapture('video.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized =rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('video resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        #upar wali line means if letter d is pressed then break the loop
        break

cv.waitKey(0)
import cv2 as cv

# reading images 
img = cv.imread('image.png')
cv.imshow('Image', img)

#reading videos
capture = cv.VideoCapture('video.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
cv.waitKey(0)
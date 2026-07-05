import cv2 as cv

# # reading images 
# img = cv.imread('image.png')
# cv.imshow('Image', img)
# cv.waitKey(0)


#reading videos
capture = cv.VideoCapture('video.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('q'):
        #upar wali line means if letter d is pressed then break the loop
        break
cv.destroyAllWindows()

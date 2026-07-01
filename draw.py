import cv2 as cv
import numpy as np

#to create a blank mage we se np.zeros() function
blank = np.zeros((500, 500,3), dtype='uint8')
cv.imshow('Blank', blank)

# img = cv.imread('image.png')
# cv.imshow('Image', img)

# painitng the image witha  cnolor
# blank[200:300, 300:400]=0,255,0
# cv.imshow('Green', blank)

#drawing a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

#drawing a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)
cv.waitKey(0)
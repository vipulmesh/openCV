import cv2 as cv
import numpy as np

#to create a blank page we se np.zeros() function
blank = np.zeros((500, 500,3), dtype='uint8')
# cv.imshow('Blank', blank)

# img = cv.imread('image.png')
# cv.imshow('Image', img)

# painitng the image witha  cnolor
# blank[200:300, 300:400]=0,255,0 #image[y1:y2, x1:x2]
# cv.imshow('Green', blank)

# #drawing a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
# # cv.rectangle(image, start_point, end_point, color, thickness)
# cv.imshow('Rectangle', blank)

# #drawing a circle
#cv.circle(image, center, radius, color, thickness)
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
# cv.imshow('Circle', blank)


# #how to write on an image 

# cv.putText(
#     image,
#     text,
#     org,
#     fontFace,
#     fontScale,
#     color,
#     thickness
# )
cv.putText(blank, 'Vipul Meshram', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv
import numpy as np

img=cv.imread('image.png')
cv.imshow('Image',img)

#Transaltion -- (basically shiting the image on X AND Y axes)

def translate(img,x,y):
    # in parameters  x and y are the pixels which the pixels shoould be shifted 

    transMat =np.float32([[1,0,x],[0,1,y]])
    dimensions =(img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

#-x --> left
# x --> right

# -y --> up
# y---> down

translated = translate(img,-100,-100)
cv.imshow('Transalted',translated)

cv.waitKey(0)


#roatation 
#it means to roate the image to a particular point

def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat =cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions =(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated =rotate(img,45)
cv.imshow('Roatated',rotated)

cv.waitKey(0)
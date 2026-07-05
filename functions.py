import cv2 as cv
img= cv.imread('image.png')
cv.imshow('Image', img)

# converting to greyscale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blurring the image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#hamesha odd number hi chiaye (7,7)) this is known as kernal size
cv.imshow('Blur', blur)


#edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)


#dialeting the image (yeh kaafi thick edges dikhata hai)
dialated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dialated)

#eroding the image (yeh kaafi thin edges dikhata hai)
eroded = cv.erode(dialated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

#resize 
reszied = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# interpolation -- Jab image ka size change hota hai, naye pixels ka color kaise calculate kiya jaye.
cv.imshow('Resized', reszied)

#cropping
cropped = img[50:200, 200:400]
#image[y1:y2, x1:x2]
cv.imshow('Cropped', cropped)
cv.waitKey(0)

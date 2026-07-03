
#cropping means to cut a rectangular part from a image
#we use numpy slicing inthe openCV

# y axis -- rows -- top to bottom
# x axis -- coloum -- left to right 

import cv2
image=cv2.imread("image.png")

cropped = image[100:200,50:150]
cv2.imshow("cropped image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows
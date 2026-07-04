#synatx --> cv2.filter2D(src,depth,kernel)

# it makes a 3*3 matrix , har ek neighbour ko pkdega aur  joh centre pixel hoga usko boost krega 

import cv2
import numpy as np
image=cv2.imread("image.png")

sharpen_kernel = np.array([
    [0,-1,0],
    [-1,5,-1],    # edges ko nahi chedte , sirf left right bottom , up ko enchance krta hai
    [0,-1,0]
])
sharpened =cv2.filter2D(image,-1,sharpen_kernel)
cv2.imshow("original image ", image)
cv2.imshow("sharpended",sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
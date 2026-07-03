# resized = cv2.reszie(src,dzise,fx,fy,interpolaion)
# dszie --> wdth *height
# fy, fx -- scale factors

import cv2
image=cv2.imread("image.png")
resized =cv2.resize(image,(300,300))
cv2.imshow("resized",resized)

cv2.imwrite("saved_resized.png",resized)

cv2.waitKey(0)
cv2.destroyAllWindows

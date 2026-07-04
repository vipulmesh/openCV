import cv2
import cv2
image=cv2.imread("image.png")

blurred_image = cv2.medianBlur(image,15)
cv2.imshow("original image", image)
cv2.imshow("blrred image",blurred_image)

cv2.waitKey(0)
cv2.destroyWindows()

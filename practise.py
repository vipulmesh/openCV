import cv2
import numpy as np

img = cv2.imread("image.png")

if img is None:
    print("Image not found")
    exit()

cv2.imshow("Original", img)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
lab_bg = cv2.GaussianBlur(lab, (5, 5), 2)

cv2.imshow("lab image",lab_bg)
cv2.imshow("lab image",lab)

cv2.waitKey(0)
cv2.destroyAllWindows()
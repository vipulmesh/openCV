
# center nikalne ke liye we use w//2 and h//2 
# // is the integer division joh output me sirf integer value deta hai

#syntaxx
# M=cv2.getRotationMatrix2D(center,angle,scale)
# rotated_image=cv2.warpAffine(image,M,(width,height))

import cv2
image=cv2.imread("image.png")

(h,w)=image.shape[:2]  #image.shape image ka size batata hai [:2] last me lagane se voh sirf height aur widdth retun krege color channel nahin
center =(w//2,h//2)
M=cv2.getRotationMatrix2D(center,90,1.0)
rotated_image=cv2.warpAffine(image,M,(w,h))

cv2.imshow("rotated image ",rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows

#flipping the image

flipped_hor=cv2.flip(image,1)
flipped_vert=cv2.flip(image,0)
flipped_both=cv2.flip(image,-1)

cv2.imshow("original",image)
cv2.imshow("flippedboth",flipped_both)
cv2.imshow("hor",flipped_hor)
cv2.imshow("vert",flipped_vert)

cv2.waitKey(0)
cv2.destroyAllWindows
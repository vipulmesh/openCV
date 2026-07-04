# detect the border
# feature extraction 
# use for separate objection

#edges =cv2.Canny(image,threshold1,threshold2)

# t1== agar halka sa brihgt hai t1 se toh ekdum bright krdo
# t2 == agar halka sa dark hai t2 se toh pura black karke do 


#hamesha greyscale value hi dii jayegi

import cv2
img =cv2.imread("image.png",cv2.IMREAD_GRAYSCALE)

ret, thres_img=cv2.threshold(img,120,255,cv2.THRESH_BINARY) # 50 -- lower boundary 150 -upper voundary
cv2.imshow("orignal pic", img)
cv2.imshow("edges", thres_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#joh bhi pixel ki value 120 ki upar toh pura black hogya hai and vicecersa
# detect the border
# feature extraction 
# use for separate objection

#edges =cv2.Canny(image,threshold1,threshold2)

# t1== agar halka sa brihgt hai t1 se toh ekdum bright krdo
# t2 == agar halka sa dark hai t2 se toh pura black karke do 


#hamesha greyscale value hi dii jayegi

import cv2
img =cv2.imread("image.png",cv2.IMREAD_GRAYSCALE)

edges=cv2.Canny(img,50,150) # 50 -- lower boundary 150 -upper voundary
cv2.imshow("orignal pic", img)
cv2.imshow("edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
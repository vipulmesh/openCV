#syntax
#cv2.line(img,pt1,pt2,color,thickness)


# pt1 and pt2 are the cordinates (imagine a 2d graph notebook/paper)

import cv2
image=cv2.imread("image.png")

pt1=(223,231) #x1 , y1
pt2=(311,322) # x2, y2
color=(255,0,0)
thickness=2
line= cv2.line(image,pt1,pt2,color,thickness)
cv2.imshow("line ",line)

cv2.waitKey(0)
cv2.destroyAllWindows

#drawing a rectangle

# pt1 top left corner of rect
# pt2 - bottom right corner of rect

pt1=(50,50) #x1 , y1
pt2=(250,200) # x2, y2
color=(255,0,0)
thickness=2

rect= cv2.rectangle(image,pt1,pt2,color,thickness)

cv2.imshow("rectangle ",rect)

cv2.waitKey(0)
cv2.destroyAllWindows


 # drawing a circle 
circle= cv2.circle(image,(150,150),50,(255,0,0),-1)
cv2.imshow("circle ",circle)

cv2.waitKey(0)


#adding a txt
#syntaxx
# cv2.putText(image,text,org,font,fontScale,color,thickness)
#org

text =cv2.putText(image,"vipul meshram",(50,300),cv2.FONT_HERSHEY_COMPLEX,1.2,(0,255,0),2)
cv2.imshow("text ",text)
cv2.waitKey(0)
cv2.destroyAllWindows


import cv2
import numpy as np

img = cv2.imread(r"C:\Users\vipul\OneDrive\Desktop\VipulMeshram\OpenCV\counters&shapedetection\shape.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_, thresh =cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

#find contours
contours,heirarchy =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#WE USE cv2.drawContours  to shwo the output
cv2.drawContours(img,contours,-1,(0,255,0),3)


for contour in contours:
    approx =cv2.approachpolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    corners =len(approx)

    if corners ==3:
        shape_name="Triangle"
    if corners ==4:
        shape_name="Rectangle"
    if corners ==5:
        shape_name="Pentagon"
    if corners >5:
        shape_name="Circle"
    else:
        shape_name="unknown"

    cv2.drawContours(img,[approx],0,(0,255,0),2)
    x=approx.rave()[0]
    y=approx=rave()[1]-10
    cv2.putText(img,shape_name,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,0,0),)

cv2.imshow("contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
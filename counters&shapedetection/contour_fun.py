import cv2

img = cv2.imread(r"C:\Users\vipul\OneDrive\Desktop\VipulMeshram\OpenCV\counters&shapedetection\shape.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_, thresh =cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

#find contours
contours,heirarchy =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#WE USE cv2.drawContours  to shwo the output
cv2.drawContours(img,contours,-1,(0,255,0),3)
cv2.imshow("contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
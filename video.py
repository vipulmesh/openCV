#a collection of images , whiich is displayed very fast 
# image displayed is called FRAME

#frame by frame processing --> 
#ek ek frame me ek ek task ko complete krte hai 

#cv2.videoCapture(source)
#if webcam inbuilt -- use source is 0

import cv2
cap = cv2.VideoCapture(0)
while True:
    ret,frame =cap.read() #ret==True/False frae =image

    if not ret:
        print("Could not read")
        break
    cv2.imshow("Webcam", frame)

   
    if cv2.waitKey(1) & 0xFF ==ord('q'):  #ord fucnt gives us ASCII number matlb q dabane se band hojayea
        print("quitting")
        break

cap.release
cv2.destroyAllWindows()

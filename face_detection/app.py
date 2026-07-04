import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # detectMultiScale() -- scan and detect object
    
    faces =face_cascade.detectMultiScale(gray,1.1,5)
    
    #minNeighbors = 5 (atleast 5 test passes krega then bolega haa yeh ek chehra hai)
    # 5-- strict chking
    # scaleFactor =1.1 (kitna zoom karega each try) 

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("webcam",frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
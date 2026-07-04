#u can draw on a frame
#detection like eyes , face 
#specific time and frame fetching 
#e.g. snapchat wala filter

# saving webcam video with a openCV

#videoWriter(filename,codec,fps,frame_szie)


#.avi is extention is used to stroee the video using XVID CODEC

# CODEC -- COMPRESSION FORMAT
#FPS -- FRAME PER SECOND

import cv2
camera = cv2.VideoCapture(0)

frame_width =int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height =int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec=cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter("myvideo.avi",codec,20,(frame_width,frame_height))

while True:
    success, image = camera.read()

    if not success:
        break

    recorder.write(image)
    cv2.imshow("recording live", image)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

camera.release()
recorder.release()
cv2.destroyAllWindows()



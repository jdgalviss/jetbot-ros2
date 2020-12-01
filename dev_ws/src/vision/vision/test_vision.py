import numpy as np
import cv2
import time
import pyfakewebcam

cap = cv2.VideoCapture(1)
#camera = pyfakewebcam.FakeWebcam('/dev/video2', 640, 480)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #camera.schedule_frame(frame)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

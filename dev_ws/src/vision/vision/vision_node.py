import rclpy
from rclpy.node import Node
import cv2 
import numpy as np
import pyfakewebcam
import time

FAKE_VIDEO_DEVICE = '/dev/video0'
REAL_VIDEO_DEVICE_ID = 1
VIDEO_HEIGHT = 360
VIDEO_WIDTH = 640
class Vision(Node):
    def __init__(self, port=8765):
        super().__init__('vision')
        self.cap = cv2.VideoCapture(REAL_VIDEO_DEVICE_ID)
        self.camera = pyfakewebcam.FakeWebcam(FAKE_VIDEO_DEVICE, VIDEO_WIDTH, VIDEO_HEIGHT)
        self.loop()

    def loop(self):
        while(True):
            # Capture frame-by-frame
            ret, frame = self.cap.read()

            # Our operations on the frame come here
            frame = cv2.resize(frame,(VIDEO_WIDTH,VIDEO_HEIGHT))
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.camera.schedule_frame(frame_rgb)

            # Display the resulting frame
            #cv2.imshow('frame',frame)
            cv2.waitKey(200)
            #time.sleep(0.1)
            

def main(args=None):
    print('Hi from vision')
    rclpy.init(args=args)
    vision = Vision()
    rclpy.spin(vision)

    rclpy.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


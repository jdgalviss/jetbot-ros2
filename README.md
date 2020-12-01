# Jetbot

## For local server
pip install SimpleWebSocketServer
python3 -m http.server 1234 --directory /home/jdbot/repos/nano_jetbot/local_server/

# For webrtc
pip3 install crc32c==2.0
pip3 install aiortc
pip3 install aiohttp


# For fake cam in webrtc
apt-get install v4l2loopback-utils
pip3 install pyfakewebcam
modprobe v4l2loopback devices=2 # will create two fake webcam devices

#For service on startup with sudo privilege
Create a file: /etc/rc.local

File contents:

#!/bin/sh -e
modprobe v4l2loopback devices=2 # will create two fake webcam devices
exit 0

Save the file and make it executable with this command:
sudo chmod +x /etc/rc.local


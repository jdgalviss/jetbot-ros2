sleep 1
source /home/jdbot/repos/nano_jetbot/scripts/env_vars.sh
# modprobe v4l2loopback devices=2 # will create two fake webcam devices
python3 /home/jdbot/repos/nano_jetbot/local_server/webrtc_control/webcam.py

# Jetbot-ros2

This is an implementation of a mobile robot in ros2. The software includes following functionalities:

* Teleoperation through websockets with live video feed using webrtc ([aiortc](https://github.com/aiortc/aiortc)).

* Integration of Intel realsese d435 and t265 cameras for depth estimation and localization respectively.

* 2D SLAM with [cartographer](https://github.com/ros2-gbp/cartographer-release).

* 3D SLAM using [rtabmap](https://github.com/introlab/rtabmap)

## Requirements
* ROS2 eloquent or foxy
* [librealsense2](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md)

# Installation

1. Clone this repo and its submodules
    ```bash
    git clone --recurse-submodules https://github.com/cameronmcnz/surface.git 
    ```
## Teleoperation support
2. Install aiortc for webrtc support
    ```bash
    pip3 install crc32c==2.0
    pip3 install aiortc
    pip3 install aiohttp
    ```

3. Install pyfakewebcam so that camera frames can be modified inside a ROS2 node and then shared through webrtc:
    ```bash
    apt-get install v4l2loopback-utils
    pip3 install pyfakewebcam
    ```

4. Write a service that creates fake webcam devices that can be used to share camera frames.
    ```bash
    gedit /etc/rc.local
    ```
    Copy and paste in file:
    ```bash
    #!/bin/sh -e
    modprobe v4l2loopback devices=2 # will create two fake webcam devices
    exit 0
    ```
    Save the file and make it executable with this command:
    ```bash
    chmod +x /etc/rc.local
    ```
## SLAM Support
1. Install Cartographer
    ```bash
    sudo apt-get install ros-<distro>-cartographer
    ```

2. Install Rtabmap

# Run
1. Run local server

## For local server
using aiohttp
simply run: python3 webcam.py
DEPRECATED:
    pip install SimpleWebSocketServer
    python3 -m http.server 1234 --directory /home/jdbot/repos/jetbot-ros2/local_server/

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

# For ROS Navigation stack
sudo apt install ros-foxy-navigation2
sudo apt install ros-foxy-nav2-bringup
sudo apt install ros-foxy-turtlebot3*

sudo apt install ros-foxy-navigation2 ros-foxy-nav2-bringup '~ros-foxy-turtlebot3-.*'

git clone https://github.com/ros-planning/navigation2.git --branch foxy-devel
rosdep install -y -r -q --from-paths src --ignore-src --rosdistro foxy




# Jetbot-ros2
[image1]: imgs/jetbot.png "jetbot"
[image2]: imgs/cartographer.gif "2D"
[image3]: imgs/rtabmap.gif "rtabmap"
[image4]: imgs/jetbot.gif "jetbot_gif"


This is an implementation of a mobile robot in ros2. The software includes the following functionalities:

* Teleoperation through websockets with live video feed using webrtc ([aiortc](https://github.com/aiortc/aiortc)).

* Integration of Intel realsense d435 and t265 cameras for depth estimation and localization respectively.

* 2D SLAM with [cartographer](https://github.com/ros2-gbp/cartographer-release).

* 3D SLAM using [rtabmap](https://github.com/introlab/rtabmap).

I used the Xiaor Geek Jetbot as a base platform and modified it to include a wide-angle camera, as well as the Intel Realsense d435 and t265.

![rs-viewer][image1]

## Requirements
* ROS2 eloquent or foxy.
* [librealsense2](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md).
* Motor Drivers - In this case, installed from the jetbot's [repository](https://github.com/NVIDIA-AI-IOT/jetbot/).

# Installation
0. Dependencies:
    ```bash

        sudo apt install ros-eloquent-navigation2
        sudo apt install ros-eloquent-nav2-bringup

    ```
1. Clone this repo and its submodules.
    ```bash
    git clone --recurse-submodules https://github.com/cameronmcnz/surface.git 
    ```
2. Install packages
    ```bash
    cd dev_ws/src
    git clone -b eloquent-devel git@github.com:stevemacenski/slam_toolbox.git 

    git clone https://github.com/ros-planning/navigation2.git --branch eloquent-devell

    rosdep install -y -r -q --from-paths src --ignore-src --rosdistro eloquent
    colcon build --symlink-install
    colcon build --packages-select motion_control


    git clone https://github.com/jdgalviss/realsense_ros2.git
    ```
## Teleoperation support
2. Install aiortc for webrtc support.
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
1. Install Cartographer.
    ```bash
    sudo apt-get install ros-<distro>-cartographer
    ```

2. Install rtabmap and rtabmap_ros following these [instructions](https://github.com/introlab/rtabmap_ros/tree/ros2#rtabmap_ros) in the branch **ros2**.

## Build ros 2 workspace
    ```bash
    cd dev_ws
    source /opt/ros/<distro>/setup.bash
    colcon build
    . /install/setup.bash
    ```


# Run
1. Run local teleoperation server.
    ```bash
    python3 local_server/webcam.py
    ```
    In a browser, open the teleoperation interface by going to: <jetson_nano's ip-address>:8080

2. In a new terminal, run the motion control launchfile to start streaming video and receiving motion commands.
    ```bash
    ros2 launch motion_control jetbot_launch.py
    ```
3. Run SLAM.
    * For 2D-SLAM, in another terminal:
    ```bash
    ros2 launch realsense_ros2 cartogrepher_launch.py
    ```
    * For 3D-SLAM, in another terminal:
    ```bash
    ros2 launch realsense_ros2 slam_rtabmap_launch.py
    ```
    3D Dense SLAM is too resource consuming for the Jetson Nano, in this case it is recommended to run it on a remote host. For this, simply set the same DOMAIN_ID on both the Jetson Nano and the remote host. (e.g. export DOMAIN_ID=0) and run the cameras in the Jetson Nano:
    ```bash
    ros2 launch realsense_ros2 realsense_launch.py
    ```
    Comment the nodes corresponding to the cameras on the host and run the rtabmap launch:
    ```bash
    ros2 launch realsense_ros2 slam_rtabmap_launch.py
    ```

# Results
[Video](https://youtu.be/T4csWliWSWs)

![jetbot][image4]
![cartographer][image2]
![rtabmap][image3]


<!-- sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE -->



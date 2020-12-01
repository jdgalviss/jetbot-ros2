sleep 1
source /opt/ros/dashing/setup.bash
source /home/jdbot/repos/jetbot-ros2/dev_ws/install/setup.bash
source /home/jdbot/repos/jetbot-ros2/scripts/env_vars.sh

ros2 run tf2_ros static_transform_publisher 0.0 0.0 0.0 0.0 0.0 0.0 camera_link_t265 camera_link & ros2 launch rs_t265 realsense_launch.py

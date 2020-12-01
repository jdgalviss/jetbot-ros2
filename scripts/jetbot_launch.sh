sleep 1
source /opt/ros/dashing/setup.bash
source /home/jdbot/repos/nano_jetbot/dev_ws/install/setup.bash
source /home/jdbot/repos/nano_jetbot/scripts/env_vars.sh
ros2 launch motion_control jetbot_launch.py

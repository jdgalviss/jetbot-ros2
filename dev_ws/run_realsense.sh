. /opt/ros/eloquent/setup.sh
# colcon build
. install/setup.sh
export DOMAIN_ID=0
ros2 launch realsense_ros2 realsense_launch.py
# ros2 launch realsense_ros2 cartographer_launch.py



#ros2 run motion_control speed_control_node

# ros2 launch slam_toolbox online_async_launch.py

# ros2 launch nav2_bringup nav2_navigation_launch.py

# sudo cp /opt/ros/eloquent/share/nav2_bringup/launch/nav2_bringup_launch.py ./src/realsense_ros2/realsense_ros2/launch/

# ros2 run explore_lite explore --ros-args -p costmap_topic:=/map -p visualize:=true -p use_sim_time:=false -p min_frontier_size:=0.3 -p planner_frequency:=20.0

# ros2 bag record -o subset /scan /tf /tf_static /rs_t265/odom /received_global_plan /marker /map /local_plan /goal_pose /cmd_vel /global_costmap/costmap /plan /transformed_global_plan /frontiers /graph_visualization /marker
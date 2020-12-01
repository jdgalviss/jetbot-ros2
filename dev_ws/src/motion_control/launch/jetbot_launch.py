from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ws_server',
            node_executable='ws_server_node',
            node_name='ws_server'
        ),
        Node(
            package='motion_control',
            node_executable='speed_control_node',
            node_name='speed_control'
        ),
        Node(
            package='vision',
            node_executable='vision_node',
            node_name='vision'
        )
    ])

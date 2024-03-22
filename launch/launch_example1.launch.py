from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sze_sw1_szinusz',
            executable='gen_node',
        ),
        Node(
            package='sze_sw1_szinusz',
            executable='sum_node',
        ),
    ])
import os
import yaml
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    dirname, filename = os.path.split(os.path.realpath(__file__))
    config_path = os.path.join(dirname, 'config.yaml')
    rviz_path = os.path.join(dirname, 'visualization.rviz')

    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    ld = LaunchDescription()

    # VineSLAM node
    vineslam = Node(
        package='vineslam_ros',
        node_executable='slam_node',
        name='slam_node',
        parameters=[config],
        remappings=[
            ('/odom_topic', '/odom'),
            ('/scan_topic', '/rslidar_points'),
        ],
    )
    ld.add_action(vineslam)

    # Rviz
    rviz = Node(
        package='rviz2',
        node_executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_path, '--ros-args', '--log-level', 'INFO'],
    )
    ld.add_action(rviz)

    return ld

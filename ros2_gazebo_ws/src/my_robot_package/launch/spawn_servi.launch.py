from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    package_name = "my_robot_package"

    pkg_share = get_package_share_directory(package_name)

    world_file = os.path.join(
        pkg_share,
        "worlds",
        "simple_restaurant.world"
    )

    urdf_file = os.path.join(
        pkg_share,
        "urdf",
        "servi_model.urdf"
    )

    with open(urdf_file, "r") as f:
        robot_description = f.read()

    gazebo = ExecuteProcess(
        cmd=[
            "gazebo",
            "--verbose",
            world_file,
            "-s",
            "libgazebo_ros_factory.so"
        ],
        output="screen"
    )

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[
            {
                "robot_description": robot_description
            }
        ]
    )

    spawn_robot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        # 로봇 생성 위치 설정
        arguments=[
            '-entity', 'servi',
            '-topic', 'robot_description',
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.2'
        ],
        output="screen"
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_robot
    ])
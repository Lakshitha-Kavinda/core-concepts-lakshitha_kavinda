from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tests',
            executable='chatter.py',
            name='test_chatter',
            output='screen',
            remappings=[('/chatter', '/test/chatter')],
        ),
        Node(
            package='tests',
            executable='listener.py',
            name='listener',
            output='screen',
        ),
        ExecuteProcess(
            cmd=[
                'ros2', 'topic', 'pub', '--once',
                '/twist', 'geometry_msgs/Twist',
                "{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
            ],
            shell=True
        )
    ])

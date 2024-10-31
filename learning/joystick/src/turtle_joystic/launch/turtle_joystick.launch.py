from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node (
            package= "joy",
            executable= "joy_node",
            name = "Joystick_node",
            output = "screen"
        ),
        
        Node (
            package= "turtle",
            executable= "turtlesim_node",
            name = "turtle",
            output = "screen"
        ),
        
        Node(
            package= "turtle_joystic",
            executable= "joy_stick_listener",
            name= "joy_stick_listener_node",
            output = "screen",
        ),
        Node(
            package='turtle_joystic',
            executable='turtle_controller',
            name='turtle_controller_node',
            output='screen',
            # You can specify parameters here if needed
        ),


    ])
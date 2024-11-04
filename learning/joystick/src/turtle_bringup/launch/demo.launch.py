from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    joy_stick_node = Node (
            package= "joy",
            executable= "joy_node",
            name = "Joystick_node",
            output = "screen"
        )
    
    turtle_sim_node = Node (
            package= "turtlesim",
            executable= "turtlesim_node",
            name = "turtle",
            output = "screen"
        )
    
    joy_stick_listener = Node(
            package= "turtle_joystic",
            executable= "joy_stick_listener",
            name= "joy_stick_listener_node",
            output = "screen",
        )
    
    turtle_controller_node = Node(
            package='turtle_joystic',
            executable='turtle_controller',
            name='turtle_controller_node',
            output='screen',
            # You can specify parameters here if needed
        )
    
    ld.add_action(joy_stick_node)
    ld.add_action(turtle_sim_node)
    ld.add_action(joy_stick_listener)
    ld.add_action(turtle_controller_node)

    return ld
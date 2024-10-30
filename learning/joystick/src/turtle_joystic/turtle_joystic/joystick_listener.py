#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

topic = "/joy"

class JoystickListener(Node):
    def __init__(self):
        super().__init__("Custom_Joystick_Listener")

        self.joy_sub = self.create_subscription(
            Joy,
            topic,
            self._joy_stick_callback,
            10,
        )

    def _joy_stick_callback(self, joy_msg):
        axes = {
            "analog_left_move_right": 1 if joy_msg.axes[0] == -1 else 0,
            "analog_left_move_left": 1 if joy_msg.axes[0] == 1 else 0,
            "analog_right_move_right": 1 if joy_msg.axes[3] == -1 else 0,
            "analog_right_move_left": 1 if joy_msg.axes[3] == 1 else 0,
            
            "analog_left_move_up": 1 if joy_msg.axes[1] == 1 else 0,
            "analog_left_move_down": 1 if joy_msg.axes[1] == -1 else 0,
            "analog_right_move_up": 1 if joy_msg.axes[2] == 1 else 0,
            "analog_right_move_down": 1 if joy_msg.axes[2] == -1 else 0,
            
            "move_left_pressed" : 1 if joy_msg.axes[4] == 1 else 0,
            "move_right_pressed" : 1 if joy_msg.axes[4] == -1 else 0,

            "move_up_pressed" : 1 if joy_msg.axes[5] == 1 else 0,
            "move_down_pressed" : 1 if joy_msg.axes[5] == -1 else 0,
        } 
        
        buttons = {
             "button_1": joy_msg.buttons[0],
             "button_2": joy_msg.buttons[1],
             "button_3": joy_msg.buttons[2],
             "button_4": joy_msg.buttons[3],
             "R_1" : joy_msg.buttons[5],
             "R_2" : joy_msg.buttons[7],
             "L_1" : joy_msg.buttons[4],
             "L_2" : joy_msg.buttons[6],
        }

        self.get_logger().info(f"{axes}, {buttons}")
        



def main():
    rclpy.init()
    node = JoystickListener()
    rclpy.spin(node)
    rclpy.shutdown()
#!/usr/bin/env python3

import rclpy

from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import json


"""

LEFT_RIGHT
pos += movement_dir * velocity

UP_DOWN
pos += movement_dir * velocity
"""


joy_stick_topic = "/joystick_data/axes_buttons"
turtle_topic = "/turtle1/cmd_vel"

class JoySubTurtleCont(Node):
    def __init__(self):
        super().__init__("Custom_Turtle_Cont")

        self.joy_stick_sub = self.create_subscription(
            String,
            joy_stick_topic,
            self.listener_callback,
            10
        )

        self.turtle_pub = self.create_publisher(
            Twist,
            turtle_topic,
            10
        )

    def listener_callback(self, joy_msg):
        joy_msg = json.loads(joy_msg.data)
        axes = joy_msg.get("axes")
        buttons = joy_msg.get("buttons")

        turtle_msg = Twist()
        
        if axes.get("move_left_pressed"):
            turtle_msg.linear.x -= 2

        if axes.get("move_right_pressed"):
            turtle_msg.linear.x += 2


        self.turtle_pub.publish(turtle_msg)
        self.get_logger().info(f"PUBLISHING..........")


def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(JoySubTurtleCont())
    rclpy.shutdown()

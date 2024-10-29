#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Publisher(Node):
    def __init__(self):
        super().__init__("Custom_Publisher")
        self.publish_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer_callback = self.create_timer(1.0, self.msg_publisher)

    def msg_publisher(self):
        msg = Twist()
        msg.linear.x = 5.0
        msg.angular.z = 2.0
        self.publish_.publish(msg)
        self.get_logger().info("Publishing")


def main(args = None):
    rclpy.init()
    node = Publisher()
    rclpy.spin(node)
    rclpy.shutdown()
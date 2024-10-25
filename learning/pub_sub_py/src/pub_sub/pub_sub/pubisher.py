#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Publisher(Node):
    def __init__(self):
        super().__init__("custom_turtle_publisher")
        self.publisher_ = self.create_publisher(
            Twist,
            "/turtle1/cmd_vel",
            10
        )
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.angular.z = 1.0
        msg.linear.x = 1.0
        self.publisher_.publish(msg)
        self.get_logger().info("PUBLISHING...")



def main(args = None):
    rclpy.init(args = args)

    publisher = Publisher()
    rclpy.spin(publisher)
    rclpy.shutdown()

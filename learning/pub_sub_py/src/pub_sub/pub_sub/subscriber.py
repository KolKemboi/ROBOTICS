#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class Subscriber(Node):
    def __init__(self):
        super().__init__("custom_turtle_subscriber")
        self.subscription_ = self.create_subscription(
            Pose,
            "/turtle1/pose",
            self.listener_callback,
            10
        )

    def listener_callback(self, pose):
        self.get_logger().info(f"I listen to {pose.x} and {pose.theta}")

def main(args = None):
    rclpy.init(args = args)
    subscriber = Subscriber()
    rclpy.spin(subscriber)
    rclpy.shutdown()
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class Subscriber(Node):
    def __init__(self):
        super().__init__("Custom_Subscriber")
        self.sub = self.create_subscription(
            Pose,
            "/turtle1/pose",
            self.msg_listener,
            10
        )

    def msg_listener(self, pose):
        self.get_logger().info(f"{pose.x}, {pose.theta}")


def main(args = None):
    rclpy.init(args= args)
    node = Subscriber()
    rclpy.spin(node)
    rclpy.shutdown()
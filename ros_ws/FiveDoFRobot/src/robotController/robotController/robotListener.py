#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class RobotListener(Node):
    def __init__(self, name):
        super().__init__("RobotListener")
        self.names: list = name

        self.subscription = self.create_subscription(
            JointState,
            "/joint_states",
            self.listener_callback,
            10
        )         
        self.subscription

    def listener_callback(self, msg):
        joint_pos = dict(zip(msg.name, msg.position))
        for joint in self.names:
            self.get_logger().info(f"{joint}:   {joint_pos[joint]}")

def main(args = None):
    rclpy.init()
    joint_names = [
            "joint_1", "joint_2", "joint_3", "joint_4", "joint_5" 
        ]
    
    node = RobotListener(joint_names)
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
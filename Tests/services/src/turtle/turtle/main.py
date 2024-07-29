#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from functools import partial


class MyNode(Node):

    def __init__(self):
        super().__init__("Closed_Loop_System")
        self.get_logger().info("Closed loop started")

        self.prev_x = 0.0
        self.pose_Pub = self.create_publisher(
            Twist,
            "/turtle1/cmd_vel",
            10
        )

        self.pose_Sub = self.create_subscription(
            Pose,
            "/turtle1/pose",
            self.pose_callback,
            10
        )

    def pose_callback(self, pose: Pose):
        cmd = Twist()

        if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
            cmd.linear.x = 1.0
            cmd.angular.z = 0.9
        else:
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
        self.pose_Pub.publish(cmd)

        if pose.x > 5.5 and self.prev_x <= 5.5:
            self.prev_x = pose.x
            self.set_pen(255, 0, 0, 3, 0)

        elif pose.x < 5.5 and self.prev_x >= 5.5:
            self.prev_x = pose.x
            self.set_pen(0, 255, 0, 3, 0)

    def set_pen(self, r, g, b, width, off):
        client = self.create_client(
            SetPen,
            "/turtle1/set_pen"
        )
        while not client.wait_for_service(1.0):
            self.get_logger().warn("warning, service not found...")

        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_set_pen))

    def callback_set_pen(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error(f"error => {e}")


def main(args=None):
    rclpy.init(args=None)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

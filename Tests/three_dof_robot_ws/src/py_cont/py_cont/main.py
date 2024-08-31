#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import argparse


class trajSenderNode(Node):
    def __init__(self, joint_pos, time_to_reach, time_to_reach_ns):
        super().__init__("Traj_Sender_Node")
        self.get_logger().info("Traj Sender Has Started")
        self.joint_pos = joint_pos
        self.time_to_reach = time_to_reach
        self.time_to_reach_ns = time_to_reach_ns

        self.action_client = ActionClient(
            self, FollowJointTrajectory, "/joint_trajectory_controller/follow_joint_trajectory"
        )

        self.action_client.wait_for_server()

        self.send_trajectory_goal()

    def send_trajectory_goal(self):
        goal_msg = FollowJointTrajectory.Goal()
        goal_msg.trajectory = JointTrajectory()
        goal_msg.trajectory.joint_names = [
            "joint_1", "joint_2", "joint_3", 
        ]
        point = JointTrajectoryPoint()
        point.positions = self.joint_pos
        point.time_from_start.sec = self.time_to_reach
        point.time_from_start.nanosec = self.time_to_reach_ns

        goal_msg.trajectory.points.append(point)

        self.future = self.action_client.send_goal_async(goal_msg)
        self.future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error("Goal rejected")
            return
        self.get_logger().info("Goal Accepted")
        goal_handle.get_result_async().add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        if result:
            self.get_logger().info("Goal completed")
        else:
            self.get_logger().error("Goal Failed")

def main(args = None):
    rclpy.init(args = args)

    joint_pos = [62.8, 6.28, 6.28,]
    time_to_reach = 3
    time_to_reach_ns = 3

    node = trajSenderNode(joint_pos, time_to_reach, time_to_reach_ns)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
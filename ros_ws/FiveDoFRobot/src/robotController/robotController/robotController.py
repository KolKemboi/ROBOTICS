#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from rclpy.action import ActionClient



class RobotPublisher(Node):
    def __init__(self, joint_pos, sec, nanosec):
        super().__init__("Publisher")
        self.get_logger().info("Publisher Has Started")
        self.pos = joint_pos
        self.sec = sec
        self.nanosec = nanosec

        self.action_client = ActionClient(
            self, FollowJointTrajectory, "/joint_trajectory_controller/follow_joint_trajectory"
        )
        self.action_client.wait_for_server()
        self.send_trajectory_node()
        
    def send_trajectory_node(self):
        goal_msg = FollowJointTrajectory.Goal()
        goal_msg.trajectory = JointTrajectory()
        goal_msg.trajectory.joint_names = [
            "joint_1", "joint_2", "joint_3", "joint_4", "joint_5" 
        ]
        point = JointTrajectoryPoint()
        point.positions = self.pos
        point.time_from_start.sec = self.sec
        point.time_from_start.nanosec = self.nanosec

        goal_msg.trajectory.points.append(point)

        self.future = self.action_client.send_goal_async(goal_msg)
        self.future.add_done_callback(self.goal_resp_callback)
        

    def goal_resp_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error("Goal Rejected")
            return
        self.get_logger().info("Success")
        goal_handle.get_result_async().add_done_callback(self.goal_result_callback)

    def goal_result_callback(self, future):
        res = future.result().result
        if res:
            self.get_logger().info("Goal Complete")
        else:
            self.get_logger().error("Failed")


def main(args = None):
    rclpy.init(args = args)
    joint = [1.3, 1.3, 1.3, 1.4, 1.5]
    sec = 2
    nanosec = 2
    node = RobotPublisher(joint, sec, nanosec)
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
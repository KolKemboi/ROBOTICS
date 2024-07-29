import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class Subscriber(Node):
    def __init__(self):
        super().__init__("teleop_subscriber")
        self.subscription = self.create_subscription(
            Twist,
            "topic",
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(msg)


def main(args=None):
    rclpy.init(args=args)
    node = Subscriber()
    rclpy.spin(node)
    rclpy.shutdown()

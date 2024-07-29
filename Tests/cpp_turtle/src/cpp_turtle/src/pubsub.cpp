#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "turtlesim/msg/pose.hpp"

using namespace std::chrono_literals;
using std::placeholders::_1;

class PosePubSub : public rclcpp::Node
{
public:
    PosePubSub()
        : Node("Turtle_pos_pub_sub"), count_(0)
    {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
        timer_ = this->create_wall_timer(
            500ms, std::bind(&PosePubSub::timer_callback, this));
        subscription_ = this->create_subscription<turtlesim::msg::Pose>(
            "/turtle1/pose", 10, std::bind(&PosePubSub::topic_callback, this, _1));
    }

private:
    void timer_callback()
    {
        auto message = geometry_msgs::msg::Twist();
        message.linear.x = 5.0;
        message.angular.z = 2.0;
        RCLCPP_INFO(this->get_logger(), "publishing");
        publisher_->publish(message);
    }
    void topic_callback(const turtlesim::msg::Pose &msg) const
    {
        RCLCPP_INFO(this->get_logger(), "I heard", msg.x, msg.angular_velocity);
    }
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr subscription_;
    size_t count_;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<PosePubSub>());
    rclcpp::shutdown();
    return 0;
}
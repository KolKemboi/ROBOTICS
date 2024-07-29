#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"

using namespace std::chrono_literals;

class PosePublisher : public rclcpp::Node
{
    public:
        PosePublisher()
        : Node("Turtle_pos_pub"), count_(0)
        {
            publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
            timer_ = this->create_wall_timer(
                500ms, std::bind(&PosePublisher::timer_callback, this)
            );
        }
    private:
        void timer_callback(){
            auto message = geometry_msgs::msg::Twist();
            message.linear.x = 5.0;
            message.angular.z = 2.0;
            RCLCPP_INFO(this->get_logger(), "publishing");
            publisher_->publish(message);
        }
        rclcpp::TimerBase::SharedPtr timer_;
        rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
        size_t count_;
};


int main(int argc, char* argv[]){
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<PosePublisher>());
    rclcpp::shutdown();
    return 0;
}
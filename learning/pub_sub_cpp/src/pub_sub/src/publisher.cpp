#include <chrono>
#include <functional>
#include <memory>

#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/twist.hpp>

using namespace std::chrono_literals;

class Publisher : public rclcpp::Node
{
public:
    Publisher() : Node("custom_publisher"), m_Count(0)
    {
        m_Publisher = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
        this->m_Timer = this->create_wall_timer(
            500ms,
            std::bind(&Publisher::publish_vel, this)
        );
    }


private:
    rclcpp::TimerBase::SharedPtr m_Timer;
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr m_Publisher;
    size_t m_Count;

private:
    void publish_vel()
    {
        geometry_msgs::msg::Twist message = geometry_msgs::msg::Twist();

        message.linear.x = 1.0;
        message.angular.z = 1.0;
        RCLCPP_INFO(this->get_logger(), "Publishing");
        m_Publisher->publish(message);

    }
};



int main(int argc, char** argv)
{
    rclcpp::init(argc, argv);
    
    std::shared_ptr<Publisher> publisher = std::make_shared<Publisher>(); 

    rclcpp::spin(publisher);
    
    rclcpp::shutdown();
}
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "turtlesim/msg/pose.hpp"

using std::placeholders::_1;

class Subscriber : public rclcpp::Node
{
public:
    Subscriber() : Node("custom_subscriber")
    {
        m_Subscriber = this->create_subscription<turtlesim::msg::Pose>(
            "/turtle1/pose",
            10,
            std::bind(&Subscriber::topic_callback, this, _1)
        );
    }

private:
    rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr m_Subscriber;

private:
    void topic_callback(const turtlesim::msg::Pose& pose) const
    {
        RCLCPP_INFO(this->get_logger(), "I heard: X = %.2f, theta = %.2f", pose.x , pose.theta);
    }
    
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    std::shared_ptr<Subscriber> subscriber = std::make_shared<Subscriber>();

    rclcpp::spin(subscriber);
    rclcpp::shutdown();
    return 0;
}

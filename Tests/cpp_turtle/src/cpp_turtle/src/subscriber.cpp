#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "turtlesim/msg/pose.hpp"

using std::placeholders::_1;

class PoseSubscriber : public rclcpp::Node
{
    public:
        PoseSubscriber()
        :Node("Turtle_pose_subscriber")
        {
            subscription_ = this->create_subscription<turtlesim::msg::Pose>(
                "/turtle1/pose", 10, std::bind(&PoseSubscriber::topic_callback, this, _1)
            );
        }
    private:
        void topic_callback(const turtlesim::msg::Pose & msg)const
        {
            RCLCPP_INFO(this->get_logger(), "I heard", msg.x, msg.angular_velocity);
        }
        rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr subscription_;
};

int main(int args, char* argv[]){
    rclcpp::init(args, argv);
    rclcpp::spin(std::make_shared<PoseSubscriber>());
    rclcpp::shutdown();
    return 0;
}
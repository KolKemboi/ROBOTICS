#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"

#include <chrono>
#include <cstdlib>
#include <memory>

using namespace std::chrono_literals;

int main(int argc, char **argv){
    rclcpp::init(argc, argv);

    if (argc != 3){
        RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "usage: add two ints x, y");
        return -1;
    }
    std::shared_ptr<rclcpp::Node> node = rclcpp::Node::make_shared("add_two_ints");
    rclcpp::Client<example_interfaces::srv::AddTwoInts>::SharedPtr client = node->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");

    auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
    request->a = atoll(argv[1]);
    request->b = atoll(argv[2]);

    rclcpp::shutdown;
}
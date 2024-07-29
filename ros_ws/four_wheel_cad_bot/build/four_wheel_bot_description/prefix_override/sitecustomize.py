import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/kol/Documents/Robotics/ros_ws/four_wheel_cad_bot/install/four_wheel_bot_description'

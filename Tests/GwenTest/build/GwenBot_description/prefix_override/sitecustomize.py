import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/kol/Documents/Robotics/Tests/GwenTest/install/GwenBot_description'

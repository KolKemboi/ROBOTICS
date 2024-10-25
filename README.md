# Robots 
Programmed using ROS2

A collection of robot types

<h2>A FIVE DOF ROBOT</h2>
This robot type has five degrees of freedom. It Offers a chuck mounted to the end that spins. This allows mounting of Tools for
machining. It was designed as a mechatronic system for machining purposes.
Its is controlled using a python script that publishes to contol_msgs and trajectory_msgs.
The robot uses an FK system

![image url](https://github.com/KolKemboi/ROBOTICS/blob/be452c4aa19daecc51d3d53a50841640a3c88354/Five%20DoF%20robot.png)

![image url](https://github.com/KolKemboi/ROBOTICS/blob/be452c4aa19daecc51d3d53a50841640a3c88354/Five%20DoF.png)

<h2>A FOUR WHEELED ROBOT</h2>
This is a four wheeled robot that uses a differential drive mechanism. This allow both velocity and angular messages to be published 
to it.
The messages are pushed to The topic "cmd_vel_unstamped" topic

![image url](https://github.com/KolKemboi/ROBOTICS/blob/be452c4aa19daecc51d3d53a50841640a3c88354/Four%20Wheel%20Bot.png)

<h2>WELDER ROBOT</h2>
This is a six degree of freedom robot. It features a chuck for mounting a TIG or any other welding mechanism.
It is a mechactronic system for welding.
Its is controlled using a python script that publishes to contol_msgs and trajectory_msgs.
The robot uses an FK system

![image url](https://github.com/KolKemboi/ROBOTICS/blob/be452c4aa19daecc51d3d53a50841640a3c88354/Six%20DoF%20robot.png)

<h2>GWEN => A CRAWLER ROBOT</h2>
Continuing with my robotics journey, I decided to make a robot that walks on 4 legs.
The name is inspired by the Marvel Character Gwen Stacy - Spider Gwen - the color code of the 
crawler also follows Gwen's colors in the MCU.

![image url](https://github.com/KolKemboi/ROBOTICS/blob/bd547804aac03944c04c0e7184f7632fe97a1d7e/Gwenbot%20v1.png)

![image url](https://github.com/KolKemboi/ROBOTICS/blob/bd547804aac03944c04c0e7184f7632fe97a1d7e/Gwenbot%20v3.png)



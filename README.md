# AgNW-sensor-AR-Robot
Silver Nanowire sensor Robot teleoperation and AR

## Arduino files
**3_sensor_ros_and_serial:** reads the signal from the set of 3 sensors and publishes the values in ROS under /sensor_values topic. Can ,odify to read more fingers (3-5, etc.).

**5_sensor_circuit_read_v:** initial code that read 5 fingers and plotted them in a serial plot. In the current version it read only 3. The rest is commented.

**calibration:** code that we used to do calibration with the manipulator. The code is more or less the same, execpt that only one value is published in ROS.

**calib:** calibration data. Contains both old and newer data in csv files. Also uploaded to Google drive folder and used in Google Colab to plot the graphs.

**turtlebot3_bringup:** bringup the turtlebot to establish a connection between the computer and robot. Set it up for work basically.

**turtlebot_teleop**: teleoperate the turtlebot burger 3 using the teleop_key node. (We modified the code for our purposes).

**turtlebot3_slam**: SLAM for turtlebot. Standard package.

Setup Arduino for ROS: https://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup

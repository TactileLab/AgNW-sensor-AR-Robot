# AgNW-sensor-AR-Robot
Silver Nanowire sensor Robot teleoperation and AR

## Arduino files
**3_sensor_ros_and_serial:** reads the signal from the set of 3 sensors and publishes the values in ROS under /sensor_values topic. Can ,odify to read more fingers (3-5, etc.).

**5_sensor_circuit_read_v:** initial code that read 5 fingers and plotted them in a serial plot. In the current version it read only 3. The rest is commented.

**calibration:** code that we used to do calibration with the manipulator. The code is more or less the same, execpt that only one value is published in ROS.

**turtlebot_teleop**: teleoperate the turtlebot burger 3 using the teleop_key node.  

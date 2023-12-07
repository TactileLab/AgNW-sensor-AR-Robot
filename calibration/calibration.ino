#include <ros.h>

/////////////////////
#include <std_msgs/String.h>

#include "std_msgs/MultiArrayLayout.h"
#include "std_msgs/MultiArrayDimension.h"
#include "std_msgs/Float64.h"
#include "std_msgs/Float64MultiArray.h"
///////////////////

#define WINDOW_SIZE 5

////////////////////////////////////  
ros::NodeHandle nh;

std_msgs::Float64 values;
ros::Publisher sensor_values("sensor_values", &values);
//////////////////////////////////////

void setup() {
  Serial.begin(9600) ;
  pinMode(A0,INPUT);

  nh.initNode();
  nh.advertise(sensor_values);
  
}

void loop() {
  float sensorVal1 = analogRead(A0);
  float voltageVal1 = sensorVal1 * (5.0/1023);

  float sensorVal2 = analogRead(A2);
  float voltageVal2 = sensorVal2 * (5.0/1023);
  
  float sensorVal3 = analogRead(A4);
  float voltageVal3 = sensorVal3 * (5.0/1023);

  Serial.print(voltageVal1);
  Serial.print("; ");
  Serial.print(voltageVal2);
  Serial.print("; ");
  Serial.println(voltageVal3);

  
  float value = voltageVal2;
  values.data = value;
  
  sensor_values.publish(&values);
  
  nh.spinOnce();  
  delay(10);

}
#!/usr/bin/env python3

from lib2to3.pgen2.token import NEWLINE
from logging import shutdown
import re
import rospy
import copy
import os
import time
import csv
import pandas as pd
import numpy as np
# from std_msgs.msg import Int32
from calib.msg import forces_3d
from geometry_msgs.msg import WrenchStamped
from datetime import datetime
import sys
from calib.msg import FrankaState
from std_msgs.msg import Float64

# force data variables
###############
ebts_force = [0.000] * 1
weiss_force = [0.000] * 3
delta_z = [0.000]*3

# other functions' variables 
###############
elapsed = 0
counter = 0
start = time.time()
dateTimeObj = datetime.now()
filename = str(dateTimeObj.strftime("%Y-%m-%d-%H-%M-%S"))
data_row = pd.DataFrame()
data_all = pd.DataFrame()



#####################################################
def listener1_callback(data):
    global weiss_force
    weiss_force[0] = data.wrench.force.x
    weiss_force[1] = data.wrench.force.y
    weiss_force[2] = data.wrench.force.z

def listener2_callback(msg):
    global ebts_force
    # ebts_force = data
    ebts_force[0] = msg.data
    # ebts_force[1] = data.force_y
    # ebts_force[2] = data.force_z

def deltaz_callback(data):
    global delta_z
    
    delta_z[0] = data.O_T_EE[14] # z
    delta_z[1] = data.O_T_EE[12] # x
    delta_z[2] = data.O_T_EE[13] # y

# subscribe to topic weiss  
def listener1():
    rospy.init_node('listener1', anonymous=True)
    rospy.Subscriber("/wrench", WrenchStamped, listener1_callback)

# subscribe to topic ebts
def listener2():
    rospy.Subscriber("/sensor_values", Float64, listener2_callback)

def listener3():
    rospy.Subscriber('/franka_state_controller/franka_states', FrankaState, deltaz_callback)    

#####################################################
def rec():       
    global elapsed, data_all, data_row, counter, start, dateTimeObj, filename, weiss_force, ebts_force, delta_z

    counter = counter + 1

    if (counter == 1):
        dateTimeObj = datetime.now()
        filename = str(dateTimeObj.strftime("%Y-%m-%d-%H-%M-%S"))
        start = time.time()

    time_k = 60  # duration of data collection          

    if(counter > 0):

        if (elapsed <= time_k):  # some time period
            data_row = pd.concat( [pd.DataFrame(weiss_force), pd.DataFrame(ebts_force), pd.DataFrame(delta_z)], axis = 0)
            data_all = pd.concat([data_all, data_row.transpose()], axis = 0)

            elapsed = time.time() - start

        if (elapsed >= time_k):
            print("stopped recording...")   
            print("saving data") 
            data_all = pd.DataFrame(data_all)

            data_2_save = copy.deepcopy(data_all)
            data_2_save.to_csv(filename + ".csv")

            data_now = pd.DataFrame()
            data_all = pd.DataFrame()
            counter = 0
            elapsed = 0
            sys.exit()




if __name__ == '__main__':
    
    listener1()
    listener2()
    listener3()
    rate = rospy.Rate(100) #10hz

    try:
        while not rospy.is_shutdown():
            rec()
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
    
    rospy.spin()
    
    

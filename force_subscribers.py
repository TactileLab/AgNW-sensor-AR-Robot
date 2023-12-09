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
from std_msgs.msg import Int32
# from tracking.msg import forces_3d
from geometry_msgs.msg import WrenchStamped
from datetime import datetime
import sys
from xela_server.msg import xServerMsg
from wittenstein_msgs.msg import wittenstein
# from tracking.msg import FrankaState
from std_msgs.msg import Float64

# force data variables
###############
# ebts_force = [0.000] * 3
# weiss_force = [0.000] * 3
# desired_force = [0.000] * 3
# delta_z = [0.000]*3
# alldist = [0.000]*3
xela_z = [0] * 16
witten = [0.000] * 3

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
# def listener2_callback(data):
#     global ebts_force
#     ebts_force[0] = data.force_x
#     ebts_force[1] = data.force_y
#     ebts_force[2] = data.force_z

# def listener1_callback(data):
#     global weiss_force
#     weiss_force[0] = data.wrench.force.x
#     weiss_force[1] = data.wrench.force.y
#     weiss_force[2] = data.wrench.force.z

def wittenstein_callback(data):
    global witten 
    witten[0] = data.fx
    witten[1] = data.fy
    witten[2] = data.fz

# def deltaz_callback(data):
#     global delta_z
    
#     delta_z[0] = data.O_T_EE[14] # z
#     delta_z[1] = data.O_T_EE[12] # x
#     delta_z[2] = data.O_T_EE[13] # y
#     #print(delta_z)

# def pixel_callback(msg):
#     global alldist

#     alldist[0] = msg.data
#     #print(alldist)

# def listener5_callback(data):
#     global desired_force
#     desired_force[0] = data.wrench.force.x
#     desired_force[1] = data.wrench.force.y
#     desired_force[2] = data.wrench.force.z

def listener_xela_callback(data):
    global xela_z
    xela_z[0] = data.points[0].point.z
    xela_z[1] = data.points[1].point.z
    xela_z[2] = data.points[2].point.z
    xela_z[3] = data.points[3].point.z
    xela_z[4] = data.points[4].point.z
    xela_z[5] = data.points[5].point.z
    xela_z[6] = data.points[6].point.z
    xela_z[7] = data.points[7].point.z
    xela_z[8] = data.points[8].point.z
    xela_z[9] = data.points[9].point.z
    xela_z[10] = data.points[10].point.z
    xela_z[11] = data.points[11].point.z
    xela_z[12] = data.points[12].point.z
    xela_z[13] = data.points[13].point.z
    xela_z[14] = data.points[14].point.z
    xela_z[15] = data.points[15].point.z

# subscribe to topic weiss  
def listener_witt():
    rospy.init_node('listener1', anonymous=True)
    rospy.Subscriber("/wittenstein_topic", wittenstein, wittenstein_callback)

# # subscribe to topic ebts
# def listener2():
#     rospy.Subscriber("forces_3d_pub", forces_3d, listener2_callback)
# # z axis of the
# def listener3():
#     rospy.Subscriber('/franka_state_controller/franka_states', FrankaState, deltaz_callback)    
# def listener4():
#     rospy.Subscriber('/pixel_pub', Float32, pixel_callback)    

# def listener5():
#     # rospy.init_node('listener1', anonymous=True)
#     rospy.Subscriber("/desired_force", WrenchStamped, listener5_callback)

def listener_xela():
    rospy.init_node('listener1', anonymous=True)
    rospy.Subscriber("/xServTopic", xServerMsg, listener_xela_callback)

#####################################################
def rec():       
    global elapsed, data_all, data_row, counter, start, dateTimeObj, filename, xela_z, witten

    counter = counter + 1

    if (counter == 1):
        dateTimeObj = datetime.now()
        filename = str(dateTimeObj.strftime("%Y-%m-%d-%H-%M-%S"))
        start = time.time()

    time_k = 10 # duration of data collection          
    

    if(counter > 0):

        if (elapsed <= time_k):  # some time period
            data_row = pd.concat( [pd.DataFrame(xela_z), pd.DataFrame(witten)], axis = 0)
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
    
    # dir1 = "/media/togzhan/windows 2/documents/lump_files/data/trial_records"
    # dir1 = "/media/togzhan/windows 2/documents/lump_files/data/trial_records/data_collection/Azamat/11"
    # os.chdir(dir1)
    # dir1 = "/media/togzhan/windows 2/documents/lump_files/data/trial_records/Karina_trials/Karina_trial_2/without"
    # dir1 = "/media/togzhan/windows 2/documents/lump_files/data/trial_records/data_collection/Saltanat/13"
    # os.chdir(dir1)
    # listener1()
    # listener2()
    # listener3()
    # listener4()
    # listener5()
    listener_witt()
    listener_xela()
    rate = rospy.Rate(100) #10hz

    try:
        while not rospy.is_shutdown():
            rec()
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
    
    rospy.spin()
    
    

#!/usr/bin/env python

import numpy as np
import random
import math
import rospy
import roscpp
from   std_msgs.msg       import Float64
from   geometry_msgs.msg  import Twist
from   visualization_msgs.msg  import MarkerArray
from   visualization_msgs.msg  import Marker
import csv


f1_x = 0.0
f1_y= 0.0
f1_z = 0.0

f2_x = 0.0
f2_y= 0.0
f2_z = 0.0

f3_x = 0.0
f3_y= 0.0
f3_z = 0.0

f4_x = 0.0
f4_y= 0.0
f4_z = 0.0

header = ['f1_x', 'f1_y', 'f1_z', 'f2_x', 'f2_y', 'f2_z', 'f3_x', 'f3_y', 'f3_z', 'f4_x', 'f4_y', 'f4_z']

f = open('src/Spot_Sim/data_acq/src/pos.csv', 'w')
writer = csv.writer(f)
writer.writerow(header)

def get_position(data1):
    global f1_x, f1_y, f1_z, f2_x, f2_y, f2_z, f3_x, f3_y, f3_z, f4_x, f4_y, f4_z

    markers = data1.markers

    f1_x = markers[0].pose.position.x
    f1_y = markers[0].pose.position.y
    f1_z = markers[0].pose.position.z

    f2_x = markers[1].pose.position.x
    f2_y = markers[1].pose.position.y
    f2_z = markers[1].pose.position.z

    f3_x = markers[2].pose.position.x
    f3_y = markers[2].pose.position.y
    f3_z = markers[2].pose.position.z

    f4_x = markers[3].pose.position.x
    f4_y = markers[3].pose.position.y
    f4_z = markers[3].pose.position.z

    print('Foot 1 x: = {}'.format(f1_x))
    print('Foot 1 y: = {}'.format(f1_y))
    print('Foot 1 z: = {}'.format(f1_z))
    print('Foot 2 x: = {}'.format(f2_x))
    print('Foot 2 y: = {}'.format(f2_y))
    print('Foot 2 z: = {}'.format(f2_z))
    print('Foot 3 x: = {}'.format(f3_x))
    print('Foot 3 y: = {}'.format(f3_y))
    print('Foot 3 z: = {}'.format(f3_z))
    print('Foot 4 x: = {}'.format(f4_x))
    print('Foot 4 y: = {}'.format(f4_y))
    print('Foot 4 z: = {}'.format(f4_z))

    # if writer is not None:
    writer.writerow([f1_x, f1_y, f1_z, f2_x, f2_y, f2_z, f3_x, f3_y, f3_z, f4_x, f4_y, f4_z])


def main():

    global f1_x, f1_y, f1_z, f2_x, f2_y, f2_z, f3_x, f3_y, f3_z, f4_x, f4_y, f4_z


    rospy.init_node('data_acq', anonymous=True)
    rate = rospy.Rate(5) # 5hz

    rospy.loginfo("This Node is working")

    sub = rospy.Subscriber('/foot', MarkerArray, get_position)
    
        


    

    # while not rospy.is_shutdown():
        
        # print('Foot 1 x: = {}'.format(f1_x))
        # print('Foot 1 y: = {}'.format(f1_y))
        # print('Foot 1 z: = {}'.format(f1_z))
        # print('Foot 2 x: = {}'.format(f2_x))
        # print('Foot 2 y: = {}'.format(f2_y))
        # print('Foot 2 z: = {}'.format(f2_z))
        # print('Foot 3 x: = {}'.format(f3_x))
        # print('Foot 3 y: = {}'.format(f3_y))
        # print('Foot 3 z: = {}'.format(f3_z))
        # print('Foot 4 x: = {}'.format(f4_x))
        # print('Foot 4 y: = {}'.format(f4_y))
        # print('Foot 4 z: = {}'.format(f4_z))
        
        # rate.sleep()
    rospy.spin()
    f.close()
    csv_writer = None


if __name__ == '__main__':
    main()
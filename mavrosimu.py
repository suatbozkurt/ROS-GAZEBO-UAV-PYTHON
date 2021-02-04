#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu

def callback(data):
  rospy.loginfo(data)

def mavros_imu_subscriber():
   rospy.init_node('imu_subscriber',anonymous=False)
   rospy.Subscriber("/mavros/imu/data",Imu,callback)
   rospy.spin()

if __name__ == '__main__':
  while not rospy.is_shutdown():
    mavros_imu_subscriber()


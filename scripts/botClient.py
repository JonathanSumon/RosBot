#!/usr/bin/env python
import rospy
from std_msgs.msg import String

pub = rospy.Publisher('chatter', String,queue_size=10)
rospy.init_node('client_bot') 

while not rospy.is_shutdown():

   input = raw_input("Ask me anything :> ")
   pub.publish(input)
   rospy.Rate(1).sleep()

   

#!/usr/bin/env python


import rospy
import aiml
import os
import sys


from std_msgs.msg import String

rospy.init_node('server_bot')
mybot = aiml.Kernel()
response_publisher = rospy.Publisher('response',String,queue_size=10)



def load_Ai(xml_file):

	data_path = rospy.get_param("Alice.ai")
	print data_path
	os.chdir(data_path)


	if os.path.isfile("standard.brn"):
		mybot.bootstrap(brainFile = "standard.brn")

	else:
		mybot.bootstrap(learnFiles = xml_file, commands = "load b")
		mybot.saveBrain("standard.brn")


        

def callback(data):

	input = data.data
	response = mybot.respond(input)
	rospy.loginfo("I Heard:: %s",data.data)
	rospy.loginfo("I Spoke:: %s",response)
	response_publisher.publish(response)
  

def listener():

	rospy.loginfo("Starting ROS Smart Bot")
	rospy.Subscriber("chatter", String, callback)
	rospy.spin()

if __name__ == '__main__':

	load_Ai('startup.xml')
	listener()


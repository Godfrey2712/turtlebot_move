#! /usr/bin/env python
from time import sleep
import rospy
from geometry_msgs.msg import Twist


rospy.init_node('rotate')

publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

rotate_right = True

while not rospy.is_shutdown():
    msg = Twist()
    msg.linear.x = 0.47
    msg.linear.y = -0.83
    msg.linear.z = 0.127
   # msg.angular.z = 2.0 if rotate_right else -2.0

    publisher.publish(msg)
    rospy.loginfo('Hi Team Turtebot')
    #rotate_left = not rotate_right
    sleep(10)

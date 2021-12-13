#! /usr/bin/env python3
import rospy
from std_msgs.msg import String 

if __name__ == "__main__":
    rospy.init_node("sample_pub2")
    pub  =rospy.Publisher("hello02" , String, queue_size=10) 
    rate = rospy.Rate(10) 
    while True:
        str = "kimheyh: %s" % rospy.get_time() 
        pub.publish(str) 
        rate.sleep()
    pass
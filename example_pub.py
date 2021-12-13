#! /usr/bin/env python3
import rospy
from std_msgs.msg import String 

if __name__ == "__main__":
    rospy.init_node("sample_pub")
    
    pub  =rospy.Publisher("hello" , String, queue_size=10) 
    
    pub1  =rospy.Publisher("hello01" , String, queue_size=10)#2개의 파일로 할 때는 주석처리
    rate = rospy.Rate(10) 
    while True:
        str = "hello_publisher: %s" % rospy.get_time() 
        str1 = "changseon1: %s" % rospy.get_time() #2개의 파일로 할 때는 주석처리
        pub.publish(str) 
        pub1.publish(str1) #2개의 파일로 할 때는 주석처리
        rate.sleep() 
    pass
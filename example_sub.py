#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

def fun_callback(msg):
    rospy.loginfo("%s" , msg.data) # print()와 똑같다
    return

if __name__ == "__main__":
    rospy.init_node("sample_sub")
    
    rospy.Subscriber("hello", String, callback=fun_callback)
    rospy.Subscriber("hello01", String, callback=fun_callback)
    rospy.Subscriber("hello02", String, callback=fun_callback)  #나는 행동을 할거야. 형식은 string으로    
    rospy.spin() 
    pass
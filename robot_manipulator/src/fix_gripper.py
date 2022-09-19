#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String, Float64

def talker():
    rate = rospy.Rate(10) # 10hz
    pub7 = rospy.Publisher('/robot_manipulator/joint7_position_controller/command', Float64, queue_size=10)
    pub8 = rospy.Publisher('/robot_manipulator/joint8_position_controller/command', Float64, queue_size=10)
    pub15 = rospy.Publisher('/robot_manipulator/joint15_position_controller/command', Float64, queue_size=10)
    pub16 = rospy.Publisher('/robot_manipulator/joint16_position_controller/command', Float64, queue_size=10)

    rospy.sleep(5)
    pub7.publish(0)
    pub15.publish(0)
    pub8.publish(0)
    pub16.publish(0)
    


if __name__ == '__main__':
    try:
        rospy.init_node('talker', anonymous=True)

        talker()
    except rospy.ROSInterruptException:
        pass

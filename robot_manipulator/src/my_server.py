#! /usr/bin/env python

import rospy
from std_msgs.msg import String, Float64
import actionlib
import actionlib_tutorials.msg
import robot_manipulator.msg
from robot_manipulator.msg import MyActionAction,MyActionFeedback,MyActionResult

class MyAction(object):
    # create messages that are used to publish feedback/result
    _feedback = MyActionFeedback()
    _result = MyActionResult()


    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name,  MyActionAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()

    def execute_cb(self, goal):

        r = rospy.Rate(3)
        r.sleep()
        success = False
        if goal.order == 'pick_up_container':
            #first step
            pub1.publish(-1.18)
            rospy.sleep(2.5)
            pub2.publish(0.32)
            rospy.sleep(2.5)
            pub3.publish(-1.45)
            rospy.sleep(2)
            pub5.publish(2)
            rospy.sleep(2.5)
            pub4.publish(-1.69)
            rospy.sleep(2.5)
            pub6.publish(0)
            rospy.sleep(2.5)
            pub7.publish(0)
            rospy.sleep(2.5)
            pub8.publish(0)


            #second step

            pub4.publish(-1.49) #49
            rospy.sleep(3)
            pub3.publish(-1.85) #85
            rospy.sleep(3)
            pub5.publish(1.4)
            rospy.sleep(5)




            #GRAB THE CONTAINER
            pub7.publish(0.12)
            pub8.publish(-0.12)
            rospy.sleep(4)

            #LIFT IT IN THE AIR
            pub3.publish(-1)
            rospy.sleep(1)
            pub5.publish(0.5)
            rospy.sleep(3)
            #END OF MOVEMENT
            success = True




        if goal.order == 'drop_container':
            #return it to its place
            pub3.publish(-1.7)
            rospy.sleep(3)
            pub3.publish(-1.8)
            rospy.sleep(3)
            pub7.publish(0)
            pub8.publish(0)
            success = True

        if goal.order == 'fill_shot_glass_with_ingredient':
            #left hand picks up the shot glass to begin with.
            pub9.publish(1.9)
            rospy.sleep(1)
            pub15.publish(0)
            pub16.publish(0)
            pub14.publish(0)

            pub13.publish(-1.3)
            rospy.sleep(3)
            pub10.publish(-0.9)
            rospy.sleep(2)
            pub12.publish(1.68)  #1.47
            rospy.sleep(2)
            pub11.publish(2.25)
            rospy.sleep(3)

            #second step
            pub11.publish(2.3)
            rospy.sleep(3)
            pub12.publish(1.5)  #1.47
            rospy.sleep(2)
            pub10.publish(-0.65)
            rospy.sleep(3)

            #close the gripper
            pub15.publish(0.1)
            pub16.publish(-0.1)
            rospy.sleep(4)

            #now lift it in the AIR
            pub11.publish(0.9)
            rospy.sleep(0.3)
            pub13.publish(0)


            #now it's time to use both hands


            pub1.publish(-1)
            rospy.sleep(1)
            pub9.publish(2)
            rospy.sleep(1)
            pub2.publish(0.8)
            rospy.sleep(1)
            pub10.publish(-1.3)
            rospy.sleep(1)
            pub3.publish(-1)
            rospy.sleep(1)
            pub11.publish(1.5)
            rospy.sleep(1)
            pub4.publish(-1.49)
            rospy.sleep(1)
            pub5.publish(0)

            #turn in respect to axis-z
            pub1.publish(-0.8)
            pub9.publish(0.8)
            rospy.sleep(1)

            #now turn the container slowly
            for i in range(15):
                pub6.publish(-0.5-0.1*i)
                rospy.sleep(0.7)

	    #now put down the container
            pub6.publish(0)
            pub5.publish(1.4)
            rospy.sleep(5)

            pub1.publish(-1.18)
            rospy.sleep(2.5)
            pub2.publish(0.32)
            rospy.sleep(2.5)
            pub3.publish(-1.85) #85
            rospy.sleep(3)

            pub4.publish(-1.49) #49
            pub6.publish(0)
            rospy.sleep(2)

            pub7.publish(0)
            pub8.publish(0)






            success = True

    	if goal.order == 'pour_ingredient_from_shot_shot_glass_to_clean_pitcher':
            #grab the cup

            pub2.publish(1.1)
            pub4.publish(-2)
            rospy.sleep(2.5)
            pub3.publish(-2.5)
            rospy.sleep(2)

            pub1.publish(-1.55)
            rospy.sleep(2)

            pub5.publish(0.8)
            rospy.sleep(2.5)
            pub4.publish(-1.3)
            rospy.sleep(2.5)
            pub6.publish(0)
            pub7.publish(0)
            pub8.publish(0)


            #second step
            pub5.publish(0.9)
            rospy.sleep(2.5)
            pub2.publish(0.8)
            rospy.sleep(2.5)
            pub7.publish(0.09)
            pub8.publish(-0.09)


            #lift the cup and move the shot glass
            pub2.publish(0.9)
            rospy.sleep(1.5)
            pub3.publish(-1.2)
            rospy.sleep(1)
            pub5.publish(0.6)
            rospy.sleep(2.5)
            pub11.publish(1.4)
            pub4.publish(-2)
            rospy.sleep(2.5)
            pub6.publish(0)
            rospy.sleep(2.5)
            pub1.publish(-0.6)
            pub9.publish(1)
            rospy.sleep(2.5)

            for i in range(12):
                pub14.publish(0.5+0.1*i)
                rospy.sleep(0.7)

            #drop the shot glass
            pub14.publish(0)
            pub9.publish(1.9)
            rospy.sleep(1)

            pub13.publish(-1.3)
            rospy.sleep(3)

            #second step
            pub11.publish(2.3)
            rospy.sleep(3)
            pub12.publish(1.5)  #1.47
            rospy.sleep(2)
            pub10.publish(-0.65)
            rospy.sleep(3)

            #open the gripper
            pub15.publish(0)
            pub16.publish(0)


            #serve the coffee!!!
            pub1.publish(-1.4)
            rospy.sleep(2.5)
            pub2.publish(0)
            pub4.publish(-1)
            rospy.sleep(2)
            pub3.publish(-1.3)
            rospy.sleep(2.5)

            success = True

















        # publish info to the console for the user
        #rospy.loginfo('%s: Executing, creating fibonacci sequence of order %i with seeds %i, %i' % (self._action_name, goal.order, self._feedback.sequence[0], self._feedback.sequence[1]))

        # start executing the action
            # check that preempt has not been requested by the client
        if self._as.is_preempt_requested():
            rospy.loginfo('%s: Preempted' % self._action_name)
            self._as.set_preempted()
            success = False


        self._feedback.sequence.append(0)
        # publish the feedback
        #self._as.publish_feedback(self._feedback)
        # this step is not necessary, the sequence is computed at 1 Hz for demonstration purposes
        #r.sleep()

        if success:
            self._result.sequence = self._feedback.sequence
            rospy.loginfo('%s: Succeeded' % self._action_name)
            self._as.set_succeeded(self._result)

if __name__ == '__main__':
    rospy.init_node('MyActionServer')
    server = MyAction(rospy.get_name())
    pub1 = rospy.Publisher('/robot_manipulator/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/robot_manipulator/joint2_position_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/robot_manipulator/joint3_position_controller/command', Float64, queue_size=10)
    pub4 = rospy.Publisher('/robot_manipulator/joint4_position_controller/command', Float64, queue_size=10)
    pub5 = rospy.Publisher('/robot_manipulator/joint5_position_controller/command', Float64, queue_size=10)
    pub6 = rospy.Publisher('/robot_manipulator/joint6_position_controller/command', Float64, queue_size=10)
    pub7 = rospy.Publisher('/robot_manipulator/joint7_position_controller/command', Float64, queue_size=10)
    pub8 = rospy.Publisher('/robot_manipulator/joint8_position_controller/command', Float64, queue_size=10)
    pub9 = rospy.Publisher('/robot_manipulator/joint9_position_controller/command', Float64, queue_size=10)
    pub10 = rospy.Publisher('/robot_manipulator/joint10_position_controller/command', Float64, queue_size=10)

    pub11 = rospy.Publisher('/robot_manipulator/joint11_position_controller/command', Float64, queue_size=10)
    pub12 = rospy.Publisher('/robot_manipulator/joint12_position_controller/command', Float64, queue_size=10)
    pub13 = rospy.Publisher('/robot_manipulator/joint13_position_controller/command', Float64, queue_size=10)
    pub14 = rospy.Publisher('/robot_manipulator/joint14_position_controller/command', Float64, queue_size=10)
    pub15 = rospy.Publisher('/robot_manipulator/joint15_position_controller/command', Float64, queue_size=10)
    pub16 = rospy.Publisher('/robot_manipulator/joint16_position_controller/command', Float64, queue_size=10)
    pub17 = rospy.Publisher('/robot_manipulator/joint17_position_controller/command', Float64, queue_size=10)
    pub18 = rospy.Publisher('/robot_manipulator/joint18_position_controller/command', Float64, queue_size=10)
    # rospy.Subscriber("chatter", String, execute_cb)
    rospy.spin()

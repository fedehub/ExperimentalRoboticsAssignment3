
import rospy
import smach
import smach_ros

class Foo(smach.State):
	 def __init__(self, outcomes=['outcome1', 'outcome2']):
		# Your state initialization goes here
		pass

	 def execute(self, userdata):
		# Your state execution goes here
		pass





if __name__ == "__main__":
	rospy.init_node("state_machine")
	
	# ... services and topics ...
	
	# ... state machine ...
	
	rospy.spin()


import rospy

from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovariance, Pose, Point, Quaternion
from geometry_msgs.msg import Point, Vector3
from std_msgs.msg import String
from erl_assignment_3_msgs.msg import GoToPoint, GoToPointRequest, GoToPointResponse

import math

from move_base_msgs.msg import MoveBaseActionGoal



odometry_topic = "/odom"
''' name of the odometry source topic
'''

last_odometry = Odometry()
''' last received odometry (nav_msgs/Odometry)
'''

last_pos = Point()
''' the last position returned by the odometry
'''

def read_odom(data):
	''' read and save the data from the Odometry topic
	
	Parameters:
		data (nav_msgs/Odometry):
			the current odometry message
	'''
	global last_odometry
	global las_pos
	
	last_odometry = data
	last_pos = data.pose.pose.position
	
	# rospy.loginfo("pos(" + str(data.pose.pose.position.x) + ", " + str(data.pose.pose.position.y) + ")")


def dist_vector(P1, P2):
	'''returns the difference vector betwee the points.
	'''
	
	v = Vector3()
	
	v.x = P1.x - P2.x
	v.y = P1.y - P2.y
	v.z = P1.z - P2.z
	
	return v

def distance(P1, P2):
	''' eucledian distance between P1 and P2
	
	Parameters:
		P1 (geometry_msgs/Point) : first point
		P2 (geometry_msgs/Point) : second point
	'''
	
	v = dist_vector(P1, P2) 
	
	return math.sqrt(v.x**2 + v.y**2 + v.z**2)



move_base_goal_topic = "/move_base/goal"
''' goal topic name for commanding the navigation stack
'''

pub_move_base = None
''' publisher to the /move_base/goal topic (move_base/MoveBaseGoal)
'''

last_target = Point()
''' last required target (geometry_msgs/Point)
'''

def send_move_base(x,y):
	'''send a goal to the navigation stack
	
	Parameters:
		x (float) : x coordinate
		y (float) : y coordinate

	'''
	global pub_move_base
	global last_target
	global working
	
	goal = MoveBaseActionGoal()
	
	goal.header.frame_id = 'map'
	goal.goal.target_pose.header.frame_id = 'map'
	goal.goal.target_pose.pose.position.x = x
	goal.goal.target_pose.pose.position.y = y
	goal.goal.target_pose.pose.position.z = 0.0
	goal.goal.target_pose.pose.orientation.x = 0.0
	goal.goal.target_pose.pose.orientation.y = 0.0
	goal.goal.target_pose.pose.orientation.z = 0.0
	goal.goal.target_pose.pose.orientation.w = 1.0
	
	pub_move_base.publish(goal)
	(rospy.Duration(1)).sleep()
	
	last_target = goal.goal.target_pose.pose.position



def go_to_point(req):
	''' service implementation of /go_to_point
	
	the service calls MoveBase and waits until the robot hasn't reached
	the given target. 
	
	Parameters:
		req (erl_assignment_3_msgs/GoToPointRequest):
			the target point to go at
	
	Returns
		res (erl_assignment_3_msgs/GoToPointResponse):
			whether the request succeeded or not. 
	'''
	
	# make the request to the nav stack
	send_move_base( req.target.x, req.target.y )
	
	# wait for the request
	r = rospy.Rate(10)
	while not rospy.is_shutdown():
		r.sleep()
		
		if distance( last_target, last_pos ) < 0.01:
			# cancel the request
			break
	
	return GoToPointResponse(True)



if __name__ == "__main__":
	rospy.init_node("navigation_node")
	
	rospy.loginfo("pub movebase")
	pub_move_base = rospy.Publisher(move_base_goal_topic, MoveBaseActionGoal, queue_size=100)
	(rospy.Duration(1)).sleep()
	
	rospy.loginfo("sub odometry")
	rospy.Subscriber(odometry_topic, Odometry, read_odom, queue_size=100)
	
	rospy.loginfo("srv go to point")
	rospy.Service
	
	rospy.loginfo("ros spin")
	rospy.spin()
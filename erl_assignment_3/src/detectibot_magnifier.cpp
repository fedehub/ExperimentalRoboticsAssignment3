

#include "ros/ros.h"
#include "cv_bridge/cv_bridge.h"
#include "sensor_msgs/image_encodings.h"
#include "aruco/aruco.h"
#include "erl_assignment_3_msgs/GetArucoIds.h"

#include <opencv2/imgproc/imgproc.hpp> 
#include <opencv2/highgui/highgui.hpp>
#include <image_transport/image_transport.h>

#include "sensor_msgs/Image.h"

#include <string>
#include <vector>
#include <algorithm>

/// window name
// static const std::string OPENCV_WINDOW = "DetectiCam";

class detectibot_magnifier_class
{
public:
	
	/** detectibot_magnifier_class class constructor */
	detectibot_magnifier_class() : it(nh)
	{
		sem=false;
		
		// open the channels
		image_sub = it.subscribe("/img_echo" , 1, &detectibot_magnifier_class::image_callback, this);
		srv_aruco_ids = nh.advertiseService("aruco_markers", &detectibot_magnifier_class::get_ids, this);
		
		// open the window
		// cv::namedWindow(OPENCV_WINDOW);
		
		// aruco configuration
		mDetector.setDictionary("ARUCO_MIP_36h12");
		// camParam = aruco::CameraParameters();
		nh.param<bool>("use_camera_info", useCamInfo, false);
	}
	
	/** detectibot_magnifier_class node class destructor */
	~detectibot_magnifier_class()
	{
		// destroy the window
		// cv::destroyWindow(OPENCV_WINDOW);
	}
	
	/** continuously detect the new IDs from ArUco */
	void spin()
	{
		ros::Rate r(1);
		while(ros::ok())
		{
			r.sleep();
			
			if(!sem) sem=true;
			else continue;
			
			for(int i=0; i<markers.size(); ++i) 
			{
				if(std::find(detected_ids.begin(), detected_ids.end(), markers[i].id) != detected_ids.end())
					detected_ids.push_back(markers[i].id);
			}
			
			detectibot_magnifier_class::sem=false;
		}
	}
	
	/** receive the image, get the ARUCO markers, then send the detections through the out topic */
	void image_callback(const sensor_msgs::ImageConstPtr& msg)
	{
		while(sem); sem=true;
		
		// read the input image 
		cv_bridge::CvImagePtr cv_ptr;
		try
		{
			cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
		}
		catch (cv_bridge::Exception& e)
		{
			ROS_ERROR("cv_bridge exception: %s", e.what());
			return;
		}
		inImage = cv_ptr->image;
		
		// detect the markers
		ROS_INFO("detecting markers");
		markers.clear();
		mDetector.detect(inImage, markers, camParam, marker_size, false);
		
		sem=false;
	}
	
	/** get the IDs identified by aruco */
	bool get_ids(erl_assignment_3_msgs::GetArucoIds::Request  &req, erl_assignment_3_msgs::GetArucoIds::Response &res) 
	{
		while(sem); sem=true;
		
		res.isEmpty = detected_ids.empty();
		res.ids = detected_ids;
		
		ROS_INFO_STREAM("Detected markers : " << markers.size());
		if(markers.size() > 0)
		{
			for(int i=0; i<markers.size(); ++i)
				ROS_INFO_STREAM("marker ID=" << markers[i].id);
		}
		
		sem=false;
		return true;
	}

private:
	
	/// class node handle
	ros::NodeHandle nh;
	/// the image transport handle
	image_transport::ImageTransport it;
	
	/// image transport subscriber from Gazebo
	image_transport::Subscriber image_sub;
	
	/// aruco detector handle
	aruco::MarkerDetector mDetector;
	
	/// last aruco markers detection
	std::vector<aruco::Marker> markers;
	
	/// camera parameters
	aruco::CameraParameters camParam;
	
	/// markers size
	double marker_size = 0.05;
	
	/// use camera infos
	bool useCamInfo = false;
	
	/// last received imade
	cv::Mat inImage;
	
	/// detected IDs
	std::vector<int> detected_ids;
	
	/// whether the subscriber is working or not
	bool sem;
	
	/// service aruco ids
	ros::ServiceServer srv_aruco_ids;
};


/** main function */
int main(int argc, char** argv)
{
	ros::init(argc, argv, "detectibot_magnifier");
	ros::AsyncSpinner spinner(3);
	spinner.start();
	
	detectibot_magnifier_class echo;
	echo.spin();
	
	return 0;
}

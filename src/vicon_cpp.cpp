#include <ros/ros.h>
#include <geometry_msgs/TransformStamped.h>
#include <cmath>
#include <iostream>

//Vicon data callback 
void getViconData(const geometry_msgs::TransformStamped::ConstPtr& data)
{
    double x = data->transform.translation.x;
    double y = data->transform.translation.y;
    double z = data->transform.translation.z;
    double rx = data->transform.rotation.x;
    double ry = data->transform.rotation.y;
    double rz = data->transform.rotation.z;
    double rw = data->transform.rotation.w;

    ROS_INFO("X: %lf \t Y: %lf \t Z: %lf \n RX: %lf \t RY: %lf \t RZ: %lf \t RW: %lf \n",x,y,z,rx,ry,rz,rw);
}

//Main function
int main(int argc, char* argv[])
{
    //Create node
    ros::init(argc,argv, "vicon_cpp");

    //Node handle to communicate with other nodes
    ros::NodeHandle n;

    //Vicon subscriber
    ros::Subscriber vicon_sub;

    //Subscribe to a topic 
    vicon_sub = n.subscribe("/vicon/Mambo_5/Mambo_5",100, getViconData);

    //Setting a sampling rate
    ros::Rate r(100);

    //Loop
    while(n.ok())
    {
        ros::spinOnce();
        r.sleep();
    }
    
    return 0;
}

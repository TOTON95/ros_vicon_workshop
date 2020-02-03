#!/usr/bin/env python3.6
import rospy
from std_msgs.msg import Empty, String, UInt8
from sensor_msgs.msg import Joy
from geometry_msgs.msg import TransformStamped


# Vicon callback
def cb_vicon_data(data):
    rospy.loginfo(rospy.get_name() + "\nX: %s \tY: %s \tZ: %s \nRX: %s \tRY: %s \tRZ: %s \nRW: %s",data.transform.translation.x, data.transform.translation.y, data.transform.translation.z, data.transform.rotation.x, data.transform.rotation.y, data.transform.rotation.z, data.transform.rotation.w)

# ROS node
def vicon_sys():

    # Init ROS node
    rospy.init_node('vicon_reader', anonymous=True)

    # Setting node's rate
    rate = rospy.Rate(100)

    # Choose which topic to listen
    s_vicon = rospy.Subscriber('/vicon/Mambo_5/Mambo_5', TransformStamped, cb_vicon_data)

    # Main loop
    while not rospy.is_shutdown():
        rate.sleep()


# Main function
if __name__ == '__main__':
    try:
        vicon_sys()
    except rospy.ROSInterruptException:
        print("Exiting...")

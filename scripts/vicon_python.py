#!/usr/bin/env python3.6
import rospy
from std_msgs.msg import Empty, String, UInt8
from sensor_msgs.msg import Joy
from geometry_msgs.msg import TransformStamped


# Vicon callback
def cb_vicon_data(data):
    x = data.transform.translation.x
    y = data.transform.translation.y
    z = data.transform.translation.z
    rx = data.transform.rotation.x
    ry = data.transform.rotation.y
    rz = data.transform.rotation.z
    rw = data.transform.rotation.w

    rospy.loginfo(rospy.get_name() + "\nX: %s\tY: %s\tZ: %s\nRX: %s\tRY: %s\tRZ: %s\nRW: %s",x, y, z, rx, ry, rz, rw)

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

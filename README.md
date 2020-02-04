# ros_vicon_workshop
Basic Vicon-ROS tutorial (Python/C++)

## Installation

```sh
$ mkdir catkin_vicon
$ cd catkin_vicon
$ mkdir src
$ cd src
$ git clone https://github.com/ethz-asl/vicon_bridge.git
$ git clone https://github.com/TOTON95/ros_vicon_workshop.git
$ cd ..
$ catkin_make
```

## Execution
```sh
$ source devel/setup.bash
```
### Python
```sh
$ rosrun vicon_workshop vicon_python.py
```

# ros_vicon_workshop

Basic Vicon-ROS tutorial (Python/C++)

![alt text](https://github.com/TOTON95/ros_vicon_workshop/blob/master/doc/overview.png "Vicon-ROS High Level Diagram")

## Dependencies

Install ROS using this link: [ROS official site](http://wiki.ros.org/melodic/Installation/Ubuntu)
```sh
$ sudo apt-get install python3-pip vim
$ sudo pip3 install rospkg
```

## Installation

```sh
$ mkdir catkin_vicon
$ cd catkin_vicon
$ mkdir src
$ cd src
$ git clone https://github.com/ethz-asl/vicon_bridge.git
$ git clone https://github.com/TOTON95/ros_vicon_workshop.git
$ cd ros_vicon_workshop
$ cd scripts
$ chmod +x vicon_python.py
$ cd ../../../
```
At `catkin_vicon` directory run:
```sh
$ catkin_make
```

## Configuration
```sh
$ rosed vicon_bridge vicon.launch 
```

Modify these lines with the IP address of the vicon machine (PC with Vicon tracker):

`<param name="datastream_hostport" value="YOUR_IP_HERE" type="str" />`

And comment this line (enclose it with `<!--- and -->`:

`<!--param name="datastream_hostport" value="vicon:801" type="str" /-->`


## Execution
In one terminal type the following (with `catkin_vicon` as root directory):
```sh
$ source devel/setup.bash
$ roslaunch vicon_bridge vicon.launch
```
In another terminal type (with `catkin_vicon` as root directory):
```sh
$ source devel/setup.bash
```
#### Python
```sh
$ rosrun vicon_workshop vicon_python.py
```

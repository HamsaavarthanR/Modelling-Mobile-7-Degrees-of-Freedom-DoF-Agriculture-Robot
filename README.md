# Modelling Mobile 7 Degrees of Freedom (DoF) Agriculture Robot

![Result GIF](https://github.com/user-attachments/assets/21ce2a4c-a946-4c47-82bc-37d4076a3e7c)
* Custom build your own Robotic arm 7DoF mounted on a Truck model using Solidworks CAD Software
* Attach frames and collisions for URDF compatibility
* Simulate using ROS2, Gazebo
* Deploy RWD motion control, sensors and vacum gripper
* Create environment with trees and apples gazebo model
* Perform motion control and pick apples from tree model

## Accomplishments
* Assisted in the design and construction of a mobile truck and harvester-arm system with 7 DoF using SolidWorks (CAD), compatible to simulate using ROS2 and Gazebo, capable of automated traversal and fruit harvesting using vacuum gripper.
* Executed accurate mathematical modelling to the robotic arm’s kinetics and dynamics, acquiring 100% virtually simulable model by analyzing Denavit-Hartenberg parameters, enhancing simulation performance.

## Contributors
* Hamsaavarthan Ravichandar
* Robens Midy Cyprien
* Kent-Diens Joseph
* Jonathan Leonard Crespo

## About Robot
The robot consistS of a truck, a robot arm with 4 revolute joints, and a vacuum gripper as the end effector.The truck has two front wheels, each with independent steering, that are passive, and two rear wheels that are powered.The main application of this robot will be to autonomously move to apple trees and use the robot arm vacuum gripper to harvest apples and placed them into a container in the bed of the truck.The truck and robot arm assembly overall has 7 degrees of freedom:
* 1 DOF for the rear-wheels, since they are connected by a one drive shaft.
* 2 DOF (1 for each wheel) for the two front wheels since they have independent steering.
* 4 DOF
 for the robot arm, since it has four revolute joints.

## DH Parameters and DH Table
<img width="543" alt="Screenshot 2025-04-15 at 7 14 35 PM" src="https://github.com/user-attachments/assets/96ff9679-b75b-4c68-b9be-03752f404586" />

<img width="893" alt="Screenshot 2025-04-15 at 7 13 15 PM" src="https://github.com/user-attachments/assets/ced556ed-83fe-4df5-8e03-bae4aa9b1a9f" />

## Gazebo and RViz Visualisation
### Gazebo
* We created two worlds to demonstrate our robot’s abilities in gazebo. Our first world consists of trees with apples attached to them. This allows us to demonstrate both motion and manipulation since we have to first navigate to the tree, then manipulate the robot arm to extract the apples.
* Our second world had three apples on a flat surface. This allowed us to further demonstrate manipulation by having apples that we can pick and drop in our basket using limited motion.

### RViz
<img width="861" alt="Screenshot 2025-04-15 at 7 17 16 PM" src="https://github.com/user-attachments/assets/c35e8e4a-ecd0-4d54-ae33-4170ee3fd841" />


## System Requirements
* Ubuntu 20.04
* Python >= 3.8
* sympy
* ROS2 galatic
* Gazebo
* RVIZ2

## Genral Setup
-Verify you have ROS2 galatic distribution installed and also CMAKE necessary installations. Refer to: https://docs.ros.org/en/galactic/Installation/Ubuntu-Install-Debians.html
On command line run:
```sh
echo $ROS_DISTRO
```
-Install previously the following packages and any additional in your linux distribution running on the terminal the command:
```sh 
sudo apt install python3-colcon-common-extensions
```
-Install all necessary dependencies and libraries with pip for insrtance. Recommended to run in your own python environment.

## Steps to build and run project.

### Install python packages 

In case of missing libraries you can use pip to install them:
```sh
pip install NAME_OF_LIBRARY
pip install 
pip install numpy
pip install matplotlib
```

### Create the workspace and install all dependencies priorly
Create a folder in your system and locate the src pkg
```sh
  mkdir -p ~/test_ws/src
  cd ~/test_ws/src
```
Clone the repository package inside this folder

```sh
   git clone https://github.com/HamsaavarthanR/Modelling_Mobile_7DoF_Agriculture_Robot.git
```

You should get a folder called **Modelling_Mobile_7DoF_Agriculture_Robot** with the content of the repository inside. It should be like the following example:

Downlod all the dependencies before runnning a build.
```sh
rosdep install -i --from-path src --rosdistro galactic -y
```
Run this command to be at root of your workspace (~/test_ws) and build your workspace
```sh
cd ../
colcon build 
```

In case you got an error while building regarding an include folder not found run this command while being in the workspace folder


```sh
mkdir -p ~/src/Modelling_Mobile_7DoF_Agriculture_Robot/include/Modelling_Mobile_7DoF_Agriculture_Robot
```
And run again the build command

```sh
colcon build --packages-select Modelling_Mobile_7DoF_Agriculture_Robot
```

Source ROS (Package will be identified) However you can do make this default when opening the terminal by modifying the .bashrc file. <ins>Don't forget your user password to give permissions </ins>
```sh
sudo nano ~/.bashrc
```

```sh
 source /opt/ros/galactic/setup.bash
```
**Source package to be identified**. Do this for every new terminal you open locating the Workspace folder:

```sh
source install/setup.bash
```

Before launch also run the following commands to install the controller dependencies:

```sh
sudo apt install ros-galactic-ros2-control ros-galactic-ros2-controllers ros-galactic-gazebo-ros2-control
sudo apt-get install ros-galactic-controller-manager
```
## Download all the additionals

### Add the odometry package

Odometry package is needed to track robot position and orientation as it contains plugin features. Vacuum gripper package is also necessary to be able to catch apples in gazebo.

To add it go to the folder **additionals** inside the package folder **Modelling_Mobile_7DoF_Agriculture_Robot** and copy the folder **odometry** to the src folder of your workspace. Final result should look like this 


You could confirm it was sucessfully done by running a general command **colcon build** and giving no errors .
```sh
colcon build 
```


### Add gazebo models
To run the world successfully custom objects of tree and apples need to be downloaded. 

To add it go to the folder **additionals** inside the package folder **Modelling_Mobile_7DoF_Agriculture_Robot** and copy the folders **app_body** and **tree_body** to the location of your gazebo


### Gazebo

Run the following command at the root of your workspace once you source it 

```sh
ros2 launch Modelling_Mobile_7DoF_Agriculture_Robot gazebo.launch.py
```

This will display the robot in the world with apples and trees ready to run after the autonomous mode script.
Sometimes at first could not due to bugs with controller manager. Open a new terminal , locate the workspace folder and run again the command.

![image](https://github.com/user-attachments/assets/7baf4d11-24e4-435e-8eb3-6b82331bdd5e)


### RVIZ

To launch rviz open a new terminal, source the package and run: 

```sh
ros2 launch Modelling_Mobile_7DoF_Agriculture_Robot display.launch.py
```


Use the joint state publisher provided to try some poses for the arm for example

![image](https://github.com/user-attachments/assets/59c9436d-1387-49dc-9515-44cbf95966de)

To visualize lidar scanner run before in other terminal the gazebo simulation and after launch RVIZ again and use the **Add** button and look for select the **laser scanner** plugin 


After check for the scan topic and it should be visible the lidar.

![image](https://github.com/user-attachments/assets/455e6d84-c6d9-4ba6-b621-6748abbc29ff)

As an extra step be sure inside the topic opetions, the Reliability Policy is set as **Best Effort**

![image](https://github.com/user-attachments/assets/dbe71e73-730e-4d4b-b87e-acc7cd1fd40d)


## Running scripts 

Inside the src folder of the package, these are the following scripts you can execute:


### Forward and inverse kinematics 

Locate the folder where the scripts are is:

```sh
cd ~\src\Modelling_Mobile_7DoF_Agriculture_Robot\src
```
Run the corresponding script:
```sh
python3 forward_position_kinematics_validation.py
```
This script will ask for the user to provide joint angles to give a final end effector matrix. This applies only for the robot arm.

Aditionally there is a matlab script (test_robot.m) using peter corke robotics toolbox for visualize the robot and interact with it.

![Screenshot 2024-12-05 140523](https://github.com/user-attachments/assets/1e3bff87-50c1-4728-b05e-63e8205146e8)

```sh
python3 Inverse_kinematics_and_validation.py
```
This script simulates the end effector of the robot drawing a circle f radius 2 inches. The plotted circle on the YZ - plane.

### Doing the grasping task

Be sure to open the gazebo by following the previous steps to open it. 

Open a new terminal,source the package and run:

```sh 
ros2 run Modelling_Mobile_7DoF_Agriculture_Robot truck_and_arm_autonomous_control.py
```

The agricultural robot will spawn from position [0.0, 0.25, 0.05] and move from its origin near the trees to catch the apples attached to them with its robot arm.

![image](https://github.com/user-attachments/assets/031c92bd-e54f-4a63-bfcd-4dc81da03476)

### Teleoperation:

Close any previously running gazebo terminals then

Build and source Modelling_Mobile_7DoF_Agriculture_Robot then launch gazebo with the command:

```sh
  colcon build --packages-select Modelling_Mobile_7DoF_Agriculture_Robot
```

```sh
  ros2 launch Modelling_Mobile_7DoF_Agriculture_Robot gazebo.launch.py
```
Open a new terminal and run:

```sh
  ros2 run Modelling_Mobile_7DoF_Agriculture_Robot teleop.py
```

Robot can now be controlled with W, A, S, D with W and S increasing and decreasing velocity 
respectively and A and D turning the wheel left and right respectively. 

For moving the arm using numbers key combinations of 
- Keys arm1: 1,5
- Keys arm2: 2,6 
- Keys arm3: 3,7 
- Keys arm4: 4,8 

### Check the odom topic
Open a new terminal,source package and run:

```sh 
ros2 run Modelling_Mobile_7DoF_Agriculture_Robot odom_subscriber.py
```
This will give information of the current position of the robot 

If odometry was settled correctly you can visualize it via the topic **/odom**, using programs as rqt_plot or plotjugger. For more information refer to the following useful link tutorial. All credits to the author https://www.youtube.com/watch?v=MnMGjvYxlUk
You can also run if installed
```sh 
ros2 run rqt_plot rqt_plot
```


## Links
### Apple picking 
https://drive.google.com/file/d/1SpIkOwTCYOupz2PXvUdXQlMOrctiJor_/view?usp=sharing

### Teleoperation 
https://drive.google.com/file/d/1qeRTex9yS9QXii5R4m6H4I7smooFlUSS/view?usp=sharing

### RVIZ Visualisation
https://drive.google.com/file/d/1inNBQx7HXsHRcq14zKzZnVdNlXGsxYK8/view?usp=sharing

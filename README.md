# Modelling Mobile 7 Degrees of Freedom (DoF) Agriculture Robot

* Custom build your own Robotic arm 7DoF mounted on a Truck model using Solidworks CAD Software
* Attach frames and collisions for URDF compatibility
* Simulate using ROS2, Gazebo
* Deploy RWD motion control, sensors and vacum gripper
* Create environment with trees and apples gazebo model
* Perform motion control and pick apples from tree model

## Accomplishments
* Assisted in the design and construction of a mobile truck and harvester-arm system with 7 DoF using SolidWorks (CAD), compatible to simulate using ROS2 and Gazebo, capable of automated traversal and fruit harvesting using vacuum gripper.
* Executed accurate mathematical modelling to the robotic arm’s kinetics and dynamics, acquiring 100% virtually simulable model by analyzing Denavit-Hartenberg parameters, enhancing simulation performance.

## Contributors:
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


## Links

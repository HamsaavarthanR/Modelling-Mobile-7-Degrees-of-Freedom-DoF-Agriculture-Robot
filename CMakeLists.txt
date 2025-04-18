cmake_minimum_required(VERSION 3.8)
project(Modelling_Mobile_7DoF_Agriculture_Robot)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(xacro REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

install(DIRECTORY
urdf
meshes
launch
config
worlds
rviz
src
DESTINATION share/${PROJECT_NAME}/
)

install(
    DIRECTORY include/Modelling_Mobile_7DoF_Agriculture_Robot
    DESTINATION include
    )

install(
  PROGRAMS
  launch/robot_description_publisher.py
  src/teleop.py
  src/truck_and_arm_autonomous_control.py
  src/odom_subscriber.py
  DESTINATION lib/${PROJECT_NAME}
  )

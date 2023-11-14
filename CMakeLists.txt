cmake_minimum_required(VERSION 3.0.2)
cmake_policy(SET CMP0003 NEW)
cmake_policy(SET CMP0057 NEW)

project(irsl_sim_environments)

catkin_package()

install(DIRECTORY cnoid
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS
  )

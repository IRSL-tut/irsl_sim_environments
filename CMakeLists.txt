cmake_minimum_required(VERSION 3.0.2)
cmake_policy(SET CMP0003 NEW)
cmake_policy(SET CMP0057 NEW)

project(irsl_sim_environments)

find_package(ament_cmake REQUIRED)

ament_package()

install(DIRECTORY cnoid
  DESTINATION share/${PROJECT_NAME}
  USE_SOURCE_PERMISSIONS
  )

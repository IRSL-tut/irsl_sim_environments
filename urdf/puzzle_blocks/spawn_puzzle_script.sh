#!/bin/bash

_OFFSET=${OFFSET:-0.06}

_BASE_FIXED=${BASE_FIXED:-"yes"}
_SPAWN_TABLE=${SPAWN_TABLE:-""}

if [ "${_SPAWN_TABLE}" -n ]; then
    rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/puzzle_table.urdf \
           -model puzzle_table -x 0.24 -z 0.025
fi

if [ "${_BASE_FIXED}" == "yes" ]; then
    rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/puzzle_base_fixed.urdf \
           -model puzzle_base -x 0.2 -z "$(echo ${_OFFSET} + 0.0 | bc)"
else
    rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/puzzle_base.urdf \
           -model puzzle_base -x 0.2 -z "$(echo ${_OFFSET} + 0.0 | bc)"
fi

## # old settings
## rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/yellow_block/yellow_block.urdf \
##  -model yellow_block -x 0.27 -y 0.1 -z 0.046 -R 3.141592653589793 -P 1.2246467991473532e-16 -Y 3.141592653589793
## 
## rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/red_block/red_block.urdf \
##  -model red_block -x 0.4 -y 0.1 -z 0.016 -R 0.0 -P -0.0 -Y 0.0
## 
## rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/purple_block/purple_block.urdf \
##  -model purple_block -x 0.43 -y 0.0 -z 0.046 -R 3.141592653589793 -P 1.2246467991473532e-16 -Y 3.141592653589793
## 
## rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/lightgreen_block/lightgreen_block.urdf \
##  -model lightgreen_block -x 0.4 -y -0.1 -z 0.046 -R 3.141592653589793 -P 1.2246467991473532e-16 -Y 3.141592653589793
## 
## rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/green_block/green_block.urdf \
##  -model green_block -x 0.27 -y -0.13 -z 0.046 -R 3.141592653589793 -P 1.2246467991473532e-16 -Y 3.141592653589793
## 
## rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/cyan_block/cyan_block.urdf \
##  -model cyan_block -x 0.32999999999999996 -y 0.2 -z 0.046 -R 3.141592653589793 -P 1.2246467991473532e-16 -Y 3.141592653589793
## 
## rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/brown_block/brown_block.urdf \
##  -model brown_block -x 0.32999999999999996 -y -0.2 -z 0.016 -R 0.0 -P -0.0 -Y 0.0

rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/brown_block/brown_block.urdf \
 -model brown_block -x 0.23 -y -0.2 -z "$(echo ${_OFFSET} + 0.016 | bc)" -R 0.0 -P -0.0 -Y 0.0

rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/cyan_block/cyan_block.urdf \
 -model cyan_block -x 0.17 -y -0.13 -z "$(echo ${_OFFSET} + 0.016 | bc)" -R 0.0 -P -1.5707963267948963 -Y 0.0

rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/green_block/green_block.urdf \
 -model green_block -x 0.23 -y 0.2 -z "$(echo ${_OFFSET} + 0.016 | bc)" -R 0.0 -P 0.0 -Y -1.5707963267948963

rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/lightgreen_block/lightgreen_block.urdf \
 -model lightgreen_block -x 0.33 -y 0.13 -z "$(echo ${_OFFSET} + 0.016 | bc)" -R 1.5707963267948963 -P 1.5707963267948963 -Y 0.0

rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/purple_block/purple_block.urdf \
 -model purple_block -x 0.33 -y 0.0 -z "$(echo ${_OFFSET} + 0.046 | bc)" -R 3.141592653589793 -P 0.0 -Y 1.5707963267948968

rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/red_block/red_block.urdf \
 -model red_block -x 0.17 -y 0.13 -z "$(echo ${_OFFSET} + 0.016 | bc)" -R 1.5707963267948963 -P -1.5707963267948963 -Y 0.0

rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/yellow_block/yellow_block.urdf \
 -model yellow_block -x 0.30 -y -0.1 -z "$(echo ${_OFFSET} + 0.016 | bc)" -R 1.5707963267948963 -P 0.0 -Y 1.5707963267948963

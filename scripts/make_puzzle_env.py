###
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

## lst = (
##   { "pos": [-0.03,  0.1,  0.046], "aa": [0, 1, 0, 3.141592653589793], "name": 'yellow' },
##   { "pos": [ 0.1,   0.1,  0.016], "name": 'red' },
##   { "pos": [ 0.13,  0.0,  0.046], "aa": [0, 1, 0, 3.141592653589793], "name": 'purple' },
##   { "pos": [ 0.1,  -0.1,  0.046], "aa": [0, 1, 0, 3.141592653589793], "name": 'lightgreen' },
##   { "pos": [-0.03, -0.13, 0.046], "aa": [0, 1, 0, 3.141592653589793], "name": 'green' },
##   { "pos": [ 0.03,  0.2,  0.046], "aa": [0, 1, 0, 3.141592653589793], "name": 'cyan'  },
##   { "pos": [ 0.03, -0.2,  0.016], "name": 'brown' }
##   )
## offset=coordinates(npa([0.3, 0, 0]))
## 
## ## spawn urdf
## for l in lst:
##   name = l['name']
##   cds = ru.make_coordinates(l)
##   cds.transform(offset, coordinates.wrt.world)
##   pos = cds.pos; RPY = cds.getRPY()
##   xx = pos[0]; yy = pos[1]; zz = pos[2]
##   RR = RPY[0]; PP = RPY[1]; YY = RPY[2]
##   print('rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/{}_block/{}_block.urdf \\\n -model {}_block -x {} -y {} -z {} -R {} -P {} -Y {}'.format(name, name, name, xx, yy, zz, RR, PP, YY))

##
from irsl_choreonoid_ros.setup_cnoid import SetupCnoid
SetupCnoid.setEnvironmentFromYaml('package://irsl_sim_environments/cnoid/world/puzzle_blocks.yaml')

offset=coordinates(npa([0.3, 0, 0]))

itm=cbase.RootItem.instance.childItem
while itm is not None:
    #print(itm.name)
    if '_block' in itm.name:
        name = itm.name[:-6]
        cds=coordinates(itm.body.rootLink.T)
        cds.transform(offset, coordinates.wrt.world)
        pos = cds.pos; RPY = cds.getRPY()
        xx = pos[0]; yy = pos[1]; zz = pos[2]
        RR = RPY[0]; PP = RPY[1]; YY = RPY[2]
        print('rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/{}_block/{}_block.urdf \\\n -model {}_block -x {} -y {} -z {} -R {} -P {} -Y {}'.format(name, name, name, xx, yy, zz, RR, PP, YY))
    itm = itm.nextItem

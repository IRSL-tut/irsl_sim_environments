exec(open('puzzle_blocks_functions.py').read())
import os

CUBE_SIZE = 0.03
CUBE_C_SIZE=0.001
_meshprefix='package://irsl_sim_environments/urdf/puzzle_blocks/'
_URDF=False
_outputdir='/tmp/cnoid/'
#_URDF=True
#_outputdir='/tmp/urdf/'

# makeConnectedCubesScen( ((0, 0, 0), (0, 0, 1), (0, 1, 1), (0, 2, 1)), yellow_color)
settings=((0, 0, 0), (0, 0, 1), (0, 1, 1), (0, 2, 1))
name='yellow_block'
_col=yellow_color
os.makedirs('{}{}/'.format(_outputdir, name), exist_ok=True)
createCubes(name, settings, CUBE_SIZE, CUBE_C_SIZE, color=_col, dirname='{}{}/'.format(_outputdir, name),
            URDF=_URDF, meshURLPrefix='{}{}/'.format(_meshprefix, name))

# makeConnectedCubesScen( ((0, 0, 0), (0, -1, 1), (0,  0, 1), (0, 1, 1)), light_blue_color)
settings=((0, 0, 0), (0, -1, 1), (0,  0, 1), (0, 1, 1))
name='cyan_block'
_col=light_blue_color
os.makedirs('{}{}/'.format(_outputdir, name), exist_ok=True)
createCubes(name, settings, CUBE_SIZE, CUBE_C_SIZE, color=_col, dirname='{}{}/'.format(_outputdir, name),
            URDF=_URDF, meshURLPrefix='{}{}/'.format(_meshprefix, name))

# makeConnectedCubesScen( ((0, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 1)), red_color)
settings=((0, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 1))
name='red_block'
_col=red_color
os.makedirs('{}{}/'.format(_outputdir, name), exist_ok=True)
createCubes(name, settings, CUBE_SIZE, CUBE_C_SIZE, color=_col, dirname='{}{}/'.format(_outputdir, name),
            URDF=_URDF, meshURLPrefix='{}{}/'.format(_meshprefix, name))

# makeConnectedCubesScen( ((0, 0, 0), (1, 0, 1), (0, 0, 1), (0, 1, 1)),  green_color)
settings=((0, 0, 0), (1, 0, 1), (0, 0, 1), (0, 1, 1))
name='green_block'
_col=green_color
os.makedirs('{}{}/'.format(_outputdir, name), exist_ok=True)
createCubes(name, settings, CUBE_SIZE, CUBE_C_SIZE, color=_col, dirname='{}{}/'.format(_outputdir, name),
            URDF=_URDF, meshURLPrefix='{}{}/'.format(_meshprefix, name))

# makeConnectedCubesScen( ((0, 0, 0), (1, 0, 0), (0, 0, 1), (1, 0, 1)), black_bean_color)
settings=((0, 0, 0), (1, 0, 0), (0, 0, 1), (1, 0, 1))
name='brown_block'
_col=black_bean_color
os.makedirs('{}{}/'.format(_outputdir, name), exist_ok=True)
createCubes(name, settings, CUBE_SIZE, CUBE_C_SIZE, color=_col, dirname='{}{}/'.format(_outputdir, name),
            URDF=_URDF, meshURLPrefix='{}{}/'.format(_meshprefix, name))

# makeConnectedCubesScen( ((0, 0, 0), (0, 0, 1), (1, 0, 1), (1, -1, 1)), african_violet_color)
settings=((0, 0, 0), (0, 0, 1), (1, 0, 1), (1, -1, 1))
name='purple_block'
_col=african_violet_color
os.makedirs('{}{}/'.format(_outputdir, name), exist_ok=True)
createCubes(name, settings, CUBE_SIZE, CUBE_C_SIZE, color=_col, dirname='{}{}/'.format(_outputdir, name),
            URDF=_URDF, meshURLPrefix='{}{}/'.format(_meshprefix, name))

# makeConnectedCubesScen( ((0, 0, 0), (0, 0, 1), (0, -1, 1)), bright_green_color)
settings=((0, 0, 0), (0, 0, 1), (0, -1, 1))
name='lightgreen_block'
_col=bright_green_color
os.makedirs('{}{}/'.format(_outputdir, name), exist_ok=True)
createCubes(name, settings, CUBE_SIZE, CUBE_C_SIZE, color=_col, dirname='{}{}/'.format(_outputdir, name),
            URDF=_URDF, meshURLPrefix='{}{}/'.format(_meshprefix, name))

### base
offset=CUBE_SIZE*0.05
plate_t=CUBE_SIZE*0.2
wood_col=(0.93, 0.86, 0.71)##
rb=RobotBuilder()
rb.makeBox(offset + CUBE_SIZE*3, offset + CUBE_SIZE*3, plate_t, color=wood_col).translate(npa([0, 0, plate_t * 0.5]))
rb.makeBox(offset + CUBE_SIZE*3, plate_t*2, plate_t*2, color=wood_col).translate(npa([0,  plate_t + (offset + CUBE_SIZE*3)*0.5, plate_t]))
rb.makeBox(offset + CUBE_SIZE*3, plate_t*2, plate_t*2, color=wood_col).translate(npa([0, -plate_t - (offset + CUBE_SIZE*3)*0.5, plate_t]))
rb.makeBox(plate_t*2, offset + CUBE_SIZE*3 + plate_t*4, plate_t*2, color=wood_col).translate(npa([ plate_t + (offset + CUBE_SIZE*3)*0.5, 0, plate_t]))
rb.makeBox(plate_t*2, offset + CUBE_SIZE*3 + plate_t*4, plate_t*2, color=wood_col).translate(npa([-plate_t - (offset + CUBE_SIZE*3)*0.5, 0, plate_t]))
lcur=rb.createLinkFromShape(name='base_link', root=True, density=200)
if _URDF:
    rb.exportURDF('{}puzzle_base.urdf'.format(_outputdir), RobotName='puzzle_base', UseURDFPrimitiveGeometry=True, UseXacro=False, MeshURLPrefix='')
else:
    rb.exportBody('{}puzzle_base.body'.format(_outputdir), modelName='puzzle_base')

import cnoid.CGALUtil as cgal
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

light_blue_color = (173/255, 216/255, 230/255)
yellow_color = (1,1,0)
red_color    = (1,0,0)
green_color  = (0, 66/255, 37/255)
black_bean_color = (61/255, 12/255, 2/255)
african_violet_color = (178/255, 132/255, 190/255)
bright_green_color = (102/255, 255/255, 0)

def makeOnEdgeTetra(from_pt, to_pt, cube_size, c_size):
    zz = to_pt - from_pt
    zz = zz/np.linalg.norm(zz)
    yy = to_pt + from_pt
    yy = yy/np.linalg.norm(yy)
    mat = np.column_stack([np.cross(yy, zz), yy, zz])
    cds=coordinates(from_pt, mat)
    #cc=mkshapes.makeTetrahedron(cube_c_size*5, cube_c_size*5, cube_size*2, center_x=cube_c_size*2.5, center_y=0.0, coords=cds)
    cc=cgal.makeTetrahedron(c_size*5, c_size*5, cube_size*2, center_x=c_size*2.5, center_y=0.0, coords=cds)
    cc.translate(npa([0, 0, -cube_size*0.05]))
    cc.translate(npa([-c_size*2.5, 0, 0]))
    cc.translate(npa([0, -c_size*0.5, 0]))
    return cc

def makeCubeWithC(cube_size, horizontal_c_size=None, vertical_c_size=None, color=None, horizontalEdge=True, verticalEdge=False):
    if horizontal_c_size is None:
        horiaontal_c_size = 0.02 * cube_size
    if vertical_c_size is None:
        vertical_c_size = 0.02 * cube_size
    res = cgal.makeBox(cube_size, color=color)
    #res = [ cgal.makeBox(cube_size, color=color) ]
    size_2 = cube_size*0.5
    lst=((1, 1), (-1, 1), (-1, -1), (1, -1))
    if horizontalEdge:
        for l in range(len(lst)):
            from_pt = npa([lst[l-1][0]*size_2, lst[l-1][1]*size_2, size_2])
            to_pt   = npa([lst[l  ][0]*size_2, lst[l  ][1]*size_2, size_2])
            obj=makeOnEdgeTetra(from_pt, to_pt, cube_size, horizontal_c_size)
            cgal.booleanDifference(res, obj)
            #res.append(obj)
        for l in range(len(lst)):
            from_pt = npa([lst[l-1][0]*size_2, lst[l-1][1]*size_2, -size_2])
            to_pt   = npa([lst[l  ][0]*size_2, lst[l  ][1]*size_2, -size_2])
            obj=makeOnEdgeTetra(from_pt, to_pt, cube_size, horizontal_c_size)
            cgal.booleanDifference(res, obj)
            #res.append(obj)
    if verticalEdge:
        for l in range(len(lst)):
            from_pt = npa([lst[l][0]*size_2, lst[l][1]*size_2, -size_2])
            to_pt   = npa([lst[l][0]*size_2, lst[l][1]*size_2,  size_2])
            obj=makeOnEdgeTetra(from_pt, to_pt, cube_size, vertical_c_size)
            cgal.booleanDifference(res, obj)
            #res.append(obj)
    return res

def makeConnectedCubes(lst, color, cube_size=1.0, cube_c_size=0.04):
    res = []
    for l in lst:
        obj = makeCubeWithC(cube_size, cube_c_size, color=color)
        obj.translate( cube_size * npa(l) )
        res.append(obj)
    return res

def makeConnectedCubesScen(lst, fname, color=None, cube_size=1.0, uri=None):
    res = []
    if uri is None:
        uri = fname
    for l in lst:
        obj = mkshapes.loadScene(fname, fileUri=uri, color=color)
        obj.translate( cube_size * npa(l) )
        res.append(obj)
    return res

def makeConnectedCubesPrimitive(lst, color=None, cube_size=1.0):
    res = []
    for l in lst:
        obj = mkshapes.makeBox(cube_size, color=color)
        obj.translate( cube_size * npa(l) )
        res.append(obj)
    return res

#settings=((0, 0, 0), (0, -1, 0), (0,  0, 1), (0, 1, 1))
def createCubes(name, settings, size, c_size, color=None, dirname='', mode=2, URDF=False, meshURLPrefix=''):
    obj = makeCubeWithC(size, horizontal_c_size=c_size, vertical_c_size=c_size,
                        horizontalEdge=True, verticalEdge=True)
    fname = '{}cube_with_c.scen'.format(dirname)
    mkshapes.exportScene(fname, obj.target, exportMesh=True)
    vis = makeConnectedCubesScen(settings, fname, color=color, cube_size=size)
    col = makeConnectedCubesPrimitive(settings, cube_size=size)
    # Builder
    rb=RobotBuilder()
    # visual
    rb.addShapes(vis)
    # collision
    gcol = cutil.SgGroup()
    for c in col:
        gcol.addChild(c.target)
    ### for zero division / calc mass from collision
    lcur=rb.createLinkFromShape(name='base_link', root=True, density=200, collision=gcol, useCollisionForMassparam=True)
    if URDF:
        urdffname='{}{}.urdf'.format(dirname, name)
        rb.exportURDF(urdffname, RobotName=name, UseURDFPrimitiveGeometry=True, UseXacro=False, MeshURLPrefix=meshURLPrefix, MeshFilePrefix=dirname)
    else:
        bodyfname='{}{}.body'.format(dirname, name)
        rb.exportBody(bodyfname, mode=mode, modelName=name)

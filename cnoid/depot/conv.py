exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())
ret = mkshapes.loadMesh('meshes/Depot.dae', rawShape=True)
#wt = cutil.StdSceneWriter()
#wt.writeScene('/tmp/files/depot/depot.scen', ret)
mkshapes.exportScene('/tmp/files/depot/depot.scen', ret)
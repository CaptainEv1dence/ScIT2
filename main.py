import gmsh
import sys

gmsh.initialize()

gmsh.model.add("t2")

lc = 1e-1
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(0, 1, 0, lc, 3)
gmsh.model.geo.addPoint(0, 0, 1, lc, 4)
gmsh.model.geo.addPoint(1, 1, 0, lc, 5)
gmsh.model.geo.addPoint(0, 1, 1, lc, 6)
gmsh.model.geo.addPoint(1, 0, 1, lc, 7)
gmsh.model.geo.addPoint(1, 1, 1, lc, 8)


for i in range(3):
    gmsh.model.geo.addLine(1, i + 1, i)
for i in range(3):
    gmsh.model.geo.addLine(8, 8-i, 12-i)
for i in range(3):
    gmsh.model.geo.addLine(i + 1, i + 4, i + 3)


gmsh.model.geo.addLine(2, 7, 7)
gmsh.model.geo.addLine(3, 5, 8)
gmsh.model.geo.addLine(4, 6, 9)


gmsh.model.geo.addCurveLoop([1, 4, -8, -2], 1)
gmsh.model.geo.addPlaneSurface([1], 1)

gmsh.model.geo.addCurveLoop([2, 5, -9, -3], 2)
gmsh.model.geo.addPlaneSurface([2], 2)

gmsh.model.geo.addCurveLoop([1, 7, -6, -3], 3)
gmsh.model.geo.addPlaneSurface([3], 3)


gmsh.model.geo.addCurveLoop([1, 4, -8, -2], 4)
gmsh.model.geo.addPlaneSurface([1], 1)

gmsh.model.geo.addCurveLoop([2, 5, -9, -3], 5)
gmsh.model.geo.addPlaneSurface([2], 2)

gmsh.model.geo.addCurveLoop([1, 7, -6, -3], 6)
gmsh.model.geo.addPlaneSurface([3], 3)



l = gmsh.model.geo.addSurfaceLoop([i + 1 for i in range(4)])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)

gmsh.write("t2.msh")
gmsh.write("t2.geo_unrolled")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
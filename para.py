import math

ngrid = 80
pi = 4.0*math.atan(1.0)
# All in Bohr units
k = 1.24
xmin, ymin, zmin =-7.0,-7.0,-7.0
xmax, ymax, zmax = 7.0, 7.0, 7.0
dq = (xmax-xmin)/float(ngrid-1)

import math
import numpy as np
import para
import orb
import cube

def main():
    filename = "H2plus.xyz"
    Nxyz = []
    sigma_1s = {}
    xyz = open(filename)
    natoms = int(xyz.readline())#Reading the xyz file
    title = xyz.readline()
    c = 0
    for line in xyz:
        x,y,z = line.split()        
        Nxyz.append([float(x), float(y), float(z)])
        c += 1
        if c == natoms: #Only up to the last line of the file
            break
    xyz.close()
    ndim = np.shape(Nxyz)[1]

    sigma_1s = orb.compute_orbital (Nxyz,natoms,ndim)

    cube.print_orbital (para.ngrid,para.ngrid,para.ngrid,sigma_1s,para.xmin,para.ymin,para.zmin,Nxyz)

main()


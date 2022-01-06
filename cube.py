import math
import numpy as np
import para
import orb

def print_orbital(N1,N2,N3,psi,xo,yo,zo,Nxyz):
    file1 = open ("H2+.cube","w")

    file1.write ("Cube file for H2+ ion\n")
    file1.write ("Bonding molecular orbital\n")
    file1.write ("%5d%16.6f%16.6f%16.6f\n"%(np.shape(Nxyz)[0],xo,yo,zo))
    file1.write ("%5d%16.6f%16.6f%16.6f\n"%(para.ngrid,para.dq,0.0,0.0))
    file1.write ("%5d%16.6f%16.6f%16.6f\n"%(para.ngrid,0.0,para.dq,0.0))
    file1.write ("%5d%16.6f%16.6f%16.6f\n"%(para.ngrid,0.0,0.0,para.dq))
    file1.write ("%5d%16.6f%16.6f%16.6f%16.6f\n"%(1,1.0,Nxyz[0][0],Nxyz[0][1],Nxyz[0][2]))
    file1.write ("%5d%16.6f%16.6f%16.6f%16.6f\n"%(1,1.0,Nxyz[1][0],Nxyz[1][1],Nxyz[1][2]))

#   NVal is taken as 1 by default              
    for ic in range (1,N1+1):
        for jc in range (1,N2+1):
            for kc in range (1,N3+1):
                if kc%6!=0 and kc!=N3:
                    file1.write ("%13.5e"%(psi[ic,jc,kc]))
                else:
                    file1.write ("%13.5e\n"%(psi[ic,jc,kc]))
    file1.close()


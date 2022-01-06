import math
import numpy as np
import para

def evaluate_sab (Rnuc):    
    S = math.exp(-para.k*Rnuc)*(1.0 + para.k*Rnuc + (1.0/3.0)*(para.k*Rnuc)**2)
    return S

def evaluate_1s (r):
    orb_s = para.k**(3/2)*math.sqrt(para.pi)*math.exp(-para.k*r)
    return orb_s

def compute_orbital (Nxyz,natoms,ndim):
    sigma_1s = {}
    x = para.xmin
    for ic in range (1,para.ngrid+1):
        y = para.ymin
        for jc in range (1,para.ngrid+1):
            z = para.zmin
            for kc in range (1,para.ngrid+1):
                
                Rnuc = [Nxyz[0][0]-Nxyz[1][0],Nxyz[0][1]-Nxyz[1][1],Nxyz[0][2]-Nxyz[1][2]]
                Rnuc = math.sqrt(np.dot(Rnuc,Rnuc))

                S = evaluate_sab (Rnuc)
                S = 1.0/math.sqrt(2.0*(1.0+S))

                ra = [x-Nxyz[0][0],y-Nxyz[0][1],z-Nxyz[0][2]]
                ra = math.sqrt(np.dot(ra,ra))
                rb = [x-Nxyz[1][0],y-Nxyz[1][1],z-Nxyz[1][2]]
                rb = math.sqrt(np.dot(rb,rb))

                orb_sa = evaluate_1s (ra)
                orb_sb = evaluate_1s (rb)

                sigma_1s[ic,jc,kc] = S*(orb_sa + orb_sb)
                z += para.dq
            y += para.dq
        x += para.dq

    return sigma_1s        

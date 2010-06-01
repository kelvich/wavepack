from scipy.special import sph_jn,sph_yn,lpn
from scipy.integrate import odeint
from numpy import *
from .. import ScatterData

class PhaseFunctions:
    """Implementation of phase functions method."""

    def __init__(self,potential,m,E):
        #natural units
        hbar_c = 197.32 # MeV*fm
        self.V = potential.coord
        self.a = potential.a
        self.m = m/hbar_c
        self.k0 = sqrt(2*self.m*E/hbar_c)
    
    def phase_eq(self,phase,r,l):
        ph = -2*self.m*self.k0*r**2*self.V(r)
        ph *= (cos(phase)*sph_jn(l,self.k0*r)[0][l]-sin(phase)*sph_yn(l,self.k0*r)[0][l])**2.0
        return (ph)

    def solve(self,moments):
        r = arange(0.00001, 5*self.a, 0.05)
        shifts=[]
        for l in range(moments):
            phase = odeint(self.phase_eq, 0, r, (l,))
            shifts.append(phase[-1])
        sd = ScatterData()
        sd.init_shifts(array(shifts),self.k0)
        return sd
    
    # def solve(self):
    #     shifts=self.phase_shifts(80)
    #     theta = arange(0, pi, 0.05)
    #     f_l = (exp(2j*shifts)-1)/(2j*self.k0)
    #     dcs=[]
    #     for t in theta:
    #         f=0.0
    #         for l in range(shifts.size):
    #             f = f + (2*l+1)*f_l[l]*lpn(l,cos(t))[0][l]
    #         dcs.append(abs(f)[0]**2)
    #     return ScatterData(theta,dcs)
    
    
    
    
    
    
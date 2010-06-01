from scipy.special import lpn
from numpy import *

class ScatterData:
    
    def __init__(self,theta=[]):
        self.theta = theta
        self.dcs = []
    
    def init_shifts(self,shifts,k0):
        self.shifts = shifts
        self.theta = arange(0, pi, 0.05)
        f_l = (exp(2j*shifts)-1)/(2j*k0)
        for t in self.theta:
            f=0.0
            for l in range(shifts.size):
                f = f + (2*l+1)*f_l[l]*lpn(l,cos(t))[0][l]
            self.dcs.append(abs(f)[0]**2)
        
    def init_phase(self,f):
        self.dcs = abs(f)**2    
    
    def get_dcs(self):
        return (self.theta, self.dcs)
    
    def print_dcs(self):
        for i in range(self.theta.size):
            print self.theta[i],self.dcs[i]

    # def log10_stdout(self):
    #     for i in range(self.theta.size):
    #         print self.theta[i],log10(self.dcs[i])
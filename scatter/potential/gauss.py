#from numpy import *
#from scipy.integrate import quad
from scipy.special import i0
from math import cos,sin,exp,pi

# hbar_c = 197.32 # MeV*fm
# a = 2.236 # fm
# A = -41.47/hbar_c # MeV
# 
# def coord(r):
#     return ( A*exp( -1*r**2/a**2 ) )
# 
# def momentum(self,k1,t1,k2,t2):
#     qq = lambda phi: k1**2 + k2**2 - 2*k1*k2*(cos(t2-t1) - 2*sin(t2)*sin(t1)*sin(phi)**2)
#     poten = lambda phi: exp( -1*a**2*qq(phi)/4.0 )
#     return A*a**3/(8*pi**1.5)*quad(poten,0,pi)[0]



class Gauss:
    """Gauss peak potential"""
    
    def __init__(self,a=2.236,A=-41.47):
        #natural units
        hbar_c = 197.32 # MeV*fm
        self.a = a # fm
        self.A = A/hbar_c # MeV
    
    def coord(self,r):
        return ( self.A*exp( -1*r**2/self.a**2 ) )
    
    def momentum(self,k1,t1,k2,t2):
        #qq = lambda phi: k1**2 + k2**2 - 2*k1*k2*(cos(t2-t1) - 2*sin(t2)*sin(t1)*sin(phi)**2)
        #poten = lambda phi: exp( -1*self.a**2*qq(phi/2.)/4. )
        #return self.A*self.a**3/(8*pi**1.5)*quad(poten,0,2*pi)[0]
        arg1 = -1*(k1**2 + k2**2 - 2*k1*k2*cos(t2)*cos(t1))*self.a/4.0
        arg2 = self.a**2*k1*k2*sin(t1)*sin(t2)
        return self.A*self.a**3/4*pi**0.5*exp( arg1 )*i0( arg2 )
        













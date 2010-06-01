from math import sqrt

class Particle:
    """Particle info"""
    
    def __init__(self,potential,m=1000.,E=5.):
        #natural units
        hbar_c = 197.32 # MeV*fm
        self.m = m/hbar_c
        self.E = E/hbar_c
        self.k0 = sqrt(2*self.m*self.E)



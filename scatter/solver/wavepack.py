from scipy.integrate import quad
from numpy import *
from .. import ScatterData

class WavePack:
    """Solve Lippmann-Schwinger equation in discrete basis."""
    
    def __init__(self,potential,m,E):
        #natural units
        hbar_c = 197.32 # MeV*fm
        self.potential = potential.momentum
        self.m = m/hbar_c
        self.E = E/hbar_c
        self.k0 = sqrt(2*self.m*self.E)

    def delta(self,i,j):
        return 1 if i==j else 0

    def banner(self,k_bins,k_max):
        hbar_c = 197.32 # MeV*fm
        print "Energy: ", self.E*hbar_c, 'MeV'
        print "Mass:   ", self.m*hbar_c, 'MeV'
        print "k0:     ", self.k0, 'fm'
        print "k_max:  ", k_max, 'fm'
        print "k_bins: ", k_bins
        #print "i_k0:   ", i_k0
    
    def solve(self,k_bins,t_bins,k_max):
        
        k0 = self.k0
        mesh_k = linspace(0.0000001,k_max,k_bins)
        mesh_t = linspace(0.0000001,pi,t_bins)
        k = zeros(mesh_k.size-1)
        t = zeros(mesh_t.size-1)
        
        for i in range(k.size):
            k[i] = mesh_k[i]+( mesh_k[i+1]-mesh_k[i] )/2.
            if (mesh_k[i] < k0) and (k0 <= mesh_k[i+1]):
                i_k0 = i
        for i in range(t.size):
            t[i] = mesh_t[i]+( mesh_t[i+1]-mesh_t[i] )/2.
        
        self.banner(k_bins,k_max)
        
        G = zeros(k.size*t.size,dtype=complex)
        for i in range(G.size):
            i_k = i/t.size
            i_t = i%t.size
            k2 = mesh_k[i_k+1]
            k1 = mesh_k[i_k]
            G[i] = (k2-k1)
            G[i] += (k0/2.)*log( abs(((k2+k0)*(k1-k0))/((k2-k0)*(k1+k0))) )
            G[i] += -1j*(k0/2.)*pi*self.delta(i_k0,i_k)
            G[i] *= ( -1*cos(mesh_t[i_t+1]) + cos(mesh_t[i_t]) )
        V0 = zeros(k.size*t.size,dtype=complex)
        for i in range(V0.size):
            i_k = i/t.size
            i_t = i%t.size
            V0[i] = self.potential(k[i_k],t[i_t],k0,0)/(2*pi)
        M = zeros([k.size*t.size,k.size*t.size],dtype=complex)
        for i in range(k.size*t.size):
            for j in range(k.size*t.size):
                i_k = i/t.size
                i_t = i%t.size
                j_k = j/t.size
                j_t = j%t.size
                M[i,j] = self.delta(i,j) - 2*self.m*self.potential( k[i_k],t[i_t],k[j_k],t[j_t] )*G[j]
            print i," of ",k.size*t.size
        
        self.T = linalg.solve(M,V0)
        self.t = t
        
        self.f = -1*self.m*(2*pi)**2*self.T[ t.size*(i_k0) : t.size*(i_k0+1) ]
        self.Born = -1*self.m*(2*pi)**2*V0[ t.size*(i_k0) : t.size*(i_k0+1) ]

        s = ScatterData(self.t)
        s.init_phase(self.f)
        return s
    


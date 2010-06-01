# 
# 
# class Lattice:
#     
#     def __init__(self,k_bins,t_bins,k_max):
#         self.mesh_k = linspace(0.0000001,k_max,k_bins)
#         self.mesh_t = linspace(0.0000001,pi,t_bins)
#         k = zeros(self.mesh_k.size-1)
#         t = zeros(self.mesh_t.size-1)
#     
#     def findSingular(self,k0):
#         for i in range(self.k.size):
#             self.k[i] = self.mesh_k[i]+( self.mesh_k[i+1]-self.mesh_k[i] )/2.
#             if (mesh_k[i] < k0) and (k0 <= mesh_k[i+1]):
#                 i_k0 = i
#         for i in range(self.t.size):
#             t[i] = mesh_t[i]+( mesh_t[i+1]-mesh_t[i] )/2.
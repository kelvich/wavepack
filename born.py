from matplotlib import pyplot
from numpy import *

E = 5. #MeV
m = 1000. #MeV
A = -41.47 #MeV
a = 2.24 #fm

hbar_c = 197
A = A/hbar_c
m = m/hbar_c
E = E/hbar_c
k0 = sqrt(2*m*E)

t = linspace(0,pi,40)
v = A*a**3/(8*pi**1.5)*exp( -( a*k0*sin(t/2) )**2 )
cs = (2*pi)**4/4.*(2*m)**2*abs(v)**2


print t
print cs

plt = pyplot
plt.plot(t,cs)
plt.show()







import scipy as sp
from scipy.integrate import odeint

#### unidades base
cm = 0.01
inch = 2.54*cm
g = 9.81 

#### coeficiente de arrastre 
p = 1.225
cd = 0.47
D = 8.5*inch
r = D/2
A = sp.pi * r**2
CD = 0.5*p*cd*A

m = 15. 

#### vientos
V1 = 0.
V2 = 10.0
V3 = 20.0
 
# funcion a integrar
# Z es el vector de estado
# z = [x,y,vx,vy]
# dz/dt = bala(z,t)   dz1/dt = z2
 
#         [z2      ]
# dz/dt = [        ]  (modelo)
#         [FD/m  -g]
 
#####vector de estado 
# Z[0]  -->  x
# Z[1]  -->  y
# Z[2]  -->  vx
# Z[3]  -->  vy

def bala(z,t):
    zp = sp.zeros(4)
    
    zp[0] = z[2]
    zp[1] = z[3]    
    v = z[2:4] #### saco los ultimos dos componentes
    v[0] = v[0] - V1    
    v2 = sp.dot(v,v)
    vnorm = sp.sqrt(v2)
    FD = -CD * v2 * (v / vnorm)    
    zp[2] = FD[0] / m
    zp[3] = FD[1] / m - g 
    
    return zp

def bala1(z,t):
    zp = sp.zeros(4)
    
    zp[0] = z[2]
    zp[1] = z[3]
    v = z[2:4] #### saco los ultimos dos componentes
    v[0] = v[0] - V2    
    v2 = sp.dot(v,v)
    vnorm = sp.sqrt(v2)
    FD = -CD * v2 * (v / vnorm)  
    zp[2] = FD[0] / m
    zp[3] = FD[1] / m - g 
    
    return zp

def bala2(z,t):
    zp = sp.zeros(4)   
    zp[0] = z[2]
    zp[1] = z[3]    
    v = z[2:4] #### saco los ultimos dos componentes
    v[0] = v[0] - V3    
    v2 = sp.dot(v,v)
    vnorm = sp.sqrt(v2)
    FD = -CD * v2 * (v / vnorm)    
    zp[2] = FD[0] / m
    zp[3] = FD[1] / m - g 
    
    return zp

#### vector de tiempo 
t = sp.linspace(0, 6, 1000)

#### parte en el origen y tiene vx = vy = 2 m/s
vi = 100*1000./3600.
z0 = sp.array([0, 0, vi, vi ])

sol = odeint(bala, z0, t)
sol1 = odeint(bala1, z0, t)
sol2 = odeint(bala2, z0, t)

import matplotlib.pylab as plt

x = sol[:,0]
y = sol[:,1]

x1 = sol1[:,0]
y1 = sol1[:,1]

x2 = sol2[:,0]
y2 = sol2[:,1]

#### grafico 

plt.figure()

plt.ylabel("Y (m)")
plt.xlabel("X (m)")
plt.title(" trayectoria para distintos vientos") 
plt.grid(True)
plt.plot(x,y,label="V = 0 m/s")
plt.plot(x1,y1,label="V = 10 m/s")
plt.plot(x2,y2,label="V = 20 m/s")
plt.ylim([0,50])
plt.xlim([0,150])
plt.legend()

plt.tight_layout()
plt.savefig("BALISTICA.png",dpi=500)

    
    
    
import numpy as np
from numpy import sin,cos

from scipy.integrate import odeint
from matplotlib import pyplot as plt

#CONDICIONES INICIALES

y=0

z=0

Vx=0 

Vz=0

#constante gravitacional
G=6.674e-11

#masa de la tierra
Mt=5e24

#distancia del satelite a la tierra
r=7071000

x=r

#velocidad angular del satelite
Ω=7.27440e-5

#velocidad inicial en el eje y
Vy=5800

t = np.linspace(0,13930,10000)

def satelite(z,t):
    R=np.array([[cos(Ω*t),-sin(Ω*t),0],[sin(Ω*t),cos(Ω*t), 0],[0., 0., 1]])

    dR_dt=np.array([[-sin(Ω*t),-cos(Ω*t),0],
                    [cos(Ω*t),-sin(Ω*t), 0],
                    [0., 0., 0.]])*Ω

    dR2_dt2=np.array([[-cos(Ω*t),sin(Ω*t), 0],[-sin(Ω*t),-cos(Ω*t),0],[0., 0., 0]])*Ω**2
    
    zp = np.zeros(6)
    zp[0:3] = z[3:6]
    z2p=(-G*Mt/(r**3))*z[0:3]-R.T@(dR2_dt2@z[0:3]+2*dR_dt@z[3:6])
    zp[3:6] = z2p
    return zp

z0 = np.array([x, y, z, Vx, Vy, Vz ])

sol = odeint(satelite, z0, t)


x = sol[:,0]
y = sol[:,1]
z = sol[:,2]

plt.figure(1)


plt.plot(t, x, label = "Distancia en x(t)", color = "violet")

plt.plot(t ,y, label = "Distancia en y(t)", color = "gold")

plt.plot(t ,z, label = "Distancia en z(t)", color = "red")

plt.ylabel("DISTANCIA (m)")
plt.xlabel("TIEMPO (t)")
plt.title("[Distancia en funcion del tiempo SATELITE]") 
plt.grid(True)

plt.tight_layout()
plt.legend()

plt.savefig("Distancia en funcion del tiempo SATELITE.png",dpi=500)






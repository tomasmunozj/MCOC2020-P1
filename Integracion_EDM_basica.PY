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

r_world = 6371000

V_A = np.arange(0, 2*np.pi, .01)

x1 = r_world*sin(V_A)
y1 = r_world*cos(V_A)

plt.plot(x1, y1,label="Atmosfera")

ATM = plt.Circle((0,0), r_world, color = "rosybrown")

plt.gcf().gca().add_artist(ATM)

plt.plot(x,y,label="satelite",color="green")

plt.ylabel("Y (Metros)")
plt.xlabel("X (Metros)")
plt.title("[Trayectoria del satelite]") 
plt.grid(True)

plt.tight_layout()
plt.legend()

plt.savefig("Trayectoria satelite.png",dpi=500)


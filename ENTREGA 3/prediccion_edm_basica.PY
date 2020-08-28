import numpy as np
from numpy import sin,cos

from scipy.integrate import odeint

#CONDICIONES INICIALES
y=0

z=0

Vx=0 

Vz=0

#CONSTANTE GRAVITACIONAL
G=6.67408e-11

#MASA DE LA TIERRA
Mt=5.972e24

#DISTANCIA DEL SATELITE A LA TIERRA
r=7071000
x=r

#VELOCIDAD ANGULAR DEL SATELITE
Ω=7.2921000e-5

#VELOCIDAD INICIA TANGENCIAL EN EL EJE Y
Vy=10000

#VECTOR DE TIEMPO
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

from datetime import datetime


ti = "2020-07-27T23:00:19.000000"
ti = ti.split("T")
ti = "{} {}".format(ti[0],ti[1])
ti = datetime.strptime(ti, '%Y-%m-%d %H:%M:%S.%f')

tf = "2020-07-29T00:59:42.000000"
tf = tf.split("T")
tf = "{} {}".format(tf[0],tf[1])
tf = datetime.strptime(tf, '%Y-%m-%d %H:%M:%S.%f')

DeltaT = (tf-ti).seconds

x_i = 1786960.484609
y_i = 3516995.995776
z_i = -5881478.109617

vx_i = -761.534117
vy_i = -6361.528274
vz_i = -4037.695910

x_f = 1771146.809826
y_f = 3389014.621421
z_f = -5960906.801128

vx_f = -819.810030
vy_f = -6436.104108
vz_f = -3904.879392

t = np.linspace(0,DeltaT,9361)

z0 = np.array([x_i, y_i, z_i, vx_i, vy_i, vz_i])

sol = odeint(satelite,z0,t)
x = sol[:, :]
pos_final = np.array([x_f, y_f, z_f, vx_f, vy_f, vz_f]) - sol[-1]

for i in pos_final:
    print (i)


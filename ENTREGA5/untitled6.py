import numpy as np
from numpy import sin,cos

from scipy.integrate import odeint
from leer_eof import leer_eof
from matplotlib.pylab import *
import matplotlib.pyplot as plt
import xml
import xml.etree.ElementTree as ET
from numpy import zeros
import datetime as dt
from time import perf_counter

#CODIGO PROFESOR------------------------------------------------------
def utc2time(utc, ut1, EOF_datetime_format = "%Y-%m-%dT%H:%M:%S.%f"):
	t1 = dt.datetime.strptime(ut1,EOF_datetime_format)
	t2 = dt.datetime.strptime(utc,EOF_datetime_format)
	return (t2 - t1).total_seconds()


def leer_eof(fname):
	tree = ET.parse(fname)
	root = tree.getroot()

	Data_Block = root.find("Data_Block")		
	List_of_OSVs = Data_Block.find("List_of_OSVs")

	count = int(List_of_OSVs.attrib["count"])

	t = zeros(count)
	x = zeros(count)
	y = zeros(count)
	z = zeros(count)
	vx = zeros(count)
	vy = zeros(count)
	vz = zeros(count)

	set_ut1 = False
	for i, osv in enumerate(List_of_OSVs):
		UTC = osv.find("UTC").text[4:]
		
		x[i] = osv.find("X").text   #conversion de string a double es implicita
		y[i] = osv.find("Y").text
		z[i] = osv.find("Z").text
		vx[i] = osv.find("VX").text
		vy[i] = osv.find("VY").text
		vz[i] = osv.find("VZ").text

		if not set_ut1:
			ut1 = UTC
			set_ut1 = True

		t[i] = utc2time(UTC, ut1)

	return t, x, y, z, vx, vy, vz

#-----------------------------------------------------------------------------




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


#CODIGO PROFESOR------------------------------------------
def eulerint(zp, z0, t, Nsubdivisiones = 1):
    Nt = len(t)
    Ndim = len(np.array(z0))
    
    z = np.zeros((Nt,Ndim))
    z[0,:] = z0[0]
    
    for i in range(1,Nt):
        t_anterior = t[i-1]
        dt = (t[i] - t[i-1])/Nsubdivisiones
        z_temp = z[i-1,:]
        
        for k in range(Nsubdivisiones):
            z_temp += dt * satelite(z_temp,t_anterior + k*dt)
            
        z[i,:] = z_temp
        
    return z
#–---------------------------------------------------------+

t, x, y, z, vx, vy, vz = leer_eof("S1A_OPER_AUX_POEORB_OPOD_20200817T120818_V20200727T225942_20200729T005942.EOF")


#vector de condición inicial
z0 = np.array([x[0], y[0], z[0], vx[0], vy[0], vz[0]])
sol = odeint(satelite, z0, t)
x1 = sol[:, 0]
y1 = sol[:, 1]
z1 = sol[:, 2]
z_p = sol[:, :]
t_1 = perf_counter()
s_f = eulerint(z_p, z0, t, Nsubdivisiones=20)
t_2 = perf_counter()
tiempo = t_2 - t_1
z_euler = s_f[:, 0]


d_p = np.sqrt((x1 - x) ** 2 + (y1 - y) ** 2 + (z1 - z) ** 2)
plot(t/3600, d_p/1000)
plt.xlabel("Tiempo, t (horas)")
plt.ylabel("Deriva ( KM )")
title("Distancia entre posicion real y predicha :O ")



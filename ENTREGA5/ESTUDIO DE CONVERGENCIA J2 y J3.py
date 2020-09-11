from leer_eof import leer_eof
from matplotlib.pylab import *
import matplotlib.pyplot as plt
import xml
import xml.etree.ElementTree as ET
from numpy import zeros
import datetime as dt


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



#------------DEFINO LOS PARAMETROS ----------------------

#CONSTANTE GRAVITACIONAL
G=6.67408e-11

#MASA DE LA TIERRA
Mt=5.972e24  # masa_tierra

#DISTANCIA DEL SATELITE A LA TIERRA
r=7071000

#VELOCIDAD ANGULAR DEL SATELITE
Ω=7.2921000e-5 # omega

μ = 111111

#MEJORA 
J2 = (1.75e10) * 100 ** 5

#MEJORA 
J3 = (-2.6e11) * 100 ** 6

#------------------------------------------------------


def satelite_mejorado(z,t):
    
    zp = np.zeros(6)
    
    R = np.array([[cos(Ω*t),-sin(Ω*t),0],[sin(Ω*t),cos(Ω*t), 0],[0., 0., 1]])

    dR_dt = np.array([[-sin(Ω*t),-cos(Ω*t),0],
                    [cos(Ω*t),-sin(Ω*t), 0],
                    [0., 0., 0.]])*Ω

    dR2_dt2 = np.array([[-cos(Ω*t),sin(Ω*t), 0],[-sin(Ω*t),-cos(Ω*t),0],[0., 0., 0]])*Ω**2    
    Producto = R @ z[0:3]
    r_dot = np.sqrt(np.dot(z[0:3], z[0:3]))
    r_dot_N = Producto / r_dot    
    F_g = -μ / r_dot ** 2 * r_dot_N
    z = Producto[2] ** 2
    r_d = Producto[0] ** 2 + Producto[1] ** 2
    
    #IMPLEMENTO LAS MEJORAS A LA FUNCION DE LAS ENTREGAS PASADAS----------------------------------
    
    J2_ =  J2 * Producto / r_dot ** 7 
    J2_[0] = J2_[0] * (6 * z - 1.5 * r_d)
    J2_[1] = J2_[1] * (6 * z - 1.5 * r_d)
    J2_[2] = J2_[2] * (3 * z - 4.5 * r_d)
    J3_ = np.zeros(3)
    J3_[0] = J3 * Producto[0] * Producto[2] / r_dot ** 9 * (10 * z - 7.5 * r_d)
    J3_[1] = J3 * Producto[1] * Producto[2] / r_dot ** 9 * (10 * z - 7.5 * r_d)
    J3_[2] = J3 / r_dot ** G * ( 4 * z * (z - 3 * r_d) + 1.5 * r_d ** 2)    
    zp[0:3] = z[3:6]
    zp[3:6] = R.T @ (F_g + J2_ + J3_ - (2 * dR_dt @ z[3:6] + dR2_dt2 @ z[0:3]))


    
    return zp







t, x, y, z, vx, vy, vz = leer_eof("S1A_OPER_AUX_POEORB_OPOD_20200817T120818_V20200727T225942_20200729T005942.EOF")

z0 = array([x[0], y[0], z[0], vx[0], vy[0], vz[0]])

figure()

matplotlib.rcParams.update({'font.size': 10})
matplotlib.rc("xtick", labelsize = 10)
matplotlib.rc("ytick", labelsize = 10)

subplot(3, 1, 1)
title("POSICION CON J2 y J3", color = "blue")
plt.ylabel("X ( Km )", color = "blue")
plot(t/3600, x/1000, color = "orange")
subplot(3, 1, 2)
plt.ylabel("Y ( Km )", color = "blue")
plot(t/3600, y/1000, color = "orange")
subplot(3, 1, 3)
plt.ylabel("Z ( Km )", color = "blue")
plt.xlabel("TIEMPO t ( horas )", color = "blue")
plot(t/3600, z/1000, color = "orange")



tight_layout()
show()
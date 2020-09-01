from scipy.integrate import odeint
import matplotlib.pylab as plt
from numpy import cos,sin ,pi
import numpy as np
from matplotlib.pylab import *

#PARAMETROS Y CONDICIONES INICIALES DE ENUNCIADO
#------------------------------------------------
M = 1

F = 1

E = 0.2

W = 2 * pi * F

K = M * W**2

C = 2 * E * W * M

t = np.linspace(0, 4., 100)

x0 = 1

v0 = 1

z0 = [x0, v0]
#-----------------------------------------------

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
            z_temp += dt * z_p(z_temp,t_anterior + k*dt)
            
        z[i,:] = z_temp
        
    return z
#–---------------------------------------------------------

#ESTA PARTE ES CLAVE PARA LA EJECUCION DEL CODIGO----------
def z_p(z,t):
    zp = zeros(2)
    
    zp[0] = z[1]
    z1 = z[0]
    z2 = z[1]
    
    zp[1] = -(C * z2 + K * z1) 
    
    return zp
#-----------------------------------------------------------

sol_edo = np.exp(-C * t / 2) * cos(W * t)
sol = odeint(z_p,z0,t)
x2p = sol[:,0]
zp = sol[:,:]

colores = ["mediumseagreen" , "red" , "darkorange"]
Sub_Div = [1,10,100]

for i in range(3):
    lista_Sub = Sub_Div[i]
    Euler = eulerint(zp, z0, t, Nsubdivisiones = Sub_Div[i])
    plot(t , Euler[:,0] ,":," ,color = colores[i], label = f"Eulerint Nsubdivision={Sub_Div[i]}")


plt.plot(t, x2p, color = "blue", label = "odeint")
plt.plot(t, sol_edo, color = "black", linewidth = 2, label = "solucion analitica")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,facecolor="azure")
plt.grid(True)

plt.xlabel("TIEMPO",fontsize=20)
plt.ylabel("POSICION",fontsize=20)
matplotlib.rc("xtick", labelsize=15) 
matplotlib.rc("ytick", labelsize=15) 
plt.suptitle("OSCILADOR ARMONICO", fontsize=30)


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


t, x, y, z, vx, vy, vz = leer_eof("S1A_OPER_AUX_POEORB_OPOD_20200817T120818_V20200727T225942_20200729T005942.EOF")

z0 = array([x[0], y[0], z[0], vx[0], vy[0], vz[0]])

figure()

matplotlib.rcParams.update({'font.size': 10})
matplotlib.rc("xtick", labelsize=10)
matplotlib.rc("ytick", labelsize=10)

subplot(3, 1, 1)
title("POSICION", color="green")
plt.ylabel("X ( Km )", color="green")
plot(t/3600, x/1000, color="orange")
subplot(3, 1, 2)
plt.ylabel("Y ( Km )", color="green")
plot(t/3600, y/1000, color="orange")
subplot(3, 1, 3)
plt.ylabel("Z ( Km )", color="green")
plt.xlabel("TIEMPO t ( horas )", color="green")
plot(t/3600, z/1000, color="orange")



tight_layout()
show()





import matplotlib.pyplot as plt
import csv

x = [] # position along x (nm)
y1 = [] # Gamma bandedge (eV)
y2 = [] # heavy hole (hh) band edge (eV)

with open('bandedge-x.dat', 'r') as csvfile:
	data = csv.reader(csvfile, delimiter=' ')
	for row in data:
		x.append(row[4])

		if row[8]: # check if there's negative sign
			y1.append(row[8])
			y2.append(row[11])
		else:
			y1.append(row[7])
			y2.append(row[10])

plt.plot(x, y1, label='Gamma conduction band', color='r')
plt.plot(x, y2, label='Heavy hole valence band', color='c')

plt.xlabel('Position along x-axis (nm)')
plt.ylabel('Gamma bandedge (eV)')

plt.title ('Band energy along x-axis')
plt.legend()

plt.show()
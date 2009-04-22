#!/Library/Frameworks/Python.framework/Versions/Current/bin/python

import sys
import matplotlib.pyplot as plt
from DensityProfiler import *
from StatisticMachine import * 

files = []
for file in sys.argv:
	files.append(file)
files = files[1:]

d = DensityProfiler(files)

m = StatisticMachine()

for file in range(len(files)):
	x_exp = d.data[file]['position']
	x_fit = d.fits[file]['position']

	w_exp = (x_exp, d.data[file]['h2o'])
	w_fit = (x_fit, d.fits[file]['h2o'])
	w_r_square = m.r_square(w_exp,w_fit)

	a_exp = (x_exp, d.data[file]['anion'])
	a_fit = (x_fit, d.fits[file]['anion'])
	a_r_square = m.r_square(a_exp,a_fit)

	c_exp = (x_exp, d.data[file]['cation'])
	c_fit = (x_fit, d.fits[file]['cation'])
	c_r_square = m.r_square(c_exp,c_fit)

	print "%s r-sqaured values\n\twater = % 5.4f\n\tanion = % 5.4f\n\tcation = % 5.4f\n" % (files[file], w_r_square, a_r_square, c_r_square)

#plt.plot(exp[0],exp[1],'k:',linewidth=3)
#plt.plot(sim[0],sim[1],'k-')
#plt.plot(exp[0],res,'g-')
#plt.xlim(-8,8)
#plt.show()

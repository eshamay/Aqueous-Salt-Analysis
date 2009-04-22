#!/Library/Frameworks/Python.framework/Versions/Current/bin/python

from scipy import *
from scipy.optimize import leastsq
import scipy.io.array_import

import matplotlib.pyplot as plt
import matplotlib.patches


def residuals(p, y, x):
	err = y-peval(x,p)
	return err

def peval(x,p):
	return 0.5*(p[0]+p[1]) - 0.5*(p[0]-p[1])*tanh((x-p[2])/p[3])

# file i/o to get the data
filename = ('density.avg.dat')
data = scipy.io.array_import.read_array(filename)

x = data[:,0]
# fitting to water (18.02 mol weight)
O = data[:,1] * 18.02
C = data[:,2] * 153.82
NA = data[:,3] * 230.0
NO3 = data[:,4] * 310.0245

# initial guess values
p1 = 0.0
p2 = 1.0
x0 = 0.0
d0 = 5.0

pname = (['p1','p2','x0','d0'])
p0 = array ([p1,p2,x0,d0])
plsq = leastsq(residuals, p0, args=(O,x), maxfev=10000)

fit = peval(x,plsq[0])

x = x - p0[2]

print "Final Parameters"
print "Bulk density: ", p0[0]
print "Zero density: ", p0[1]
print "gibbs surface: ", p0[2]
print "thickness d = ", p0[3], " t = ", p0[3]*2.197
print

fig = plt.figure(num=1, facecolor='w', edgecolor='k', frameon=False)
ax = fig.add_subplot(111)
ax.set_autoscale_on(False)
ax.plot(x,O,'k', linewidth=3)
ax.plot(x,fit,'g',linewidth=2)
ax.plot(x,C,'k:',linewidth=2)
ax.plot(x,NA,'k',linewidth=2)
ax.plot(x,NO3,'k--',linewidth=2)

gibbs1 = matplotlib.patches.Ellipse ((0, (p0[1]-p0[0])/2.0), 0.5, 0.1, alpha=0.0, fc="none")
ax.add_patch(gibbs1)

ax.grid(False)

ax.vlines(0.0, ax.get_ybound()[0], ax.get_ybound()[1], color='k', linestyles='dotted', label="% 8.3f" % p0[2])

ax.annotate("Gibbs-surface\nthickness = %5.3f\n\"90-10\" = %5.3f" % (p0[3], p0[3]*2.197), (0.0, (p0[1]+p0[0])/2.0), 
	xytext=(120,30), textcoords='offset points', size=20,
	bbox=dict(boxstyle="round", fc=(1.0, 0.7, 0.7), ec=(1., .5, .5)),
    arrowprops=dict(arrowstyle="wedge,tail_width=1.",
    	fc=(1.0, 0.7, 0.7), ec=(1., .5, .5),
        patchA=None,
        patchB=gibbs1,
        relpos=(0.2, 0.8),
        connectionstyle="arc3,rad=-0.1"),
    )

#ion locations
max_NO3, max_NO3_index = max((no3, i) for i, no3 in enumerate(NO3))

ax.annotate("NO3- max at %5.3f" % (x[max_NO3_index]), (x[max_NO3_index], max_NO3),
	xytext=(120, 30), textcoords='offset points', size=20,
	bbox=dict(boxstyle="round", fc=(1.0, 0.7, 0.7), ec=(1., .5, .5)),
    arrowprops=dict(arrowstyle="wedge,tail_width=1.",
    	fc=(1.0, 0.7, 0.7), ec=(1., .5, .5),
		patchA=None,
        relpos=(0.2, 0.8),
        connectionstyle="arc3,rad=-0.1"),
    )

max_NA, max_NA_index = max((na, i) for i, na in enumerate(NA))

ax.annotate("Na+ max at %5.3f" % (x[max_NA_index]), (x[max_NA_index], max_NA),
	xytext=(-60, 30), textcoords='offset points', size=20,
	bbox=dict(boxstyle="round", fc=(1.0, 0.7, 0.7), ec=(1., .5, .5)),
    arrowprops=dict(arrowstyle="wedge,tail_width=1.",
    	fc=(1.0, 0.7, 0.7), ec=(1., .5, .5),
		patchA=None,
        relpos=(0.2, 0.8),
        connectionstyle="arc3,rad=-0.1"),
    )



leg = ax.legend(('H2O', 'Fit', 'CCl4', 'Na+', 'NO3-'), 'best', shadow=True)
ax.set_xlabel('Slab Position (Angstroms) --->')
ax.set_ylabel('Density (g/ml) --->')
ax.set_title('Simulation Slab Density')

ax.set_ylim([0,max(C)+0.1])
ax.set_xlim([p0[2] - 10.0 , p0[2]+6.0])
ax.set_axis_bgcolor('w')
# set some legend properties.  All the code below is optional.  The
# defaults are usually sensible but if you need more control, this
# shows you how

# the matplotlib.patches.Rectangle instance surrounding the legend
frame  = leg.get_frame()
frame.set_facecolor('0.80')    # set the frame face color to light gray

# matplotlib.text.Text instances
for t in leg.get_texts():
    t.set_fontsize('small')    # the legend text fontsize

# matplotlib.lines.Line2D instances
for l in leg.get_lines(): 
    l.set_linewidth(1.5)  # the legend line width
plt.show()

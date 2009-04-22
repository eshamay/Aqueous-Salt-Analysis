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
	return 0.5*(p[0]+p[1]) - 0.5*(p[0]-p[1])*tanh((x-p[2])/p[3]) - 0.5*(p[4]-p[5])*tanh((x-p[6])/p[7])

# file i/o to get the data
filename = ('density.dat')
data = scipy.io.array_import.read_array(filename)

x = data[:,0]
# fitting to water (18.02 mol weight)
y = data[:,1] * 18.02
C = data[:,2] * 153.82
NA = data[:,3] * 23.0
CL = data[:,4] * 35.45

# initial guess values
p1_1 = 0.0
p1_2 = 1.0
p2_1 = 1.0
p2_2 = 0.0
x1 = 30.0
x2 = 55.0
d1 = 5.0
d2 = 5.0
pname = (['p1_1','p1_2','x1','d1','p2_1','p2_2','x2','d2'])
p0 = array ([p1_1,p1_2,x1,d1,p2_1,p2_2,x2,d2])
plsq = leastsq(residuals, p0, args=(y,x), maxfev=10000)

fit = peval(x,plsq[0])

print "Final Parameters"
print "density of side 1: ", p0[1] - p0[0]
print "gibbs surface: ", p0[2]
print "thickness d = ", p0[3], " t = ", p0[3]*2.197
print
print "density of side 2: ", p0[4] - p0[5]
print "gibbs surface: ", p0[6]
print "thickness d = ", p0[7], " t = ", p0[7]*2.197


fig = plt.figure(num=1, facecolor='w', edgecolor='w', frameon=False)
ax = fig.add_subplot(111)
ax.set_autoscale_on(False)
ax.plot(x,y,'k', linewidth=3)
ax.plot(x,fit,'g',linewidth=2)
ax.plot(x,C,'k:',linewidth=2)
ax.plot(x,NA,'k--',linewidth=2)
ax.plot(x,CL,'k-.',linewidth=2)

gibbs1 = matplotlib.patches.Ellipse ((p0[2], (p0[1]-p0[0])/2.0), 0.5, 0.1, alpha=0.0, fc="none")
gibbs2 = matplotlib.patches.Ellipse ((p0[6], (p0[4]-p0[5])/2.0), 0.5, 0.1, alpha=0.0, fc="none")
ax.add_patch(gibbs1)
ax.add_patch(gibbs2)

#ax.set_ylim([0,max(C)+0.4])
ax.grid(False)

ax.vlines(p0[2], ax.get_ybound()[0], ax.get_ybound()[1], color='k', linestyles='dotted', label="% 8.3f" % p0[2])
ax.vlines(p0[6], ax.get_ybound()[0], ax.get_ybound()[1], color='k', linestyles='dotted', label="% 8.3f" % p0[6])

ax.annotate("% 8.3f (thickness = % 5.3f)\n\"90-10\" = % 5.3f" % (p0[2], p0[3], p0[3]*2.197), (p0[2], (p0[1]-p0[0])/2.0), 
	xytext=(p0[2]-9.0, (p0[1]-p0[0])/2.0+0.3), 
	arrowprops=dict(
		arrowstyle="fancy", connectionstyle="angle3, angleA=-90", patchB=gibbs1, fc="0.6", ec="none")
	)

ax.annotate("% 8.3f (thickness = % 5.3f)\n\"90-10\" = % 5.3f" % (p0[6], p0[7], p0[7]*2.197), (p0[6], (p0[4]-p0[5])/2.0), 
	xytext=(p0[6]+1.0, (p0[4]-p0[5])/2.0+0.3),
	arrowprops=dict(
		arrowstyle="fancy", connectionstyle="angle3, angleA=-90", patchB=gibbs2, fc="0.6", ec="none")
	)

leg = ax.legend(('H2O', 'Fit', 'CCl4', 'Na+', 'Cl-'), 'best', shadow=True)
ax.set_xlabel('Slab Position (Angstroms) --->')
ax.set_ylabel('Density (g/ml) --->')
ax.set_title('Simulation Slab Density')

ax.set_ylim([0,max(C)+0.4])
ax.set_xlim([30.0, 90.0])
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
#plt.savefig('density.dat.png', dpi=300.0, format='png' )


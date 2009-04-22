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

def annotate_gibbs(x0,d,p1,p2,offset):
	ax.annotate("%5.3f\nthickness = %5.3f\n\"90-10\" = %5.3f" % (x0, d, d*2.197), (x0, (p2-p1)/2.0), 
		xytext=offset, textcoords='offset points', size=15,
		bbox=dict(boxstyle="round", fc=(1.0, 0.7, 0.7), ec=(1., .5, .5)),
    	arrowprops=dict(arrowstyle="wedge,tail_width=1.",
    		fc=(1.0, 0.7, 0.7), ec=(1., .5, .5),
        	patchA=None,
        	patchB=gibbs1,
        	relpos=(0.2, 0.8),
        	connectionstyle="arc3,rad=-0.1"),
    	)

def annotate_point(x,y,offset):
	ax.annotate("%5.3f" % (x), (x, y),
		xytext=offset, textcoords='offset points', size=15,
		bbox=dict(boxstyle="round", fc=(1.0, 0.7, 0.7), ec=(1., .5, .5)),
    	arrowprops=dict(arrowstyle="wedge,tail_width=1.",
    		fc=(1.0, 0.7, 0.7), ec=(1., .5, .5),
			patchA=None,
        	relpos=(0.2, 0.8),
        	connectionstyle="arc3,rad=-0.1"),
    	)

def annotate_max (Xdata,Ydata,offset):
	Ydata = Ydata.tolist()
	y1, index1 = max((data, i) for i, data in enumerate(Ydata))
	x1 = Xdata[index1]

	annotate_point(x1,y1,offset)



# file i/o to get the data
filename = ('density1.dat')
data = scipy.io.array_import.read_array(filename)

x = data[:,0]
# fitting to water (18.02 mol weight)
y = data[:,1] * 18.02
C = data[:,2] * 153.82
NA = data[:,3] * 23.0 * 10.0
CL = data[:,4] * 35.45 * 10.0

# initial guess values
p1 = 0.0
p2 = 1.0
x0 = 30.0
d = 5.0
pname = (['p1','p2','x0','d'])
p0 = array ([p1,p2,x0,d])
plsq = leastsq(residuals, p0, args=(y,x), maxfev=10000)

fit = peval(x,plsq[0])

print "Final Parameters"
print "density of side 1: ", p0[1] - p0[0]
print "gibbs surface: ", p0[2]
print "thickness d = ", p0[3], " t = ", p0[3]*2.197

fig = plt.figure(num=1, facecolor='w', edgecolor='w', frameon=False)
ax = fig.add_subplot(111)
ax.set_autoscale_on(False)
ax.plot(x,y,'k', linewidth=3)
ax.plot(x,fit,'g',linewidth=2)
ax.plot(x,C,'k:',linewidth=2)
ax.plot(x,NA,'k--',linewidth=2)
ax.plot(x,CL,'k-.',linewidth=2)

gibbs1 = matplotlib.patches.Ellipse ((p0[2], (p0[1]-p0[0])/2.0), 0.5, 0.1, alpha=0.0, fc="none")
ax.add_patch(gibbs1)

#ax.set_ylim([0,max(C)+0.4])
ax.grid(False)

ax.vlines(p0[2], ax.get_ybound()[0], ax.get_ybound()[1], color='k', linestyles='dotted', label="% 8.3f" % p0[2])

annotate_gibbs(p0[2],p0[3],p0[0],p0[1],(-250,0))
annotate_max(x,NA,(20,100))
annotate_max(x,CL,(20,100))

leg = ax.legend(('H2O', 'Fit', 'CCl4', 'Na+', 'Cl-'), 'best', shadow=True)
ax.set_xlabel('Slab Position (Angstroms) --->')
ax.set_ylabel('Density (g/ml) --->')
ax.set_title('Simulation Slab Density')

ax.set_ylim([0,max(C)])
ax.set_xlim([30.0, 45.0])
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


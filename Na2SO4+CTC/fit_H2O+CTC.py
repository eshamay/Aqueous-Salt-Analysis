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

def annotate_maxes (Xdata,Ydata,offset1,offset2):
	Ydata = Ydata.tolist()
	y1, index1 = max((data, i) for i, data in enumerate(Ydata[:len(Ydata)/2]))
	#Ydata_copy = Ydata
	#Ydata_copy = Ydata_copy.tolist()
	#Ydata_copy = Ydata_copy[1:1000]
	y2, index2 = max((data, i) for i, data in enumerate(Ydata[len(Ydata)/2:]))
	index2 = index2 + len(Ydata)/2
	x1 = Xdata[index1]
	x2 = Xdata[index2]

	annotate_point(x1,y1,offset1)
	annotate_point(x2,y2,offset2)



# file i/o to get the data
filename = ('density.dat')
data = scipy.io.array_import.read_array(filename)

x = data[:,0]
# fitting to water (18.02 mol weight)
y = data[:,1] * 18.02
C = data[:,2] * 153.82
NA = data[:,3] * 230.0
SO4 = data[:,4] * 480.35

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
# perform the fitting
plsq = leastsq(residuals, p0, args=(y,x), maxfev=10000)
fit = peval(x,plsq[0])

print "Final Parameters"
print "density of side 1: ", p0[1] - p0[0]
print "density of side 2: ", p0[4] - p0[5]

# plot out all the lines
fig = plt.figure(num=1, facecolor='w', edgecolor='w', frameon=False)
ax = fig.add_subplot(111)
ax.set_autoscale_on(False)
ax.plot(x,y,'k', linewidth=3)
ax.plot(x,fit,'g',linewidth=2)
ax.plot(x,C,'k:',linewidth=2)
ax.plot(x,NA,'k',linewidth=2)
ax.plot(x,SO4,'k--',linewidth=2)

# set a couple patches to point out the gibbs surfaces
gibbs1 = matplotlib.patches.Ellipse ((p0[2], (p0[1]-p0[0])/2.0), 0.5, 0.1, alpha=0.0, fc="none")
gibbs2 = matplotlib.patches.Ellipse ((p0[6], (p0[4]-p0[5])/2.0), 0.5, 0.1, alpha=0.0, fc="none")
ax.add_patch(gibbs1)
ax.add_patch(gibbs2)

# vertical lines to show where the dividing surfaces are
ax.vlines(p0[2], ax.get_ybound()[0], ax.get_ybound()[1], color='k', linestyles='dotted', label="% 8.3f" % p0[2])
ax.vlines(p0[6], ax.get_ybound()[0], ax.get_ybound()[1], color='k', linestyles='dotted', label="% 8.3f" % p0[6])

# label the gibbs dividing surfaces
annotate_gibbs(p0[2],p0[3],p0[0],p0[1],(-110,75))
annotate_gibbs(p0[6],p0[7],p0[5],p0[4],(45,45))

# label the max points for the ions in solution
annotate_maxes (x,SO4,(20,50),(-30,30))
annotate_maxes (x,NA,(20,60),(-60,50))

# print out a legend and axis labels
leg = ax.legend(('H2O', 'H2O tanh() Fit', 'CCl4', 'Na+ (x10 scale)', 'SO42- (x5 scale)'), 'best', shadow=True)
ax.set_xlabel('Slab Position (Angstroms) --->')
ax.set_ylabel('Density (g/ml) --->')
ax.set_title('Simulation Slab Density')

# set the axis limits
ax.set_ylim([0,max(C)+0.4])
ax.set_xlim([30.0, 120.0])
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


#!/Library/Frameworks/Python.framework/Versions/Current/bin/python
import csv
import numpy
import sys

import matplotlib.pyplot as plt
import matplotlib.patches

# Should handle extracting all the data we want into a dictionary from the coordination files
def DataDict(filename):
	datareader = csv.reader(open(filename), dialect=csv.excel_tab)

	data = []
	header = datareader.next()

	for name in range(len(header)):
		data.append([])

	for row in datareader:
		row = row[0]
		row = row.strip()
		row = row.split()
		for datum in range(len(row)):
			data[datum].append(float(row[datum]))
	
	data_dict = {}
	for name in range(len(header)):
		data_dict[header[name]] = data[name]

	return data_dict

#******************************************************#

coord = ''
files = []
# The coordination to plot
if sys.argv[1] == 'coord':
	coord = sys.argv[2]
	files.append('H2O+CTC')
	files.append('NaCl+CTC')
	files.append('Na2SO4+CTC')
	files.append('NaNO3+CTC')

else:
	files.append(sys.argv[1])

# file i/o to get the data
dicts = []
legend_names = []
for file in files:
	dicts.append (DataDict(file + '/coordination.avg.dat'))
	if coord != '':
		legend_names.append (file)

if coord == "":
	legend_names.append ('OH')
	legend_names.append ('OOH')
	legend_names.append ('OHH')
	legend_names.append ('OOHH')
	legend_names.append ('OOOHH')
	legend_names.append ('OOHHH')

# Set up the plot parameters (labels, size, limits, etc)
fig = plt.figure(num=1, facecolor='w', edgecolor='w', frameon=False)
ax = fig.add_subplot(111)
ax.set_autoscale_on(True)
ax.set_xlabel(r'Slab Position', size='xx-large')
if coord == '':
	plt.setp(ax.get_yticklabels(), visible=False)
plt.setp(ax.get_xticklabels(), visible=True, size='x-large')

if coord == '':
	ax.set_ylabel(r'Relative Density', size='xx-large')
else:
	ax.set_ylabel(r'Normalized Density', size='xx-large')
	
if coord == '':
	ax.set_title(files[0].split('+')[0] + r' / CCl$_4$ - Water Coordination', size='xx-large')
else:
	ax.set_title(coord + ' - Coordinated Waters', size='xx-large')

filesize = 82

for d in dicts:
	x = d['position'][filesize:]
	data = []
	if coord == '':
		for c in legend_names:
			data = d[c][filesize:]
			ax.plot(x, data, linewidth=2)
	else:
		data = d[coord][filesize:]
		data = data / numpy.trapz(data,x,dx=0.1)	# normalize by area under the curve
		ax.plot(x, data, linewidth=2)

ax.set_xlim([-18,22])
ax.grid(False)

#ax.vlines(p0[2], ax.get_ybound()[0], ax.get_ybound()[1], color='k', linestyles='dotted', label="% 8.3f" % p0[2])
#ax.vlines(p0[6], ax.get_ybound()[0], ax.get_ybound()[1], color='k', linestyles='dotted', label="% 8.3f" % p0[6])

leg = ax.legend(tuple(legend_names), 'best', shadow=True)
ax.set_axis_bgcolor('w')
# set some legend properties.  All the code below is optional.  The
# defaults are usually sensible but if you need more control, this
# shows you how

# the matplotlib.patches.Rectangle instance surrounding the legend
frame = leg.get_frame()
frame.set_facecolor('0.80')    # set the frame face color to light gray

# matplotlib.text.Text instances
for t in leg.get_texts():
    t.set_fontsize('x-large')    # the legend text fontsize

# matplotlib.lines.Line2D instances
for l in leg.get_lines(): 
    l.set_linewidth(1.5)  # the legend line width

#plt.show()
if coord == '':
	plt.savefig(files[0]+'/coordination.avg-'+files[0]+'.pdf', dpi=600.0, edgecolor='w', orientation='landscape', format='pdf' )
else:
	plt.savefig('coordination.avg-'+coord+'.pdf', dpi=600.0, edgecolor='w', orientation='landscape', format='pdf' )
	

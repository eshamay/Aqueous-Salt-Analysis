#!/Library/Frameworks/Python.framework/Versions/Current/bin/python
"""
connect the data limits on the axes in one figure with the axes in
another.  This is not the right way to do this for two axes in the
same figure -- use the sharex and sharey property in that case
"""
# -*- noplot -*-
import numpy
from pylab import figure, show

fig1 = figure()
fig2 = figure()

ax1 = fig1.add_subplot(111)
ax2 = fig2.add_subplot(111, sharex=ax1, sharey=ax1)

ax1.plot(numpy.random.rand(100), 'o')
ax2.plot(numpy.random.rand(100), 'v')

# In the latest release, it is no longer necessary to do anything
# special to share axes across figures:

# ax1.sharex_foreign(ax2)
# ax2.sharex_foreign(ax1)

# ax1.sharey_foreign(ax2)
# ax2.sharey_foreign(ax1)

show()

def pretty_format(f, fmt='%0.3f'):
return fmt % f

I want to use it with map() like this:

formatted = map(pretty_format, unformatted_list)
#exept I want fmt='%4.5f' !!!

def curry(f, **kwargs):
return lambda *largs: f(*largs,**kwargs)

map(curry(pretty_format, fmt='%4.5f'), unformatted_list)






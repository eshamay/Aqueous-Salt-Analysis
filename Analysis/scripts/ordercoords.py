#!/Library/Frameworks/Python.framework/Versions/Current/bin/python
import sys

from OrderCoordAnalyzer import OrderCoord

#*******************Main******************************#
oc = OrderCoord(sys.argv[1])
#oc.OutputInfo()
oc.PlotData()


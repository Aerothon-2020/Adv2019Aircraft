from __future__ import division # let 5/2 = 2.5 rather than 2

#
# The following line turns off unit checking. Make sure things are working before it is turned off
#
from os import environ as _environ; _environ["scalar_off"] = "off"


import numpy as npy
import pylab as pyl
from scalar.units import FT, SEC, LBF, MIN, IN, ARCDEG
#from Aircraft_Models.Reg2013Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
#from Aircraft_40 import Aircraft
#from Aircraft_42 import Aircraft
#from Aircraft_44 import Aircraft
#from Aircraft_46 import Aircraft
#from Aircraft_48 import Aircraft
#from Aircraft_49 import Aircraft
#from Aircraft_50 import Aircraft
#from Aircraft_6413 import Aircraft
#from Aircraft_52 import Aircraft
#from Aircraft_55 import Aircraft

from Aircraft_100 import Aircraft
#from Aircraft_Models.Adv2014Aircraft_AeroCats.TradeStudies.LowMoment.Aircraft import Aircraft

#Aircraft.Draw(fig=2)       #commented out by Brock Pleiman
pyl.figure(1)

#
# Get the design point
#
dsgnGR = Aircraft.Groundroll() / (FT)
dsgnCR = Aircraft.Rate_of_Climb() / (FT/MIN)
pyl.plot([dsgnCR],[dsgnGR],'ro', markersize = 8)

#
# Set up ranges
#
S    = npy.linspace(906,1800,7)*IN**2
Span = npy.linspace(66,85,7)*IN

lgnd = ['Design W = %2.0f (lbf)' % (Aircraft.TotalWeight / LBF)]
arealist = []

# Initialize data arrays
grndroll = npy.zeros((len(Span),len(S)))
clmbrate = npy.zeros((len(Span),len(S)))

#
# Calculate the ground roll and climb rate
#
for ii in range(len(Span)):
    print "Calculating at Span = ", Span[ii]/IN
    for jj in range(len(S)):
        print "Calculating at S = ", S[jj]/IN**2
        Aircraft.Wing.S = S[jj]
        Aircraft.Wing.b = Span[ii]
        
        grndroll[ii][jj] = Aircraft.Groundroll() / (FT)
        clmbrate[ii][jj] = Aircraft.Rate_of_Climb() / (FT/MIN)
        
        print "Climb Rate = ", clmbrate[ii][jj]

#
# Plot the calculated values
#
for ii in range(len(Span)):
    clmplt = []
    grnplt = []
    for jj in range(len(S)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
        
    pyl.plot(clmplt,grnplt,ls = '--', lw = 2)        
    lgnd.append('b = %2.0f (in)' % (Span[ii] / IN))
    
for jj in range(len(S)):
    clmplt = []
    grnplt = []
    for ii in range(len(Span)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
    
    pyl.plot(clmplt,grnplt, lw = 2)        
    lgnd.append('S = %4.0f (in^2)' % (S[jj] / IN**2))

#lgnd.append('W = %2.0f (lbf)' % (Aircraft.TotalWeight / LBF))

pyl.plot()
pyl.axhline(y = 300, color = 'k', lw = 1)
pyl.axvline(x = 250, color = 'k', lw = 1)
pyl.title('Groundroll and Climb Rate for Varying Wing Area and Span')
pyl.xlabel('Climb Rate (ft/min)') ; pyl.ylabel('Groundroll (ft)')
pyl.legend(lgnd, loc = 'best', numpoints=1, labelspacing = 0.0)

pyl.show()
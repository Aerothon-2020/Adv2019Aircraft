from __future__ import division # let 5/2 = 2.5 rather than 2

#
# The following line turns off unit checking. Make sure things are working before it is turned off
#
from os import environ as _environ; _environ["scalar_off"] = "off"


import numpy as npy
import pylab as pyl
from scalar.units import FT, SEC, LBF, MIN, IN, ARCDEG
from Aircraft_Models.Adv2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
#from Aircraft_144 import Aircraft
#from Aircraft_148 import Aircraft
#from Aircraft_150 import Aircraft
#from Aircraft_152 import Aircraft
#from Aircraft_154 import Aircraft
#from Aircraft_155 import Aircraft
#from Aircraft_156 import Aircraft
#from Aircraft_158 import Aircraft
#from Aircraft_160 import Aircraft

#from Aircraft_Models.Reg2013Aircraft_AeroCats.MonoWing.AircraftGE import Aircraft
#from Aircraft_144GE import Aircraft
#from Aircraft_148GE import Aircraft
#from Aircraft_150GE import Aircraft
#from Aircraft_152GE import Aircraft
#from Aircraft_154GE import Aircraft
#from Aircraft_155GE import Aircraft
#from Aircraft_156GE import Aircraft
#from Aircraft_158GE import Aircraft


#from Aircraft_Models.Reg2013Aircraft_AeroCats.TradeStudies.LowMoment.Aircraft import Aircraft

Aircraft.Draw(fig=2)
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
S    = npy.linspace(1800,3200,4)*IN**2
TotalWeight = npy.linspace(27,30,5)*LBF

lgnd = ['Design W = %2.2f (lbf)' % (Aircraft.TotalWeight / LBF)]
arealist = []

# Initialize data arrays
grndroll = npy.zeros((len(TotalWeight),len(S)))
clmbrate = npy.zeros((len(TotalWeight),len(S)))

#
# Calculate the groundroll and climb rate
#
for ii in range(len(TotalWeight)):
    print "Calculating at TotalWeight = ", TotalWeight[ii]/LBF
    for jj in range(len(S)):
        print "Calculating at S = ", S[jj]/IN**2
        Aircraft.Wing.S = S[jj]
        Aircraft.TotalWeight = TotalWeight[ii]
        
        grndroll[ii][jj] = Aircraft.Groundroll() / (FT)
        clmbrate[ii][jj] = Aircraft.Rate_of_Climb() / (FT/MIN)
        
        print "Climb Rate = ", clmbrate[ii][jj]

#
# Plot the calculated values
#
for ii in range(len(TotalWeight)):
    clmplt = []
    grnplt = []
    for jj in range(len(S)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
        
    pyl.plot(clmplt,grnplt,ls = '--', lw = 2)        
    lgnd.append('TW = %2.2f (in)' % (TotalWeight[ii] / LBF))
    
for jj in range(len(S)):
    clmplt = []
    grnplt = []
    for ii in range(len(TotalWeight)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
    
    pyl.plot(clmplt,grnplt, lw = 2)        
    lgnd.append('S = %4.0f (in^2)' % (S[jj] / IN**2))

#lgnd.append('W = %2.0f (lbf)' % (Aircraft.TotalWeight / LBF))

pyl.plot()
pyl.axhline(y = 190, color = 'k', lw = 1)
pyl.axvline(x = 74.37, color = 'k', lw = 1)
#pyl.axvline(x = 100, color = 'k', lw = 1)
pyl.ylim(160,220)
pyl.xlim(65,100)
pyl.title('Groundroll and Climb Rate for Varying Wing Area and TotalWeight')
pyl.xlabel('Lift Off Climb Rate (ft/min)') ; pyl.ylabel('Groundroll (ft)')
pyl.legend(lgnd, loc = 'best', numpoints=1, labelspacing = 0.0)

pyl.show()
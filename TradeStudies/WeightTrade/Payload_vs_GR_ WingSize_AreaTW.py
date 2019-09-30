from __future__ import division # let 5/2 = 2.5 rather than 2

#
# The following line turns off unit checking. Make sure things are working before it is turned off
#
from os import environ as _environ; _environ["scalar_off"] = "off"


import numpy as npy
import pylab as pyl
from scalar.units import FT, SEC, LBF, MIN, IN, ARCDEG
from Aircraft_Models.Reg2013Aircraft_AeroCats.MonoWing.Aircraft import Aircraft

Aircraft.Draw(fig=2)
pyl.figure(1)

#
# Get the design point
#
dsgnPL = Aircraft.PayloadWeight() / (LBF)
dsgnGR = Aircraft.Groundroll() /(FT)
pyl.plot([dsgnPL],[dsgnGR],'ro', markersize = 8)

#
# Set up ranges
#
S    = npy.linspace(3400,3700,4)*IN**2
TotalWeight = npy.linspace(50,53.5,4)*LBF

lgnd = ['Design W = %2.2f (lbf)' % (Aircraft.TotalWeight / LBF)]
arealist = []

# Initialize data arrays
payload = npy.zeros((len(TotalWeight),len(S)))
grndrll = npy.zeros((len(TotalWeight),len(S)))

#
# Calculate the groundroll and climb rate
#
for ii in range(len(TotalWeight)):
    print "Calculating at TotalWeight = ", TotalWeight[ii]/LBF
    for jj in range(len(S)):
        print "Calculating at S = ", S[jj]/IN**2
        Aircraft.Wing.S = S[jj]
        Aircraft.TotalWeight = TotalWeight[ii]
        
        payload[ii][jj] = Aircraft.PayloadWeight() / (LBF)
        grndrll[ii][jj] = Aircraft.Groundroll() / (FT)
        
        print "Payload Weight = ", payload[ii][jj]

#
# Plot the calculated values
#
for ii in range(len(TotalWeight)):
    grplt = []
    payloadplt = []
    for jj in range(len(S)):
        grplt.append(grndrll[ii][jj])
        payloadplt.append(payload[ii][jj])
        
    pyl.plot(payloadplt,grplt,ls = '--', lw = 2)        
    lgnd.append('TW = %2.2f (in)' % (TotalWeight[ii] / LBF))
    
for jj in range(len(S)):
    grplt = []
    payloadplt = []
    for ii in range(len(TotalWeight)):
        grplt.append(grndrll[ii][jj])
        payloadplt.append(payload[ii][jj])
    
    pyl.plot(payloadplt,grplt, lw = 2)        
    lgnd.append('S = %4.0f (in^2)' % (S[jj] / IN**2))

#lgnd.append('W = %2.0f (lbf)' % (Aircraft.TotalWeight / LBF))

pyl.plot()
pyl.axhline(y = 190, color = 'k', lw = 1)
#pyl.axvline(x = 74.37, color = 'k', lw = 1)
#pyl.axvline(x = 100, color = 'k', lw = 1)
pyl.ylim(160,200)
pyl.xlim(38,44)
pyl.title('Payload and Ground Roll for Varying Wing Area and TotalWeight')
pyl.xlabel('Payload Weight (lbf)') ; pyl.ylabel('Ground Roll Distance (ft)')
pyl.legend(lgnd, loc = 'best', numpoints=1, labelspacing = 0.0)

pyl.show()
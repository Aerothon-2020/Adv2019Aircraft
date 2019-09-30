from __future__ import division # let 5/2 = 2.5 rather than 2

# import built-in modules
import os
import sys
import numpy as npy
import cmath as math
import pylab as pyl

from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, W, K, degR, inHg, MM
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name       = 'APC 22x12E'
Prop.D          = 22*IN
Prop.Thickness  = 0.5*IN

Prop.Pitch      = 12*IN
Prop.dAlpha     = 11*ARCDEG
Prop.Solidity   = 0.0126  

Prop.AlphaStall = 20*ARCDEG
Prop.AlphaZeroCL = 0*ARCDEG
Prop.CLSlope    = .065/ARCDEG   #- 2D airfoil lift slope
Prop.CDCurve    = 2.2          #- 2D curvature of the airfoil drag bucket
Prop.CDp        = .04          #- Parasitic drag

Prop.Weight     = 159.89*GRAM*gacc

Prop.ThrustUnit = LBF
Prop.ThrustUnitName = 'lbf'
Prop.PowerUnit = W 
Prop.PowerUnitName = 'watt' 
Prop.MaxTipSpeed = None
#
# These are corrected for standard day
#
#Second set of data taken - concern about first set since taken at night
#STD = STDCorrection(28.14*inHg, (294.16)*K)
Arm= 19.5

Prop.ThrustData = [(4250 *RPM, 209*OZF*Arm),
                   (4250 *RPM, 195.2*OZF*Arm)]# this point taken after initial points on Hacker A50. Used to verify good data.





################################################################################
if __name__ == '__main__':
   
    print " D     : ", AsUnit( Prop.D, 'in')
    print " Pitch : ", AsUnit( Prop.Pitch, 'in')
    
    Vmax = 50
    h = 0*FT
    N = npy.linspace(1000, 6800, 5)*RPM
    
    Alpha = npy.linspace(-25,25,41)*ARCDEG
    V     = npy.linspace(0,Vmax,30)*FT/SEC
    
    Prop.CoefPlot(Alpha,fig = 1)
    Prop.PTPlot(N,V,h,'V', fig = 2)
#
#    N = npy.linspace(0, 13000,31)*RPM
#    V = npy.linspace(0,Vmax,5)*FT/SEC
#
#    Prop.PTPlot(N,V,h,'N', fig = 3)
    Prop.PlotTestData(fig=4)

    N = 4250*RPM
    print
    print "Static Thrust   : ", AsUnit( Prop.T(N, 0*FT/SEC, h), 'lbf' )
    print "Measured Thrust : ", AsUnit( max(npy.array(Prop.ThrustData)[:,1]), 'lbf' )
    print
    print "Static Torque   : ", AsUnit( Prop.P(N, 0*FT/SEC, h)/N, 'in*ozf' )
  #  print "Measured Torque : ", AsUnit( max(npy.array(Prop.TorqueData)[:,1]), 'in*ozf' )
    
    pyl.show() 

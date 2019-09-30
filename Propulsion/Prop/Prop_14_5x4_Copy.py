from __future__ import division # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name       = 'Prop 14.2x4'
Prop.D          = 14.5*IN
Prop.Thickness  = 5/8*IN
#Prop.PitchAngle = 12*ARCDEG
Prop.Pitch      = 4.*IN
Prop.dAlpha     = 3.1*ARCDEG #0.8*ARCDEG
Prop.CLSlope    = .07/ARCDEG
Prop.Solidity   = 0.0102
Prop.RD         = 3/8
Prop.AlphaStall = 13*ARCDEG #13*ARCDEG
Prop.Weight     = 3/32*LBF

#
# These are corrected for standard day
#
#                 RPM,        Thrust
Prop.ThrustData = [(8100  *RPM, 4 *LBF + 8*OZF),
                   (9200  *RPM, 5 *LBF + 13*OZF),
                   (11200 *RPM, 9 *LBF + 3*OZF)]

#                   RPM,        Torque
Prop.TorqueData = [(11000 *RPM, 114.768*IN*OZF)]

################################################################################
if __name__ == '__main__':
    
    print "Max " + AsUnit(Prop.MaxRPM(), 'rpm', '%3.0f') + " at " + AsUnit(Prop.MaxTipSpeed, 'ft/s') + " tip speed ", 

    Vmax = 100
    h=0*FT
    N=npy.linspace(1000, 13000,4)*RPM
    
    Alpha = npy.linspace(-25,25,31)*ARCDEG
    V     = npy.linspace(0,Vmax,11)*FT/SEC
    
    #Prop.CoefPlot(Alpha,fig = 1)
    #Prop.PTPlot(N,V,h,'V', fig = 2)

    N = npy.linspace(0, 13000,31)*RPM
    V = npy.linspace(0,Vmax,5)*FT/SEC

    #Prop.PTPlot(N,V,h,'N', fig = 3)
    Prop.PlotTestData(fig=4)

    
    pyl.show()
from __future__ import division # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, Pa, degR, W, inHg, K
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name       = 'Prop 13.5x6'
Prop.D          = 13.5*IN
Prop.Thickness  = 5/8*IN
#Prop.PitchAngle = 12*ARCDEG
Prop.Pitch      = 6*IN
Prop.dAlpha     = 0.8*ARCDEG
Prop.Solidity   = 0.013   #0.0125 seems to match the old data better...
Prop.RD         = 3/8
Prop.AlphaStall = 16*ARCDEG
Prop.Weight     = 3/32*LBF

#
# These are corrected for standard day
#Standard correction for 2:00 pm for the test day
STD = STDCorrection(30.03*inHg, (19 + 273.15)*K)
#                  RPM,        Thrust
Prop.ThrustData = [(1726 *RPM, (1 *LBF + 10*OZF)*STD),
                   (3560 *RPM, (4 *LBF + 12*OZF)*STD),
                   (4600 *RPM, (6 *LBF + 5*OZF)*STD),
                   (4850 *RPM, (6 *LBF + 11*OZF)*STD)]

#Standard correction for 2:00 pm for the test day
#STD = STDCorrection(3003*3385*Pa, (19 + 273.15*9/5)*degR)

#                   RPM,        Torque
#Prop.TorqueData = [(11000 *RPM, 114.768*IN*OZF)]

################################################################################
if __name__ == '__main__':
    
    print "Max " + AsUnit(Prop.MaxRPM(), 'rpm', '%3.0f') + " at " + AsUnit(Prop.MaxTipSpeed, 'ft/s') + " tip speed ", 

    Vmax = 100
    h=0*FT
    N=npy.linspace(1000, 13000,4)*RPM
    
    Alpha = npy.linspace(-25,25,31)*ARCDEG
    V     = npy.linspace(0,Vmax,11)*FT/SEC
    
    Prop.CoefPlot(Alpha,fig = 1)
#    Prop.PTPlot(N,V,h,'V', fig = 2)

    N = npy.linspace(0, 13000,31)*RPM
    V = npy.linspace(0,Vmax,5)*FT/SEC

 #   Prop.PTPlot(N,V,h,'N', fig = 3)
    Prop.PlotTestData(fig=4)

    
    pyl.show()
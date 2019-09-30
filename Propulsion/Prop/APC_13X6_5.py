from __future__ import division # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, Pa, degR, W, inHg, K
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name       = 'APC 13x6_5'
Prop.D          = 13*IN
Prop.Thickness  = 5/8*IN

Prop.Pitch      = 6.5*IN
Prop.dAlpha     = 4.9*ARCDEG
Prop.Solidity   = 0.015

Prop.AlphaStall = 15*ARCDEG
Prop.CLSlope    = 0.065/ARCDEG
Prop.CDCurve    = 2.2
Prop.CDp        = 0.01

Prop.Weight     = 1.80*OZF

#


STD = STDCorrection(30.03*inHg, (19 + 273.15)*K)
#                  RPM,        Thrust
Prop.ThrustData = [(5000  *RPM, (1 *LBF + 5*OZF)*STD),
                   (6000  *RPM, (2 *LBF + 3*OZF)*STD),
                   (7000  *RPM, (2 *LBF + 8*OZF)*STD),
                   (8000  *RPM, (3 *LBF + 5*OZF)*STD),
                   (8700 *RPM,  (4 *LBF + 13*OZF)*STD)]

STD = STDCorrection(29.75*inHg, (17 + 273.15)*K)

Arm = 19.5*IN

#                   RPM,        Torque
Prop.TorqueData = [(12360 *RPM, (4.00*Arm*OZF)*STD),
                   (7050  *RPM, (1.40*Arm*OZF)*STD),
                   (9270  *RPM, (1.75*Arm*OZF)*STD),
                   (11280 *RPM, (3.10*Arm*OZF)*STD),
                   (12660 *RPM, (3.85*Arm*OZF)*STD),
                   (12540 *RPM, (4.70*Arm*OZF)*STD),
                   (5610  *RPM, (1.25*Arm*OZF)*STD),
                   (7650  *RPM, (1.60*Arm*OZF)*STD),
                   (8550 *RPM,  (2.20*Arm*OZF)*STD),
                   (11730 *RPM, (4.15*Arm*OZF)*STD),
                   (12330 *RPM, (4.55*Arm*OZF)*STD),
                   (11310 *RPM, (3.90*Arm*OZF)*STD),
                   (9900  *RPM, (2.90*Arm*OZF)*STD),
                   (8430 *RPM,  (2.25*Arm*OZF)*STD),
                   (7050 *RPM,  (1.45*Arm*OZF)*STD),
                   (4560 *RPM,  (.65*Arm*OZF)*STD),
                   (2700 *RPM,  (.30*Arm*OZF)*STD)]

################################################################################
if __name__ == '__main__':
    
    Vmax = 100
    h=0*FT
    N=npy.linspace(1000, 12300, 5)*RPM
    
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

    N = 12240*RPM
    print "Max " + AsUnit(Prop.MaxRPM(), 'rpm', '%3.0f') + " at " + AsUnit(Prop.MaxTipSpeed, 'ft/s') + " tip speed "
    print
    print "Static Thrust   : ", AsUnit( Prop.T(N, 0*FT/SEC, h), 'lbf' )
    print "Measured Thrust : ", AsUnit( max(npy.array(Prop.ThrustData)[:,1]), 'lbf' )
    N = 12660*RPM
    print
    print "Static Torque   : ", AsUnit( Prop.P(N, 0*FT/SEC, h)/N, 'in*ozf' )
    print "Measured Torque : ", AsUnit( max(npy.array(Prop.TorqueData)[:,1]), 'in*ozf' )
    
    pyl.show()

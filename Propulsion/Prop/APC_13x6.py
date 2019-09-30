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
Prop.Pitch      = 5.*IN
Prop.dAlpha     = 4.*ARCDEG
Prop.Solidity   = 0.014
Prop.RD         = 3/8
Prop.AlphaStall = 14*ARCDEG
Prop.CLSlope    = 0.07/ARCDEG

Prop.Weight     = 1.25*OZF

#
# These are corrected for standard day
STD = STDCorrection(30.03*inHg, (19 + 273.15)*K)

#                  RPM,        Thrust
Prop.ThrustData = [(3200  *RPM, (1 *LBF + 6*OZF)*STD),
                   (5610  *RPM, (3 *LBF + 2*OZF)*STD),
                   (7380  *RPM, (3 *LBF + 13*OZF)*STD),
                   (8640  *RPM, (5 *LBF + 7*OZF)*STD),
                   (9250  *RPM, (6 *LBF + 11*OZF)*STD),
                   (10320 *RPM, (7 *LBF + 3*OZF)*STD),
                   (10410 *RPM, (7 *LBF + 2*OZF)*STD),
                   (3600  *RPM, (1 *LBF + 2*OZF)*STD),
                   (4470  *RPM, (1 *LBF + 14*OZF)*STD),
                   (5580  *RPM, (2 *LBF + 10*OZF)*STD),
                   (6510  *RPM, (3 *LBF + 8*OZF)*STD),
                   (7470  *RPM, (4 *LBF + 5*OZF)*STD),
                   (8280 *RPM,  (5 *LBF + 5*OZF)*STD),
                   (8640 *RPM,  (5 *LBF + 14*OZF)*STD),
                   (9300  *RPM, (6 *LBF + 13*OZF)*STD),
                   (9690  *RPM, (7 *LBF + 0*OZF)*STD),
                   (9840  *RPM, (6 *LBF + 14*OZF)*STD),
                   (10140  *RPM, (7 *LBF + 4*OZF)*STD),
                   (10380 *RPM,  (7 *LBF + 3*OZF)*STD),
                   (10380 *RPM,  (7 *LBF + 1*OZF)*STD)]

#Standard correction for 2:00 pm for the test day
STD = STDCorrection(29.75*inHg, (17 + 273.15)*K)

Arm = 19.5*IN

#                   RPM,        Torque
Prop.TorqueData = [(10560 *RPM, (4.6*Arm*OZF)*STD),
                   (5670  *RPM, (.9*Arm*OZF)*STD),
                   (7800  *RPM, (2.35*Arm*OZF)*STD),
                   (9060  *RPM, (3.50*Arm*OZF)*STD),
                   (11130 *RPM, (4.25*Arm*OZF)*STD),
                   (10440 *RPM, (4.5*Arm*OZF)*STD),
                   (5670  *RPM, (1.35*Arm*OZF)*STD),
                   (7230  *RPM, (1.95*Arm*OZF)*STD),
                   (8250  *RPM, (2.35*Arm*OZF)*STD),
                   (9210 *RPM,  (3.40*Arm*OZF)*STD),
                   (10050 *RPM, (4.20*Arm*OZF)*STD),
                   (10410 *RPM, (4.55*Arm*OZF)*STD)]

################################################################################
if __name__ == '__main__':
    
    Vmax = 100
    h=0*FT
    N=npy.linspace(1000, 10500, 5)*RPM
    
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

    N = 10500*RPM
    print "Max " + AsUnit(Prop.MaxRPM(), 'rpm', '%3.0f') + " at " + AsUnit(Prop.MaxTipSpeed, 'ft/s') + " tip speed "
    print
    print "Static Thrust   : ", AsUnit( Prop.T(N, 0*FT/SEC, h), 'lbf' )
    print "Measured Thrust : ", AsUnit( max(npy.array(Prop.ThrustData)[:,1]), 'lbf' )
    print
    print "Static Torque   : ", AsUnit( Prop.P(N, 0*FT/SEC, h)/N, 'in*ozf' )
    print "Measured Torque : ", AsUnit( max(npy.array(Prop.TorqueData)[:,1]), 'in*ozf' )
    
    pyl.show()
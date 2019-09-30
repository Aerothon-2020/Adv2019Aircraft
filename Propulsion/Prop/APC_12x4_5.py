from __future__ import division # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, hPa, K, W, inHg
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name       = 'APC 12.2x4.5'
Prop.D          = 12.2*IN
Prop.Thickness  = 5/8*IN
#Prop.PitchAngle = 12*ARCDEG
Prop.Pitch      = 4.5*IN
Prop.dAlpha     = 3.4*ARCDEG
Prop.Solidity   = 0.0135
Prop.AlphaStall = 14*ARCDEG
Prop.CLSlope    = 0.072/ARCDEG

Prop.Weight     = 1.80*OZF

#
# These are corrected for standard day
#Standard correction for 2:00 pm for the test day
STD = STDCorrection(30.03*inHg, (19 + 273.15)*K)
#
#                  RPM,        Thrust
Prop.ThrustData = [(3750  *RPM, (0 *LBF + 14*OZF)*STD),
                   (6210  *RPM, (2 *LBF + 4*OZF)*STD),
                   (7830  *RPM, (1 *LBF + 15*OZF)*STD),
                   (8160  *RPM, (4 *LBF + 4*OZF)*STD),
                   (9090  *RPM, (4 *LBF + 14*OZF)*STD),
                   (10110 *RPM, (4 *LBF + 10*OZF)*STD),
                   (11190 *RPM, (6 *LBF + 4*OZF)*STD),
                   (11670 *RPM, (7 *LBF + 4*OZF)*STD),
                   (12060 *RPM, (7 *LBF + 8*OZF)*STD),
                   (12270 *RPM, (8 *LBF + 7*OZF)*STD),
                   (12570 *RPM, (8 *LBF + 13*OZF)*STD),
                   (13110 *RPM, (9 *LBF + 1*OZF)*STD),
                   (2880  *RPM, (0 *LBF + 8*OZF)*STD),
                   (5250  *RPM, (1 *LBF + 13*OZF)*STD),
                   (6120  *RPM, (2 *LBF + 3*OZF)*STD),
                   (6840  *RPM, (1 *LBF + 14*OZF)*STD),
                   (7680  *RPM, (2 *LBF + 12*OZF)*STD),
                   (8520 *RPM,  (4 *LBF + 10*OZF)*STD),
                   (9090 *RPM,  (4 *LBF + 5*OZF)*STD),
                   (9870 *RPM,  (4 *LBF + 8*OZF)*STD),
                   (10410 *RPM, (4 *LBF + 9*OZF)*STD),
                   (11370 *RPM, (6 *LBF + 9*OZF)*STD),
                   (12120 *RPM, (7 *LBF + 3*OZF)*STD),
                   (12360 *RPM, (7 *LBF + 11*OZF)*STD)]

#Prop.ThrustData += ThrustData

STD = STDCorrection(30.34*inHg, (15.55 + 273.15)*K)


ThrustData = [(5000  *RPM, (1 *LBF +  2*OZF)*STD),
              (6000  *RPM, (1 *LBF +  13*OZF)*STD),
              (7000  *RPM, (2 *LBF + 3*OZF)*STD),
              (8000  *RPM, (2 *LBF +  13*OZF)*STD),
              (9000 *RPM,  (3 *LBF +  11*OZF)*STD),
              (10000 *RPM, (4 *LBF + 7*OZF)*STD),
              (11000 *RPM, (5 *LBF +  8*OZF)*STD),
              (12000 *RPM, (6 *LBF +  10*OZF)*STD),
              (12630 *RPM, (8 *LBF +  2*OZF)*STD)]

Prop.ThrustData += ThrustData

#Standard correction for 2:00 pm for the test day
STD = STDCorrection(29.75*inHg, (17 + 273.15)*K)

Arm = 19.5*IN

#                   RPM,        Torque
Prop.TorqueData = [(12390 *RPM, (3.65*Arm*OZF)*STD),
                   (7950  *RPM, (1.40*Arm*OZF)*STD),
                   (9270  *RPM, (1.75*Arm*OZF)*STD),
                   (11280 *RPM, (3.10*Arm*OZF)*STD),
                   (12660 *RPM, (3.85*Arm*OZF)*STD),
                   (12660 *RPM, (4.25*Arm*OZF)*STD),
                   (5570  *RPM, (1.00*Arm*OZF)*STD),
                   (7920  *RPM, (1.35*Arm*OZF)*STD),
                   (9120 *RPM,  (2.05*Arm*OZF)*STD),
                   (11370 *RPM, (3.20*Arm*OZF)*STD),
                   (12030 *RPM, (3.80*Arm*OZF)*STD),
                   (12360 *RPM, (4.25*Arm*OZF)*STD)]

################################################################################
if __name__ == '__main__':
    
    Vmax = 100
    h=0*FT
    N=npy.linspace(1000, 13200, 5)*RPM
    
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

    N = 13200*RPM
    print "Max " + AsUnit(Prop.MaxRPM(), 'rpm', '%3.0f') + " at " + AsUnit(Prop.MaxTipSpeed, 'ft/s') + " tip speed "
    print
    print "Static Thrust   : ", AsUnit( Prop.T(N, 0*FT/SEC, h), 'lbf' )
    print "Measured Thrust : ", AsUnit( max(npy.array(Prop.ThrustData)[:,1]), 'lbf' )
    print
    print "Static Torque   : ", AsUnit( Prop.P(N, 0*FT/SEC, h)/N, 'in*ozf' )
    print "Measured Torque : ", AsUnit( max(npy.array(Prop.TorqueData)[:,1]), 'in*ozf' )

    
    pyl.show()
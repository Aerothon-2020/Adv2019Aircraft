from __future__ import division # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, hPa, K, W, inHg
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name        = 'Graupner 14.2x4'
Prop.D           = 14.2*IN
Prop.Thickness   = 5/8*IN
#Prop.PitchAngle  = 12*ARCDEG
Prop.Pitch       = 4*IN
Prop.dAlpha      = 0*ARCDEG
Prop.Solidity    = 0.013
Prop.RD          = 3/8
Prop.AlphaStall  = 15*ARCDEG
Prop.AlphaZeroCL = 0*ARCDEG
Prop.CLSlope     = 0.07/ARCDEG  #- 2D airfoil lift slope (default 0.068/deg)
Prop.CDp         = 0.01

Prop.Weight      = 1.95*OZF

#
# These are corrected for standard day
#Standard correction for 2:00 pm for the test day
STD = STDCorrection(30.03*inHg, (19 + 273.15)*K)
#
#                  RPM,        Thrust
Prop.ThrustData = [(4020  *RPM, (0 *LBF +  8*OZF)*STD),
                   (5640  *RPM, (0 *LBF +  10*OZF)*STD),
                   (7860  *RPM, (2 *LBF +  1*OZF)*STD),
                   (9150  *RPM, (6 *LBF +  7*OZF)*STD),
                   (9900 *RPM,  (7 *LBF +  9*OZF)*STD),
                   (10890 *RPM, (9 *LBF +  2*OZF)*STD),
                   (11130 *RPM, (9 *LBF +  11*OZF)*STD),
                   (10320 *RPM,  (8 *LBF +  1*OZF)*STD),
                   (9870  *RPM, (7 *LBF +  0*OZF)*STD),
                   (9030  *RPM, (5 *LBF +  3*OZF)*STD)]
                   #(3150  *RPM, (1 *LBF +  7*OZF)*STD)
                  


STD = STDCorrection(30.3*inHg, (19 + 273.15)*K)


ThrustData = [(3270  *RPM, (0 *LBF +  10*OZF)*STD),
              (6030  *RPM, (2 *LBF +  12*OZF)*STD),
              (7140  *RPM, (4 *LBF + 3*OZF)*STD),
              (8340  *RPM, (5 *LBF +  14*OZF)*STD),
              (9390 *RPM,  (6 *LBF +  12*OZF)*STD),
              (10140 *RPM, (7 *LBF + 8*OZF)*STD),
              (10590 *RPM, (9 *LBF +  2*OZF)*STD),
              (11100 *RPM, (9 *LBF +  9*OZF)*STD)]

Prop.ThrustData += ThrustData

Arm = 19.5*IN*OZF

#                   RPM,        Torque
Prop.TorqueData = [(11400 *RPM,  (5.00*Arm)*STD),
                   (6660 *RPM,  (1.10*Arm)*STD),
                   (7800 *RPM,  (1.85*Arm)*STD),
                   (9990 *RPM,  (3.30*Arm)*STD),
                   (10980 *RPM, (4.25*Arm)*STD),
                   (11100 *RPM, (4.90*Arm)*STD),
                   (10380 *RPM, (4.25*Arm)*STD),
                   (9030 *RPM,  (3.05*Arm)*STD),
                   (8040 *RPM,  (2.25*Arm)*STD),
                   (6390 *RPM,  (1.35*Arm)*STD),
                   (3690 *RPM,  (.40*Arm)*STD)]

################################################################################
if __name__ == '__main__':
    
    Vmax = 100
    h=0*FT
    N=npy.linspace(1000, 12000, 5)*RPM
    
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

    
    N = 11400*RPM
    print "Max " + AsUnit(Prop.MaxRPM(), 'rpm', '%3.0f') + " at " + AsUnit(Prop.MaxTipSpeed, 'ft/s') + " tip speed "
    print
    print "Static Thrust   : ", AsUnit( Prop.T(N, 0*FT/SEC, h), 'lbf' )
    print "Measured Thrust : ", AsUnit( max(npy.array(Prop.ThrustData)[:,1]), 'lbf' )
    print
    print "Static Torque   : ", AsUnit( Prop.P(N, 0*FT/SEC, h)/N, 'in*ozf' )
    print "Measured Torque : ", AsUnit( max(npy.array(Prop.TorqueData)[:,1]), 'in*ozf' )

    
    pyl.show()
from __future__ import division # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, hPa, K, W, inHg
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name        = 'APC 14x4'
Prop.D           = 14*IN
Prop.Thickness   = 5/8*IN
#Prop.PitchAngle  = 12*ARCDEG
Prop.Pitch       = 4*IN

Prop.dAlpha      = 3.7*ARCDEG
Prop.Solidity    = 0.014
Prop.AlphaStall  = 15*ARCDEG
Prop.AlphaZeroCL = 0*ARCDEG
Prop.CLSlope     = 0.0725/ARCDEG  #- 2D airfoil lift slope (default 0.068/deg)
Prop.CDp         = 0.01

Prop.Weight      = 1.8*OZF

#
# These are corrected for standard day
#Standard correction for 2:00 pm for the test day
STD = STDCorrection(30.34*inHg, (15.55 + 273.15)*K)
#
#                  RPM,        Thrust
Prop.ThrustData = [(5000  *RPM, (1 *LBF +  4*OZF)*STD),
                   (6000  *RPM, (2 *LBF +  9*OZF)*STD),
                   (7000  *RPM, (3 *LBF + 12*OZF)*STD),
                   (8000  *RPM, (5 *LBF +  8*OZF)*STD),
                   (9120 *RPM, (8 *LBF +  11*OZF)*STD)]
                  


STD = STDCorrection(29.75*inHg, (17 + 273.15)*K)

Arm = 19.5*IN*OZF

#                   RPM,        Torque
Prop.TorqueData = [(10950 *RPM, (4.50*Arm)*STD),
                   (5730 *RPM,  (1.30*Arm)*STD),
                   (9330 *RPM,  (3.25*Arm)*STD),
                   (10860 *RPM, (4.45*Arm)*STD),
                   (10950 *RPM, (4.60*Arm)*STD),
                   (11160 *RPM, (4.70*Arm)*STD),
                   (6060 *RPM,  (1.05*Arm)*STD),
                   (7920 *RPM,  (2.15*Arm)*STD),
                   (9150 *RPM,  (3.05*Arm)*STD),
                   (10440 *RPM, (4.20*Arm)*STD),
                   (10920 *RPM, (4.65*Arm)*STD),
                   (10320 *RPM, (4.00*Arm)*STD),
                   (8880 *RPM,  (2.90*Arm)*STD),
                   (7620 *RPM,  (1.90*Arm)*STD),
                   (5100 *RPM,  (.75*Arm)*STD),
                   (3210 *RPM,  (.10*Arm)*STD)]

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

    N = 12000*RPM
    print "Max " + AsUnit(Prop.MaxRPM(), 'rpm', '%3.0f') + " at " + AsUnit(Prop.MaxTipSpeed, 'ft/s') + " tip speed "
    print
    print "Static Thrust   : ", AsUnit( Prop.T(N, 0*FT/SEC, h), 'lbf' )
    print "Measured Thrust : ", AsUnit( max(npy.array(Prop.ThrustData)[:,1]), 'lbf' )
    print
    print "Static Torque   : ", AsUnit( Prop.P(N, 0*FT/SEC, h)/N, 'in*ozf' )
    print "Measured Torque : ", AsUnit( max(npy.array(Prop.TorqueData)[:,1]), 'in*ozf' )
    
    pyl.show()
from __future__ import division # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, hPa, K, W, inHg
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name        = 'APC 12.25x3.75'
Prop.D           = 12.25*IN
Prop.Thickness   = 5/8*IN

Prop.Pitch       = 3.75*IN
Prop.dAlpha      = 6.25*ARCDEG
Prop.Solidity    = 0.012

Prop.AlphaStall  = 18*ARCDEG
Prop.AlphaZeroCL = 0*ARCDEG     #- 2D curvature of the airfoil drag bucket
Prop.CLSlope     = 0.09/ARCDEG  #- 2D airfoil lift slope (default 0.068/deg)
Prop.CDCurve     = 2.5          #- 2D curvature of the airfoil drag bucket
Prop.CDp         = 0.01         #- 2D parasite drag

Prop.Weight      = 1.80*OZF
Prop.WeightGroup = 'Propulsion'

#
# These are corrected for standard day
#Standard correction for 2:00 pm for the test day
STD = STDCorrection(30.03*inHg, (19 + 273.15)*K)
#
#                  RPM,        Thrust
Prop.ThrustData = [(4110  *RPM, (1 *LBF +  0*OZF)*STD),
                   (7770  *RPM, (2 *LBF +  8*OZF)*STD),
                   (8850  *RPM, (3 *LBF + 10*OZF)*STD),
                   (9750  *RPM, (4 *LBF +  8*OZF)*STD),
                   (9960 *RPM,  (4 *LBF +  9*OZF)*STD),
                   (10950 *RPM, (5 *LBF + 12*OZF)*STD),
                   (11610 *RPM, (6 *LBF +  9*OZF)*STD),
                   (11910 *RPM, (7 *LBF +  13*OZF)*STD),
                   (12330  *RPM,(8 *LBF +  8*OZF)*STD),
                   (12780  *RPM, (9 *LBF +  7*OZF)*STD),
                   (12870  *RPM, (9 *LBF +  13*OZF)*STD),
                   (12900 *RPM,  (9 *LBF +  15*OZF)*STD)]
                  
STD = STDCorrection(30.3*inHg, (19 + 273.15)*K)


ThrustData = [(3510  *RPM, (0 *LBF +  12*OZF)*STD),
              (5010  *RPM, (1 *LBF +  7*OZF)*STD),
              (6660  *RPM, (2 *LBF + 9*OZF)*STD),
              (6810  *RPM, (2 *LBF +  12*OZF)*STD),
              (7830 *RPM,  (3 *LBF +  5*OZF)*STD),
              (9360 *RPM, (4 *LBF + 2*OZF)*STD),
              (10410 *RPM, (5 *LBF +  3*OZF)*STD),
              (11340 *RPM, (6 *LBF +  14*OZF)*STD),
              (13500  *RPM,(10 *LBF +  3*OZF)*STD),
              (12210  *RPM, (8 *LBF +  15*OZF)*STD),
              (13410  *RPM, (9 *LBF +  14*OZF)*STD)]

Prop.ThrustData += ThrustData

STD = STDCorrection(30.29*inHg, (16.66 + 273.15)*K)


ThrustData = [(4700  *RPM, (1 *LBF +  2*OZF)*STD),
              (7600  *RPM, (2 *LBF +  15*OZF)*STD),
              (8000  *RPM, (3 *LBF + 12*OZF)*STD),
              (9500  *RPM, (4 *LBF +  4*OZF)*STD),
              (10000 *RPM,  (5 *LBF +  3*OZF)*STD),
              (11400 *RPM, (6 *LBF + 9*OZF)*STD),
              (12000 *RPM, (7 *LBF +  10*OZF)*STD),
              (13260 *RPM, (9 *LBF +  12*OZF)*STD)]

Prop.ThrustData += ThrustData

STD = STDCorrection(30.45*inHg, (8.88 + 273.15)*K)


ThrustData = [  (11500 *RPM, (6 *LBF + 3 *OZF)*STD),
                (11900 *RPM, (6 *LBF + 1 *OZF)*STD),
                (12600 *RPM, (7 *LBF + 4 *OZF)*STD),
                (13000 *RPM, (8 *LBF + 5 *OZF)*STD),
                (13320 *RPM, (8 *LBF + 9 *OZF)*STD),
                (13020 *RPM, (8 *LBF + 0 *OZF)*STD),
                (12720 *RPM, (7 *LBF + 8 *OZF)*STD),
                (12300 *RPM, (6 *LBF + 14 *OZF)*STD),
                (11550 *RPM, (6 *LBF + 1 *OZF)*STD),
                (10440 *RPM, (5 *LBF + 2 *OZF)*STD),
                (9510 *RPM, (4 *LBF + 3 *OZF)*STD),
                (8160 *RPM, (3 *LBF + 1 *OZF)*STD),
                (8010 *RPM, (3 *LBF + 3 *OZF)*STD),
                (10710 *RPM, (5 *LBF + 7 *OZF)*STD),
                (11370 *RPM, (6 *LBF + 1 *OZF)*STD),
                (11610 *RPM, (6 *LBF + 13 *OZF)*STD),
                (11900 *RPM, (6 *LBF + 14 *OZF)*STD),
                (12300 *RPM, (7 *LBF + 12 *OZF)*STD),
                (12660 *RPM, (7 *LBF + 14 *OZF)*STD),
                (12450 *RPM, (7 *LBF + 5 *OZF)*STD),
                (11550 *RPM, (6 *LBF + 2 *OZF)*STD),
                (10890 *RPM, (5 *LBF + 12 *OZF)*STD),
                (10350 *RPM, (5 *LBF + 0 *OZF)*STD),
                (9850 *RPM, (4 *LBF + 8 *OZF)*STD),]

Prop.ThrustData = ThrustData

STD = STDCorrection(29.48*inHg, 280.372*K)


ThrustData = [  (12960 *RPM, (9 *LBF + 0 *OZF)*STD),
                (12870 *RPM, (9 *LBF + 0 *OZF)*STD),
                (12400 *RPM, (8 *LBF + 0 *OZF)*STD),
                (11370 *RPM, (6 *LBF + 9 *OZF)*STD),
                (10800 *RPM, (6 *LBF + 2 *OZF)*STD),
                (9540  *RPM, (4 *LBF + 10 *OZF)*STD),
                (8670  *RPM, (3 *LBF + 11 *OZF)*STD),
                (8000  *RPM, (3 *LBF + 3  *OZF)*STD),
                (13100 *RPM, (9 *LBF + 4 *OZF)*STD),
                (13020 *RPM, (9 *LBF + 2 *OZF)*STD),
                (12930 *RPM, (8 *LBF + 14 *OZF)*STD),
                (12060 *RPM, (7 *LBF + 11 *OZF)*STD),
                (11070 *RPM, (6 *LBF + 2 *OZF)*STD),
                (8700  *RPM, (3 *LBF + 13 *OZF)*STD),
                (7260  *RPM, (2 *LBF + 7 *OZF)*STD),
                (5100  *RPM, (1 *LBF + 3 *OZF)*STD),
                ]

Prop.ThrustData = ThrustData

#
# Dynamic thust data
#
STD = STDCorrection(29.2*inHg, (10 + 273.15)*K)

# This is garbage data. Delete this when the data is not garbage
#            RPM,        Thrust,     Velocity
DynThrustData = [(13050  *RPM, (9 *LBF +  13*OZF)*STD, 0*FT/SEC),
                 (14070  *RPM, (8 *LBF +  3*OZF)*STD, 36.66666*FT/SEC),
                 (14150  *RPM, (7 *LBF +  1*OZF)*STD, 44*FT/SEC),
                 (14380  *RPM, (6 *LBF +  14*OZF)*STD, 58.66666*FT/SEC),
                 (14670  *RPM, (6 *LBF +  5*OZF)*STD, 66*FT/SEC),
                 (15200  *RPM, (6 *LBF + 1*OZF)*STD, 73.33333*FT/SEC) ]

Prop.DynThrustData = DynThrustData



#Static torque

STD = STDCorrection(29.75*inHg, (17 + 273.15)*K)

Arm = 19.5*IN*OZF

#                   RPM,        Torque
Prop.TorqueData = [(13110 *RPM, (4.50*Arm)*STD),
                   (6990 *RPM,  (1.00*Arm)*STD),
                   (8520 *RPM,  (2.00*Arm)*STD),
                   (11430 *RPM, (3.90*Arm)*STD),
                   (12360 *RPM, (3.95*Arm)*STD),
                   (12510 *RPM, (4.10*Arm)*STD),
                   (10950 *RPM, (2.80*Arm)*STD),
                   (8730 *RPM,  (1.85*Arm)*STD),
                   (6600 *RPM,  (.85*Arm)*STD),
                   (4740 *RPM,  (.35*Arm)*STD)]

STD = STDCorrection(29.63*inHg, (12.4 + 273.15)*K)

Arm = 19.5*IN*OZF

#                   RPM,        Torque
Prop.TorqueData = [(3240 *RPM, (0.25*Arm)*STD),
                   (4290 *RPM,  (0.55*Arm)*STD),
                   (5370 *RPM,  (0.8*Arm)*STD),
                   (6270 *RPM, (1.05*Arm)*STD),
                   (6630 *RPM, (1.2*Arm)*STD),
                   (7380 *RPM, (1.45*Arm)*STD),
                   (8610 *RPM, (1.95*Arm)*STD),
                   (9960 *RPM,  (2.55*Arm)*STD),
                   (10920 *RPM,  (3.1*Arm)*STD),
                   (11760 *RPM,  (3.7*Arm)*STD),
                   (12350 *RPM,  (3.95*Arm)*STD),
                   (12720 *RPM, (4.35*Arm)*STD),
                   (13010 *RPM, (4.5*Arm)*STD),
                   (13170 *RPM, (4.7*Arm)*STD),
                   (11340 *RPM, (3.4*Arm)*STD),
                   (10710 *RPM,  (3.1*Arm)*STD),
                   (9450 *RPM,  (2.2*Arm)*STD),
                   (8670 *RPM,  (1.95*Arm)*STD),
                   (8010 *RPM,  (1.65*Arm)*STD),
                   (7440 *RPM, (1.4*Arm)*STD),
                   (6810 *RPM, (1.15*Arm)*STD),
                   (5790 *RPM, (0.75*Arm)*STD),
                   (3870 *RPM, (0.4*Arm)*STD),
                   (3210 *RPM,  (0.25*Arm)*STD)]

################################################################################
if __name__ == '__main__':
    
    Vmax = 100
    h=0*FT
    N=npy.linspace(1000, 13000, 5)*RPM
    
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

    N = 12900*RPM
    print "Max " + AsUnit(Prop.MaxRPM(), 'rpm', '%3.0f') + " at " + AsUnit(Prop.MaxTipSpeed, 'ft/s') + " tip speed "
    print
    print "Static Thrust   : ", AsUnit( Prop.T(N, 0*FT/SEC, h), 'lbf' )
    print "Measured Thrust : ", AsUnit( max(npy.array(Prop.ThrustData)[:,1]), 'lbf' )
    N = 13110*RPM
    print
    print "Static Torque   : ", AsUnit( Prop.P(N, 0*FT/SEC, h)/N, 'in*ozf' )
    print "Measured Torque : ", AsUnit( max(npy.array(Prop.TorqueData)[:,1]), 'in*ozf' )
    
    pyl.show()

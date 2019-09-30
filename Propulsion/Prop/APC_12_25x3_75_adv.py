from __future__ import division # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, hPa, K, W, inHg
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name        = 'APC 12.25x3.75 ADV'
Prop.D           = 12.25*IN
Prop.Thickness   = 5/8*IN

Prop.Pitch       = 3.75*IN
Prop.dAlpha      = 6.25*ARCDEG  # for correlating
Prop.Solidity    = 0.013        # for correlating

Prop.AlphaStall  = 18*ARCDEG    # for correlating
Prop.AlphaZeroCL = 0*ARCDEG     #- 2D curvature of the airfoil drag bucket
Prop.CLSlope     = 0.095/ARCDEG  #- 2D airfoil lift slope (default 0.068/deg)
Prop.CDCurve     = 2.5          #- 2D curvature of the airfoil drag bucket
Prop.CDp         = 0.01         #- 2D parasite drag

Prop.Weight      = 1.80*OZF
Prop.WeightGroup = 'Propulsion'

#
# These are corrected for standard day
#Standard correction for 2:00 pm for the test day
#STD = STDCorrection(30.16*inHg, (1.6667 + 273.15)*K)
#
#                  RPM,        Thrust
#Prop.ThrustData = [(13440 *RPM, (10 *LBF + 8*OZF)*STD),
#                   (12340 *RPM, (10 *LBF + 5*OZF)*STD),
#                   (11750 *RPM, (9 *LBF + 0 *OZF)*STD),
#                   (10650 *RPM, (8 *LBF + 6 *OZF)*STD),
#                   (10500 *RPM, (6 *LBF + 12*OZF)*STD),
#                   (10180 *RPM, (6 *LBF + 0 *OZF)*STD),
#                   (9630  *RPM, (5 *LBF + 6 *OZF)*STD),
#                   (8025  *RPM, (4 *LBF + 3 *OZF)*STD),
#                   (7290  *RPM, (3 *LBF + 4 *OZF)*STD),
#                   (4070  *RPM, (2 *LBF + 6 *OZF)*STD),
#                   (2840  *RPM, (1 *LBF + 3 *OZF)*STD),]

#Prop.ThrustData += ThrustData

#STD = STDCorrection(30.29*inHg, (16.66 + 273.15)*K)


#ThrustData = [(4700  *RPM, (1 *LBF +  2*OZF)*STD),
#              (7600  *RPM, (2 *LBF +  15*OZF)*STD),
#              (8000  *RPM, (3 *LBF + 12*OZF)*STD),]

#Prop.ThrustData += ThrustData

#STD = STDCorrection(30.45*inHg, (8.88 + 273.15)*K)


#ThrustData = [  (11500 *RPM, (6 *LBF + 3 *OZF)*STD),
#                (11900 *RPM, (6 *LBF + 1 *OZF)*STD),
#                (12600 *RPM, (7 *LBF + 4 *OZF)*STD),
#                (13000 *RPM, (8 *LBF + 5 *OZF)*STD),
#                (13320 *RPM, (8 *LBF + 9 *OZF)*STD),]

#Prop.ThrustData = ThrustData

#STD = STDCorrection(29.48*inHg, 280.372*K)


#ThrustData = [  (12960 *RPM, (9 *LBF + 0 *OZF)*STD),
#                (12870 *RPM, (9 *LBF + 0 *OZF)*STD),
#                (12400 *RPM, (8 *LBF + 0 *OZF)*STD),]

#Prop.ThrustData = ThrustData

#
# Dynamic thust data
#
#STD = STDCorrection(29.2*inHg, (10 + 273.15)*K)

# This is garbage data. Delete this when the data is not garbage
#            RPM,        Thrust,     Velocity
#DynThrustData = [(13050  *RPM, (9 *LBF +  13*OZF)*STD, 0*FT/SEC),
#                 (14070  *RPM, (8 *LBF +  3*OZF)*STD, 36.66666*FT/SEC),
#                 (14150  *RPM, (7 *LBF +  1*OZF)*STD, 44*FT/SEC),
#                 (14380  *RPM, (6 *LBF +  14*OZF)*STD, 58.66666*FT/SEC),
#                 (14670  *RPM, (6 *LBF +  5*OZF)*STD, 66*FT/SEC),
#                 (15200  *RPM, (6 *LBF + 1*OZF)*STD, 73.33333*FT/SEC) ]

#Prop.DynThrustData = DynThrustData



#Static torque

#STD = STDCorrection(29.75*inHg, (17 + 273.15)*K)

#Arm = 19.5*IN*OZF

#                   RPM,        Torque
#Prop.TorqueData = [(13110 *RPM, (4.50*Arm)*STD),
#                   (6990 *RPM,  (1.00*Arm)*STD),
#                   (8520 *RPM,  (2.00*Arm)*STD),]

#STD = STDCorrection(29.63*inHg, (12.4 + 273.15)*K)
#Arm = 19.5*IN*OZF

#                   RPM,        Torque
#Prop.TorqueData = [(3240 *RPM, (0.25*Arm)*STD),
#                   (4290 *RPM,  (0.55*Arm)*STD),
#                   (5370 *RPM,  (0.8*Arm)*STD),
#                   (6270 *RPM, (1.05*Arm)*STD),]

#STD = STDCorrection(30.32*inHg, (16.1 + 273.15)*K)

#Arm = 19.5*IN

#                   RPM,        Torque
#Prop.TorqueData = [(4290 *RPM, (0.03*Arm*LBF)*STD),
#                   (5790 *RPM, (0.05*Arm*LBF)*STD),
#                   (6330 *RPM, (0.07*Arm*LBF)*STD),
#                   (7650 *RPM, (0.09*Arm*LBF)*STD),
#                   (9220 *RPM, (0.13*Arm*LBF)*STD),
 #                  (11920 *RPM, (0.24*Arm*LBF)*STD),
 #                  (12750 *RPM, (0.28*Arm*LBF)*STD),
#                   (13600 *RPM, (0.32*Arm*LBF)*STD),
#                   (13800 *RPM, (0.34*Arm*LBF)*STD)]
################################################################################
# Marietta GA
STD = STDCorrection(30.3*inHg, (21.1 + 273.15)*K)
#                  RPM,        Thrust
Prop.ThrustData = [(13440 *RPM, (10 *LBF + 8*OZF)*STD),
                   (12340 *RPM, (10 *LBF + 5*OZF)*STD),
                   (11750 *RPM, (9 *LBF + 0 *OZF)*STD),
                   (10650 *RPM, (8 *LBF + 6 *OZF)*STD),
                   (10500 *RPM, (6 *LBF + 12*OZF)*STD),
                   (10180 *RPM, (6 *LBF + 0 *OZF)*STD),
                   (9630  *RPM, (5 *LBF + 6 *OZF)*STD),
                   (8025  *RPM, (4 *LBF + 3 *OZF)*STD),
                   (7290  *RPM, (3 *LBF + 4 *OZF)*STD),
                   (4070  *RPM, (2 *LBF + 6 *OZF)*STD),
                   (2840  *RPM, (1 *LBF + 3 *OZF)*STD),]

STD = STDCorrection(30.3*inHg, (21.1 + 273.15)*K)

Arm = 19.5*IN

#                   RPM,        Torque
Prop.TorqueData = [(4290 *RPM, (0.03*Arm*LBF)*STD),
                   (5790 *RPM, (0.05*Arm*LBF)*STD),
                   (6330 *RPM, (0.07*Arm*LBF)*STD),
                   (7650 *RPM, (0.09*Arm*LBF)*STD),
                   (9220 *RPM, (0.13*Arm*LBF)*STD),
                   (11920 *RPM, (0.24*Arm*LBF)*STD),
                   (12750 *RPM, (0.28*Arm*LBF)*STD),
                   (13600 *RPM, (0.32*Arm*LBF)*STD),
                   (13800 *RPM, (0.34*Arm*LBF)*STD)]
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

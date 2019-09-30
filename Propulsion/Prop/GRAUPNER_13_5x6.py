from __future__ import division # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, Pa, degR, W, inHg, K
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name        = 'Graupner 13.5x6' #This is a Santiago especial
Prop.D           = 13.5*IN
Prop.Thickness   = 5/8*IN

Prop.Pitch       = 6*IN
Prop.dAlpha      = 3.7*ARCDEG
Prop.Solidity    = 0.0135

Prop.AlphaStall  = 15*ARCDEG
Prop.AlphaZeroCL = 0*ARCDEG
Prop.CLSlope     = 0.08/ARCDEG 
Prop.CDCurve     = 2.3
Prop.CDp         = 0.01

Prop.Weight      = 100*LBF

#
# These are corrected for standard day
#Standard correction for 2:00 pm for the test day
STD = STDCorrection(30.03*inHg, (19 + 273.15)*K)
#
#                  RPM,        Thrust
Prop.ThrustData = [(4560  *RPM, (2 *LBF + 13*OZF)*STD),
                   #(13500 *RPM, (9 *LBF + 3*OZF)*STD),
                   (5760  *RPM, (3 *LBF + 7*OZF)*STD),
                   (6900  *RPM, (4 *LBF + 5*OZF)*STD),
                   (7890  *RPM, (4 *LBF + 9*OZF)*STD),
                   (9300  *RPM, (7 *LBF + 6*OZF)*STD),
                   (9450  *RPM, (7 *LBF + 12*OZF)*STD),
                   (8200  *RPM, (6 *LBF + 5*OZF)*STD),
                   (4230  *RPM, (2 *LBF + 0*OZF)*STD),
                   (5430  *RPM, (2 *LBF + 12*OZF)*STD),
                   (6390  *RPM, (3 *LBF + 15*OZF)*STD),
                   (7200  *RPM, (4 *LBF + 4*OZF)*STD),
                   (8010  *RPM, (5 *LBF + 7*OZF)*STD),
                   (8400  *RPM, (6 *LBF + 0*OZF)*STD),
                   (8700  *RPM, (7 *LBF + 3*OZF)*STD),
                   (6940  *RPM, (7 *LBF + 4*OZF)*STD),
                   (9180  *RPM, (7 *LBF + 5*OZF)*STD),
                   (9420  *RPM, (7 *LBF + 11*OZF)*STD),
                   (9630  *RPM, (8 *LBF + 7*OZF)*STD),
                   (9600  *RPM, (8 *LBF + 9*OZF)*STD)]

STD = STDCorrection(30.3*inHg, (19 + 273.15)*K)


ThrustData = [(3450  *RPM, (1 *LBF +  4*OZF)*STD),
              (5070  *RPM, (2 *LBF +  10*OZF)*STD),
              (5940  *RPM, (3 *LBF + 12*OZF)*STD),
              (6930  *RPM, (4 *LBF +  14*OZF)*STD),
              (8100 *RPM,  (6 *LBF +  11*OZF)*STD),
              (8670 *RPM, (8 *LBF + 3*OZF)*STD),
              (9210 *RPM, (8 *LBF +  8*OZF)*STD),
              (9660 *RPM, (9 *LBF +  1*OZF)*STD),
              (9670  *RPM,(9 *LBF +  3*OZF)*STD)]

Prop.ThrustData += ThrustData



Arm = 19.5*IN

#                   RPM,        Torque
Prop.TorqueData = [(9720 *RPM, (4.75*Arm*OZF)*STD),
                   (4470 *RPM, (.50*Arm*OZF)*STD),
                   (5610 *RPM, (1.20*Arm*OZF)*STD),
                   (6690 *RPM, (1.75*Arm*OZF)*STD),
                   (8010 *RPM, (3.0*Arm*OZF)*STD),
                   (8640 *RPM, (3.60*Arm*OZF)*STD),
                   (9330 *RPM, (4.35*Arm*OZF)*STD),
                   (9720 *RPM, (4.65*Arm*OZF)*STD),
                   (9300 *RPM, (4.40*Arm*OZF)*STD),
                   (8460 *RPM, (3.25*Arm*OZF)*STD),
                   (7230 *RPM, (2.30*Arm*OZF)*STD),
                   (4560 *RPM, (.75*Arm*OZF)*STD)]

################################################################################
if __name__ == '__main__':
    
    Vmax = 100
    h=0*FT
    N=npy.linspace(1000, 10000, 5)*RPM
    
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

    N = 9600*RPM
    print "Max " + AsUnit(Prop.MaxRPM(), 'rpm', '%3.0f') + " at " + AsUnit(Prop.MaxTipSpeed, 'ft/s') + " tip speed "
    print
    print "Static Thrust   : ", AsUnit( Prop.T(N, 0*FT/SEC, h), 'lbf' )
    print "Measured Thrust : ", AsUnit( max(npy.array(Prop.ThrustData)[:,1]), 'lbf' )
    N = 9700*RPM
    print
    print "Static Torque   : ", AsUnit( Prop.P(N, 0*FT/SEC, h)/N, 'in*ozf' )
    print "Measured Torque : ", AsUnit( max(npy.array(Prop.TorqueData)[:,1]), 'in*ozf' )
    
    pyl.show()

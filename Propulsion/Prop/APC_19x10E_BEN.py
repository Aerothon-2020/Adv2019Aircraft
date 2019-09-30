from __future__ import division # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, W, K, degR, inHg, MM
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name       = 'APC 19x10E'
Prop.D          = 19*IN
Prop.Thickness  = 0.5*IN

Prop.Pitch      = 10*IN
Prop.dAlpha     = 2.9*ARCDEG
Prop.Solidity   = 0.0126  

Prop.AlphaStall = 20*ARCDEG
Prop.AlphaZeroCL = 0*ARCDEG
Prop.CLSlope    = .085/ARCDEG   #- 2D airfoil lift slope (started at 0.08/ARCDEG)
Prop.CDCurve    = 2.2          #- 2D curvature of the airfoil drag bucket (started at 2.2)
Prop.CDp        = 0.02         #- Parasitic drag (started at 0.02)

Prop.Weight     = 99*GRAM*gacc

Prop.ThrustUnit = LBF
Prop.ThrustUnitName = 'lbf'
Prop.PowerUnit = W 
Prop.PowerUnitName = 'watt' 
Prop.MaxTipSpeed = None

#
# These are corrected for standard day
#
#Standard correction
STD = STDCorrection(29.79*inHg, (29.79 + 273.15)*K)

#                 RPM,        Thrust
Prop.ThrustData = [(5460 *RPM, (154+18)*OZF*STD),
                   (4500 *RPM, (99+18)*OZF*STD),
                   (3990 *RPM, (74+18)*OZF*STD),
                   (3540 *RPM, (51+18)*OZF*STD),
                   (2970 *RPM, (34+18)*OZF*STD),
                   (2520 *RPM, (15+18)*OZF*STD)]

STD2 = STDCorrection(29.92*inHg, (24 + 273.15)*K)
Arm = 19.5*IN*STD2

Prop.TorqueData = [(5580  *RPM, (9.3*Arm*OZF)),
                   (4980  *RPM, (7.1*Arm*OZF)),
                   (4500  *RPM, (5.7*Arm*OZF)),
                   (3930  *RPM, (4.5*Arm*OZF)),
                   (3450  *RPM, (3.4*Arm*OZF))]

################################################################################
if __name__ == '__main__':
   
    print " D     : ", AsUnit( Prop.D, 'in')
    print " Pitch : ", AsUnit( Prop.Pitch, 'in')
    
    Vmax = 50
    h=0*FT
    N=npy.linspace(1000, 6800, 5)*RPM
    
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

    N = 6024*RPM
    print
    print "Static Thrust   : ", AsUnit( Prop.T(N, 0*FT/SEC, h), 'lbf' )
    print "Measured Thrust : ", AsUnit( max(npy.array(Prop.ThrustData)[:,1]), 'lbf' )
    N = 6410*RPM
    print
    print "Static Torque   : ", AsUnit( Prop.P(N, 0*FT/SEC, h)/N, 'in*ozf' )
    print "Measured Torque : ", AsUnit( max(npy.array(Prop.TorqueData)[:,1]), 'in*ozf' )
    
    pyl.show() 
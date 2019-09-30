from __future__ import division # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, W, K, degR, inHg, MM
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name       = 'APC 20x8E'
Prop.D          = 20*IN
Prop.Thickness  = 0.5*IN

Prop.Pitch      = 8*IN
Prop.dAlpha     = 3.3*ARCDEG
Prop.Solidity   = 0.0126  

Prop.AlphaStall = 20*ARCDEG
Prop.AlphaZeroCL = 0*ARCDEG
Prop.CLSlope    = .078/ARCDEG  #- 2D airfoil lift slope
Prop.CDCurve    = 2.2          #- 2D curvature of the airfoil drag bucket
Prop.CDp        = .02          #- Parasitic drag

Prop.Weight     = 115*GRAM*gacc

Prop.ThrustUnit = LBF
Prop.ThrustUnitName = 'lbf'
Prop.PowerUnit = W 
Prop.PowerUnitName = 'watt' 
Prop.MaxTipSpeed = None

#
# These are corrected for standard day
#
#Second set of data taken - concern about first set since taken at night
STD = STDCorrection(29.74*inHg, (17.22 + 273.15)*K)
STD2 = STDCorrection( 29.63*inHg, (21.1+273.15)*K )
STD3 = STDCorrection( 30.10*inHg, (12.7+273.15)*K )
Prop.ThrustData = [(5580 *RPM, 186*OZF*STD),
                   (5040 *RPM, 135*OZF*STD),
                   (4470 *RPM, 116*OZF*STD),
                   (4050 *RPM, 99*OZF*STD),
                   (3510 *RPM, 74*OZF*STD),
                   (3210 *RPM, 56*OZF*STD)]


Arm = 19.5*IN*STD
Arm3=19.5*IN*STD3 # Took torque data in closet with known prop to observe difference between temp
Prop.TorqueData = [(5490  *RPM, (8.3*Arm*OZF)),
                   (5000  *RPM, (6.8*Arm*OZF)),
                   (4560  *RPM, (5.5*Arm*OZF)),
                   (4000  *RPM, (4.3*Arm*OZF)),
                   (3525  *RPM, (3.4*Arm*OZF)),
                   # begin 2nd taking of torque data in closet
                   (5690  *RPM, (9.5*Arm3*OZF)),
                   (5018  *RPM, (7.1*Arm3*OZF)),
                   (4525  *RPM, (5.7*Arm3*OZF)),
                   (4118  *RPM, (4.8*Arm3*OZF))]



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
from __future__ import division # let 5/2 = 2.5 rather than 2

#==============================================================================#
# IMPORTS
#==============================================================================#
# import built-in modules
import os
import sys
import numpy as npy
import cmath as math
import pylab as pyl


# import Aerothon modules
from scalar.units import MM, IN, OZF, RPM, HP, V, A, OHM, GRAM, gacc, mAh, W, \
     LBF, inHg, K
from scalar.units import AsUnit
from Aerothon.ACMotor import ACMotor
from Aerothon.AeroUtil import STDCorrection

# (USER) import Aerothon components
from Adv2019Aircraft.Propulsion.Turnigy_6Cell_3000 import Turnigy_6Cell_3000
from Adv2019Aircraft.Propulsion.Phoenix import Phoenix100 # note: Phoenix contains multiple models

#==============================================================================#
# MOTOR MODEL
#==============================================================================#
# Set Motor properties
Motor  = ACMotor()
Motor.name = 'Hacker_A50_14L'

# Associate the motor with a battery and a speed controller (imported above)
Motor.Battery = Turnigy_6Cell_3000
Motor.SpeedController = Phoenix100

# Motor dimensions # SPH: confirm these values 151113
Motor.Weight = 445*GRAM*gacc
Motor.LenDi = [46.8*MM, 59.98*MM]

# Assign objects to weight classes
Motor.Battery.WeightGroup = 'Electronics'
Motor.SpeedController.WeightGroup = 'Electronics'

Motor.WeightGroup = 'Propulsion'

## Manufacturer Data(SPH: Why are we not using these? are they not valid? 151113)
# Motor.Ri  = 0.025*OHM        #Coil resistance
# Motor.Io  = 1*A          #Idle current
# Motor.Kv  = 300*RPM/V      #RPM/Voltage ratio

# Matched data - Model 2
Motor.Ri =.077*OHM #.09
Motor.Io = 1.5*A
Motor.Kv  = 310*RPM/V #320

# SPH: Test data here?? (151113)
Motor.Vmax = 23.5*V
Motor.Imax = 55*A
Motor.ThrustUnit = LBF
Motor.ThrustUnitName = 'lbf'

Motor.xRm =  100000
Motor.Pz  = 0.0

# This data has been corrected for standard day #SPH: confirm the methodology behind these calculations 151113
STD = STDCorrection( 29.9*inHg, (23.9  +273.15)*K )
Arm=19.5*IN
# Test data from the test stand
#            RPM,      Torque              Current   Voltage
TestData = [(6210*RPM, (7.5*Arm*OZF)*STD,  34.8*A,   23.0*V),
            (5910*RPM, (8.7*Arm*OZF)*STD,  39.0*A,   21.9*V),
            (5610*RPM, (9.9*Arm*OZF)*STD,  44.2*A,   21.5*V),
            (5640*RPM, (9.3*Arm*OZF)*STD,  40.5*A,   21.4*V),
            (5640*RPM, (11.9*Arm*OZF)*STD, 48.2*A,   21.5*V),
            (6034*RPM, (8.9*Arm*OZF)*STD,  35.8*A,   22.06*V),
            (5802*RPM, (11.1*Arm*OZF)*STD, 45.2*A,   21.9*V)]

Motor.TestData = TestData

#==============================================================================#
# VISUALIZATION & RESULTS
#==============================================================================#
if __name__ == '__main__':
    
    print 'V to Motor       : ', AsUnit( Motor.Vmotor(Ib=45*A) , 'V' )
    print 'Efficiency       : ', Motor.Efficiency(Ib=45*A)
    print 'Max efficiency   : ', Motor.Effmax()
    print 'Max eff. current : ', AsUnit( Motor.I_Effmax() , 'A' )
    print 'Max eff. RPM     : ', AsUnit( Motor.N_Effmax() , 'rpm' )
    
    Motor.PlotTestData()
    
    pyl.show()

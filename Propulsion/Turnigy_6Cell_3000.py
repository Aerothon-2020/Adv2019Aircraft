#==============================================================================#
# TITLE
#==============================================================================#
# University of Cincinnati
# Aerocats - Regular Class 2016
# Turnigy_6Cell_3000.py: Aerothon battery definition
from scalar.units import GRAM, gacc, A, V, mAh, IN, LBF
from scalar.units import AsUnit
from Aerothon.ACMotor import ACBattery

Weight = []
Power = []

#Thunder Power 

Turnigy_6Cell_3000 = ACBattery()
Turnigy_6Cell_3000.Voltage = 22.2*V
Turnigy_6Cell_3000.Cells = 6 
Turnigy_6Cell_3000.Capacity = 3000*mAh
Turnigy_6Cell_3000.C_Rating = 25
Turnigy_6Cell_3000.Weight = .915*LBF 
Turnigy_6Cell_3000.LWH = (1.375*IN,1.875*IN,6.0*IN) #inaccurate dimensions

Power.append( Turnigy_6Cell_3000.Power() )
Weight.append( Turnigy_6Cell_3000.Weight )

if __name__ == '__main__':
    print AsUnit( Turnigy_6Cell_3000.Imax, 'A' )
from scalar.units import GRAM, gacc, A, V, mAh, IN
from Aerothon.ACMotor import ACSpeedController


Phoenix10 = ACSpeedController()
Phoenix10.Weight = 7*GRAM*gacc
Phoenix10.Imax = 10*A

Phoenix25 = ACSpeedController()
Phoenix25.Weight = 19*GRAM*gacc
Phoenix25.Imax = 25*A

Phoenix100 = ACSpeedController()
Phoenix100.Weight = 91.5*GRAM*gacc
Phoenix100.Imax = 100*A 
Phoenix100.LWH = (1.5*IN, 2*IN, 0.75*IN)

X5 = ACSpeedController()
X5.Weight = 5*GRAM*gacc
X5.Imax = 5*A
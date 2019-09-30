import numpy as npy
import pylab as pyl
from Aerothon.ACPropulsionUCALD import ACPropulsion
from scalar.units import SEC, FT, RPM, HP, LBF, IN, OZF
from Engine.OS46RC import Engine
from Prop.Xoar_11x4 import Prop as Xoar_11x4
from Prop.Xoar_12x4 import Prop as Xoar_12x4
#from Prop.APC_12x3 import Prop as APC_12x3
#from Prop.APC_12x4 import Prop as APC_12x4
from Prop.APC_13x4 import Prop as APC_13x4
from Prop.APC_12x5 import Prop as APC_12x5
from Prop.APC_12_25x3_75_adv import Prop as APC_12_25x3_75_adv
#from Prop_14x6 import Prop as Prop_14x6


Alt  = 0*FT
Vmax = 50*FT/SEC
nV   = 20

V = npy.linspace(0, Vmax / (FT/SEC), 30)*FT/SEC

Propulsion = []
legend = []

Propulsion += [ACPropulsion(Xoar_11x4,Engine)] ; legend += ['Xoar_11x4']
Propulsion += [ACPropulsion(APC_12_25x3_75_adv,Engine)]   ; legend += ['APC_12_25x3_75_adv']
Propulsion += [ACPropulsion(Xoar_12x4,Engine)] ; legend += ['Xoar_12x4']
Propulsion += [ACPropulsion(APC_12x5,Engine)]   ; legend += ['APC_12x5']
Propulsion += [ACPropulsion(APC_13x4,Engine)]   ; legend += ['APC_13x4']
#Propulsion += [ACPropulsion(APC_12x3,Engine)]   ; legend += ['APC_12x3']
#Propulsion += [ACPropulsion(APC_12x4,Engine)]   ; legend += ['APC_12x4']


#Propulsion += [ACPropulsion(APC_14x5,Engine)]   ; legend += ['14x5']
#Propulsion += [ACPropulsion(GRAUPNER_13_5x6,Engine)]   ; legend += ['13.5x6']

#Propulsion += [ACPropulsion(Prop_14x6,Engine)] ; legend += ['14x6']

Vprop = npy.linspace(0,Vmax/(FT/SEC),5)*FT/SEC
N = npy.linspace(1000,20000,30)*RPM

for pp in Propulsion:
    pp.Alt  = Alt
    pp.Vmax = Vmax
    pp.nV   = nV
    
    #Nm = pp.RPMMatch(V)
    #T = pp.Prop.T(Nm, V=0*FT/SEC, h=0*FT)
    #pyl.figure(2)
    #pyl.plot(Nm/RPM, T/LBF)
    
    pp.PlotMatched(V, N, Vprop, fig = 3)
    pp.Prop.PlotTestData(fig = 4)
    

#pyl.figure(2)
#pyl.legend(legend)
#pyl.xlabel("RPM")
#pyl.ylabel("Thrust (lbf)")

pyl.figure(3)
pyl.subplot(223)
pyl.legend(legend, loc='best')

pyl.show()
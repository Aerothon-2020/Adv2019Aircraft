from __future__ import division # let 5/2 = 2.5 rather than 2

#from os import environ as _environ; _environ["scalar_off"] = "off"

from Aerothon.ACPropeller import ACPropeller
from Aerothon.ACEngine import ACEngine
from Aerothon.ACPropulsion import ACPropulsion
from Engine.OS61FX_04 import Engine as OS
from Engine.MAGNUM import Engine as Magnum
from Prop.APC_12_25x3_75 import Prop
#from APC_13_5x6 import Prop
#from GRAUPNER_13_5x6 import Prop
import numpy as npy
from scalar.units import IN, LBF, PSFC, SEC, ARCDEG, FT, OZF, RPM, HP
from scalar.units import AsUnit


# Set Propulsion properties
PropulsionOS = ACPropulsion(Prop,OS)
PropulsionOS.Alt  = 0*FT
PropulsionOS.Vmax = 100*FT/SEC
PropulsionOS.nV   = 20

PropulsionMAG = ACPropulsion(Prop,Magnum)
PropulsionMAG.Alt  = 0*FT
PropulsionMAG.Vmax = 100*FT/SEC
PropulsionMAG.nV   = 20

if __name__ == '__main__':
    import pylab as pyl
   
    print "Static Thrust :", AsUnit( PropulsionOS.T(0*FT/SEC), "lbf")
    print "Static Thrust :", AsUnit( PropulsionMAG.T(0*FT/SEC), "lbf")
    
    Vmax = 100
    V = npy.linspace(0,Vmax,30)*FT/SEC
    Vprop = npy.linspace(0,Vmax,5)*FT/SEC
    N = npy.linspace(1000,20000,30)*RPM
    PropulsionOS.PlotMatched(V, N, Vprop, fig = 2)
    PropulsionMAG.PlotMatched(V, N, Vprop, fig = 2)
    #Propulsion.PlotTPvsN(N, Vprop, fig=3)
    PropulsionMAG.PlotTestData(fig = 3)
    PropulsionOS.PlotTestData(fig = 4)

    
    #Propulsion.Draw(fig=4)
    
    pyl.show()
    
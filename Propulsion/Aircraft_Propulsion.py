from __future__ import division # let 5/2 = 2.5 rather than 2

#from os import environ as _environ; _environ["scalar_off"] = "off"

from Aerothon.ACPropulsion import ACPropulsion
#from Adv2019Aircraft.Propulsion.Motor.Scorpion_SII_4025_330 import Motor
from Adv2019Aircraft.Propulsion.Scorpion250KV import Motor
from Adv2019Aircraft.Propulsion.Prop.APC_22x12W import Prop
from Adv2019Aircraft.Propulsion.Turnigy_6Cell_3000 import Turnigy_6Cell_3000
from Adv2019Aircraft.Propulsion.Phoenix import Phoenix100

import numpy as npy
import cmath as math
import Aerothon.AeroUtil as AUtil
from scalar.units import IN, LBF, PSFC, SEC, ARCDEG, FT, OZF, RPM, HP, A, KG, M, MIN, W, OHM, mAh, V
from scalar.units import AsUnit

#Motor.Ri = Motor.Ri + 0.04*OHM

Motor.Battery = Turnigy_6Cell_3000
Motor.SpeedController = Phoenix100

Motor.Battery.WeightGroup = 'Electronics'
Motor.SpeedController.WeightGroup = 'Electronics'
Motor.WeightGroup = "Propulsion"
Prop.WeightGroup = "Propulsion"

Vmax = 50

# Set Propulsion properties
Propulsion = ACPropulsion(Prop,Motor)
Propulsion.Alt  = 721*FT
Propulsion.Vmax = Vmax*FT/SEC
Propulsion.nV   = 30

if __name__ == '__main__':
    import pylab as pyl
    
    V = npy.linspace(0,Vmax,30)*FT/SEC
    Vprop = npy.linspace(0,Vmax,6)*FT/SEC
    N = Motor.NRange()
    Propulsion.PlotMatched(V, N, Vprop, fig = 2, ylimits = [None,None,None,None] )
    #Propulsion.PlotTPvsN(N, Vprop, fig=3)
    
    Propulsion.PlotTestData(fig=3)
    
    #Propulsion.Draw(fig=4)

    Nm = Propulsion.RPMMatch(V)
    Ib = Motor.Ib(Nm)/A
    #rho = KG/M**3
    #print AsUnit( 0.11 * rho * (6723*RPM/(2*math.pi))**3 * (9*IN)**4*(6*IN), 'W' )
    #print AsUnit( Prop.P(N=Nm[0], V=0*FT/SEC, h=0*FT), 'W' )

    print "Static Thrust          : ", AsUnit( Propulsion.T(0*FT/SEC), "ozf")
    print "Max efficiency current : ", AsUnit( Motor.I_Effmax(), 'A' )
    print "Max efficiency RPM     : ", AsUnit( Motor.N_Effmax(), 'rpm' )
    print "Weight                 : ", AsUnit( Propulsion.Weight, 'lbf' )
        
    pyl.figure(1)
    pyl.subplot(221)
    pyl.title(Propulsion.Engine.name + ', ' + Propulsion.Prop.name)
    pyl.plot(V/(FT/SEC), Ib)
    pyl.grid()
    pyl.xlabel('Aircraft Velocity (ft/s)'); pyl.ylabel('Current (A)') 
    pyl.subplot(222)
    pyl.plot(V/(FT/SEC), Motor.Duration(N=Nm)/MIN)
    pyl.grid()
    pyl.xlabel('Aircraft Velocity (ft/s)'); pyl.ylabel('Duration (min)')

    pyl.subplot(223)
    pyl.plot(V/(FT/SEC), Motor.Pin(Nm)/W)
    pyl.grid()
    pyl.xlabel('Aircraft Velocity (ft/s)'); pyl.ylabel('Power In (watt)') 
    pyl.subplot(224)
    pyl.plot(V/(FT/SEC), Motor.Efficiency(Nm))
    pyl.grid()
    pyl.xlabel('Aircraft Velocity (ft/s)'); pyl.ylabel('Efficiency (%)') 
    
    pyl.show()
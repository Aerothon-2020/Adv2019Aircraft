from __future__ import division # let 5/2 = 2.5 rather than 2

from os import environ as _environ
_environ["scalar_off"] = "off"

import numpy as npy
import pylab as pyl
from scalar.units import FT, SEC, LBF
from Aircraft_Models.Adv2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft

Vstl = npy.linspace(30,34,5)*FT/SEC
LLO  = npy.linspace(31,36,6)*LBF
Vplt = Vstl / (FT/SEC)

Aircraft.VmaxPlt = 100 *FT/SEC

Wing = Aircraft.Wing

pyl.figure(1)
lgnd = []
for l in LLO:
    grndroll = []
    for v in Vstl:
        Wing.V_Stall = v
        Wing.Lift_LO = l
        Aircraft.TotalWeight = l
        
        grndroll.append(Aircraft.Groundroll() / FT)
        
    pyl.plot(Vplt,grndroll)
    lgnd.append('L_LO = %2.0f (lbf)' % (l / LBF) ) 

pyl.axhline(y = 190, color = 'r')
pyl.title('Groundroll vs. Stall Velocity')
pyl.xlabel('Stall Velocity (ft/s)') ; pyl.ylabel('Groundroll (ft)')
pyl.legend(lgnd, loc = 'best')

pyl.show()
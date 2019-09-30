from __future__ import division # let 5/2 = 2.5 rather than 2

#from os import environ as _environ; _environ["scalar_off"] = "off"

import numpy as npy
import pylab as pyl
from scalar.units import LBF
from Adv2019Aircraft.MonoWing.Aircraft import Aircraft

WeightRange = npy.linspace(27,34,1)*LBF

Aircraft.PlotVNDiagram(2 , nlimit = 5) #,WeightRange
Aircraft.Draw(1)

pyl.show()

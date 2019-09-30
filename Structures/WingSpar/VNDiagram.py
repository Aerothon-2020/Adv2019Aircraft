from __future__ import division # let 5/2 = 2.5 rather than 2

from os import environ as _environ; _environ["scalar_off"] = "off"

import numpy as npy
import pylab as pyl
from scalar.units import LBF
from Aircraft_Models.Adv2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft

#WeightRange = npy.linspace(35,40,2)*LBF

WeightRange = [Aircraft.TotalWeight]

Aircraft.PlotVNDiagram(2, WeightRange)
Aircraft.Draw(1)

pyl.show()

from __future__ import division # let 5/2 = 2.5 rather than 2
#from os import environ as _environ; _environ["scalar_off"] = "off"

from Aircraft_Models.Adv2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
import pylab as pyl

Aircraft.PlotTailLoad(fig=2)
Aircraft.Draw()
pyl.show()

from __future__ import division # let 5/2 = 2.5 rather than 2

#from os import environ as _environ; _environ["scalar_off"] = "off"

import numpy as npy
import pylab as pyl
from scalar.units import ARCDEG, FT, SEC, LBF
from scalar.units import AsUnit
#from Aircraft_Models.Reg2013Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
#from Aircraft_Models.Reg2013Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_144 import Aircraft
#from Aircraft_Models.Reg2013Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_148 import Aircraft
from Aircraft_Models.Reg2013Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_152 import Aircraft
#from Aircraft_Models.Reg2013Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_154 import Aircraft
#from Aircraft_Models.Reg2013Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_156 import Aircraft

print 'Aircraft   V_LO     : ', AsUnit( Aircraft.GetV_LO(), 'ft/s')
print 'Wing       V_LO     : ',  AsUnit( Aircraft.Wing.GetV_LO(), 'ft/s')
print 'Ground Roll Distance: ',   AsUnit( Aircraft.Groundroll(), 'ft' )

#
# Uncomment the next two lines and comment out the other "PlotPropulsionPerformance"
# call to plot for a range of values
#

#WeightRange = [ Aircraft.TotalWeight - 0.5*LBF, Aircraft.TotalWeight + 0.5*LBF]
WeightRange = [ Aircraft.TotalWeight ]
Aircraft.PlotPropulsionPerformance(1, Vmax = 80*FT/SEC, TotalWeights = WeightRange)
ii = 2
for wt in WeightRange:
    Aircraft.TotalWeight=wt
    Aircraft.PlotLiftVelocityGroundroll(fig = ii, GrndRollLimit = 190*FT, RulesRollLimit = 200*FT)
    ii += 1
    
Aircraft.Draw(ii+1)

pyl.show()
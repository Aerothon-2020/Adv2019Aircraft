#from os import environ as _environ; _environ["scalar_off"] = "off"

from scalar.units import ARCDEG, IN
from scalar.units import AsUnit
from Aircraft_Models.Adv2014Aircraft_AeroCats.MonoWing.CopyofAircraft import Aircraft
#from Aircraft_Models.Reg2013Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_144 import Aircraft
#from Aircraft_Models.Reg2013Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_148 import Aircraft
#from Aircraft_Models.Reg2013Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_152 import Aircraft
#from Aircraft_Models.Reg2013Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_154 import Aircraft
#from Aircraft_Models.Reg2013Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_156 import Aircraft
#from Aircraft_Models.Reg2013Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_158 import Aircraft

import pylab as pyl


if __name__ == "__main__":
    Aircraft.Wing.Draw2DAirfoilPolars(fig=1)
    Aircraft.HTail.Draw2DAirfoilPolars(fig=2)

    Aircraft.PlotPolarsSlopes(fig=3)
    Aircraft.PlotCMPolars(4, (-12*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +12* ARCDEG), XcgOffsets=(+0.02, -0.02))

    Aircraft.PlotCLCMComponents(fig = 5, del_es = (-10*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10 * ARCDEG))

    Aircraft.Refresh()

    print "Xnp             : ", AsUnit( Aircraft.Xnp(), 'in' )
    print "Wing X          : ", AsUnit( Aircraft.Wing.X[0], 'in' )
    print 'HTail Incidence : ', AsUnit(Aircraft.HTail.i, 'deg')
    print 'HTail VC        : ', Aircraft.HTail.VC
   
    pyl.show()
    
    #
    # The green linear slop approximations should agree well with the blue polars.
    # The slope is adjusted with the *SlopeAt variables.
    #
    # The CM vs. alpha curve for the neutral point should be horizontal.
    #
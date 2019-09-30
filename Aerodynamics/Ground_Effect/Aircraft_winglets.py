from Aircraft_Models.Reg2013Aircraft_AeroCats.MonoWing.Aircraft import Aircraft, Wing, Fuselage, ACSolidWing, ACRibWing
from Aerothon.DefaultMaterialsLibrary import Monokote, PinkFoam, Basswood, Steel, Balsa, Aluminum, Ultracote
from scalar.units import ARCDEG, FT, SEC, LBF, IN
from scalar.units import AsUnit
import pylab as pyl

#
# Add Vertical Winglets
#

Wing.AddWinglet("Winglet",5)
Winglet = Wing.Winglets.Winglet

Winglet.b = 6 *IN
Winglet.Airfoil = 'NACA0012'
Winglet.Lam = [0*ARCDEG, 0*ARCDEG]
Winglet.Gam = [0*ARCDEG, 0*ARCDEG]
Winglet.Fb  = [0.3, 1]
Winglet.TR  = [1.0, 1.0]
Winglet.SweepFc = 0
Winglet.Symmetric = True
Winglet.Axis = (0,-1)
Winglet.SetWeightCalc(ACSolidWing)
Winglet.WingWeight.WingMat = PinkFoam.copy()


if __name__ == '__main__':
    print 'Aircraft   V_LO     : ', AsUnit( Aircraft.GetV_LO(), 'ft/s')
    print 'Wing       V_LO     : ',  AsUnit( Aircraft.Wing.GetV_LO(), 'ft/s')
    print 'Wing       Area     : ',  AsUnit( Aircraft.Wing.S, 'in**2')
    print 'Ground Roll Distance: ',   AsUnit( Aircraft.Groundroll(), 'ft' )
    print 'HTail      Area     : ',    AsUnit( Aircraft.HTail.S, 'in**2')
    print 'HTail      VC       : ',     AsUnit( Aircraft.HTail.VC) 
    print 'HTail      Span       : ',     AsUnit( Aircraft.HTail.b, 'in') 
    
    # Write two avl input files of the aircraft
    # The first does not write the winglets
    # The second writes the main wing and its winglets
    # Currently, you must manually combine the two avl files into one with all the surfaces
    Aircraft.WriteAVLAircraft('AVL\AVLAircraft_winglets.avl')
    
    
    Aircraft.Draw()
    
#    Aircraft.PlotPolarsSlopes(fig=3)
#    Aircraft.PlotCMPolars(4, (-10*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10 * ARCDEG), XcgOffsets=(+0.02, -0.02))
    
    pyl.show()

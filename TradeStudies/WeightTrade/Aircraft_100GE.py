from Aircraft_Models.Adv2014Aircraft_AeroCats.MonoWing.AircraftGE import Aircraft, Wing
from Aircraft_Models.Adv2014Aircraft_AeroCats.MonoWing.Fuselage import Fuselage
from scalar.units import ARCDEG, FT, SEC, LBF, IN
from scalar.units import AsUnit
import pylab as pyl

Wing.b       = 100*IN

#ClimbRate 100
#Aircraft.TotalWeight = 53.17 *LBF
#Wing.S       = 3155*IN**2
#Climb Rate 72.8, Max/CR 129
Wing.S= 1800*IN**2
Aircraft.TotalWeight= 28 *LBF

#===============================================================================
# 3D Wing Slopes
#===============================================================================
Aircraft.CMSlopeAt   = (0 * ARCDEG, 17 * ARCDEG) 
#Aircraft.CLSlopeAt   = (15 * ARCDEG, 18 * ARCDEG)
#Aircraft.CLHTSlopeAt = (5 * ARCDEG, 18 * ARCDEG)
#Aircraft.DWSlopeAt   = (5 * ARCDEG, 19 * ARCDEG)

#Aircraft.Alpha_Zero_CM  = 0 * ARCDEG   #Angle of attach where CM = 0 for the aircraft
#Aircraft.StaticMargin   = 0.09
#Aircraft.WingXMaxIt = 20

#==============================================================================
# Horizontal tail
#==============================================================================
HTail = Aircraft.HTail
#HTail.Airfoil  = 'clarky'
#HTail.AR       = 5
#HTail.S         = 850 * IN **2
#HTail.b        = 63.4 * IN
#HTail.TR       = 1.0
#HTail.o_eff    = 0.96
#HTail.L        = 10 * IN
#HTail.VC       = 0.23
#HTail.FullWing = True
#HTail.DWF      = 1.2 #Main wing Down wash factor (Between 1.0 (close to wing) and 2.0 (far away))
#HTail.Inverted = True
#HTail.ClSlopeAt = (0*ARCDEG, 7*ARCDEG) 
#HTail.CmSlopeAt = (-5*ARCDEG, 5*ARCDEG) 
#===============================================================================
# Elevator properties
#===============================================================================
#HTail.Elevator.Fc = 0.5
#HTail.Elevator.Fb = 1.0
#HTail.Elevator.Ft = 0.0
#HTail.Elevator.Weight = 0.1*LBF 
#HTail.Elevator.Servo.Fc  = 0.3
#HTail.Elevator.Servo.Fbc = 0.1
#HTail.Elevator.Servo.Weight = 2.11 * OZF
#HTail.Elevator.Servo.Torque = 131*IN*OZM
##Set the sweep about the elevator hinge
#HTail.SweepFc  = 1.0 - HTail.Elevator.Fc

#==============================================================================
# Vertical tail
#==============================================================================
VTail = Aircraft.VTail
#VTail.Airfoil = 'NACA0012'
#VTail.VC      = 0.0043
#VTail.AR      = 2
#VTail.TR      = .7
#VTail.Axis    = (0, 1)
#VTail.L       = 10.0 * IN
#VTail.o_eff    = 0.96

#===============================================================================
 # Rudder properties
#===============================================================================
#VTail.Rudder.Fc = 0.5
#VTail.Rudder.Weight = 0.05*LBF * 2 # * 2 For symmetric vertical tail
#VTail.Rudder.SgnDup    = -1.0
#VTail.Rudder.Servo.Fc  = 0.3
#VTail.Rudder.Servo.Fbc = 0.1
#VTail.Rudder.Servo.Weight = 5*GRAM*gacc
#VTail.Rudder.Servo.Weight = 0.58 * OZF
#VTail.Rudder.Servo.Torque = 42*IN*OZM
#Set the sweep about the rudder hinge
#VTail.SweepFc = 1.0 - VTail.Rudder.Fc


if __name__ == '__main__':
    print 'Aircraft   V_LO     : ', AsUnit( Aircraft.GetV_LO(), 'ft/s')
    #print 'Wing       V_LO     : ',  AsUnit( Aircraft.Wing.GetV_LO(), 'ft/s')
    #print 'Wing       Area     : ',  AsUnit( Aircraft.Wing.S, 'in**2')
    print 'Ground Roll Distance: ',   AsUnit( Aircraft.Groundroll(), 'ft' )
    #print 'HTail      Area     : ',    AsUnit( Aircraft.HTail.S, 'in**2')
    #print 'HTail      VC       : ',     AsUnit( Aircraft.HTail.VC) 
    #print 'HTail      Span       : ',     AsUnit( Aircraft.HTail.b, 'in') 
    
    Aircraft.WriteAVLAircraft('AVL\AVLAircraft144GE.avl')

    Aircraft.Draw()
    
    #Aircraft.PlotPolarsSlopes(fig=2)
    #Aircraft.PlotCMPolars(3, (-10*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10 * ARCDEG), XcgOffsets=(+0.02, -0.02))
    #HTail.Draw2DAirfoilPolars(fig=4)
    #Aircraft.PlotCLCMComponents(fig = 5, del_es = (-10*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10 * ARCDEG))
    
    pyl.show()
    

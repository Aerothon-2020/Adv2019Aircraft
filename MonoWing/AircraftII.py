from __future__ import division # let 5/2 = 2.5 rather than 2
#from os import environ as _environ; _environ["scalar_off"] = "off"

from scalar.units import M, FT, IN, ARCDEG, RAD, LBF, SEC, KG, SLUG, OZF, gacc, GRAM, OZM
from scalar.units import AsUnit
from Aerothon.ACAircraft import ACTailAircraft
from Aerothon.ACWingWeight import ACRibWing
from Aerothon.DefaultMaterialsLibrary import Monokote, PinkFoam, Basswood, Steel, Balsa, Aluminum, Ultracote
from Adv2019Aircraft.MonoWing.Fuselage  import Fuselage
#from Adv2019Aircraft.Propulsion.Aircraft_Propulsion import Propulsion
from Reg2015Aircraft_Aerocats.Propulsion.Propulsion import Propulsion
from Adv2019Aircraft.MonoWing.Wing import Wing
import pylab as pyl
import cmath as math
#
# Create the Aircraft from the ACTailAircraft class
Aircraft = ACTailAircraft()
Aircraft.name = 'AdvAeroCats_2019'
# 
# Assign the already generated parts
Aircraft.SetFuselage(Fuselage)
Aircraft.SetPropulsion(Propulsion)
Aircraft.SetWing(Wing)
#
# Position the wing on the top of the fuselage
Aircraft.WingFuseFrac = 0.575
Aircraft.Wing.i = 1.0*ARCDEG
#
# Aircraft Properties
# Total weight is going to change
Aircraft.TotalWeight = 50*LBF 
# Engine align
Aircraft.EngineAlign = 0.7

Aircraft.TippingAngle     = 15*ARCDEG # Black line on AC plot
Aircraft.RotationAngle    = 12*ARCDEG  # Red line on AC plot
Aircraft.Alpha_Groundroll = 0*ARCDEG 

Aircraft.CMSlopeAt   = (0 * ARCDEG, 10 * ARCDEG) 
Aircraft.CLSlopeAt   = (0 * ARCDEG, 15 * ARCDEG)
Aircraft.CLHTSlopeAt = (0 * ARCDEG, 15 * ARCDEG)
Aircraft.DWSlopeAt   = (0 * ARCDEG, 15 * ARCDEG)

Aircraft.Alpha_Zero_CM  = 3.0 * ARCDEG   #for steady level flight
Aircraft.StaticMargin   = 0.06 # Location of Wing           
Aircraft.WingXMaxIt = 50
Aircraft.WingXOmega = 1
#
# Maximum velocity for plotting purposes
Aircraft.VmaxPlt = 75*FT/SEC
#
# Estimate for the time the aircraft rotates on the ground during takeoff
Aircraft.RotationTime = 0.5 * SEC

Aircraft.NoseGearOffset = 7.5*IN
###############################################################################
#
# Tail surfaces
#
###############################################################################

#==============================================================================
# Horizontal tail
#==============================================================================
HTail = Aircraft.HTail
HTail.Airfoil  = 'NACA0012'
#HTail.AR       = 3
HTail.b        = 42 *IN
HTail.TR       = 1.0
HTail.o_eff    = 0.96
HTail.S        = 480 *IN**2
HTail.L        = 45 *IN  #Length from X_CG to Tail AC
#HTail.VC       = 0.70  # 0.8 for S1223 airfoil
HTail.FullWing = True
HTail.DWF      = 1    #Main wing Down wash factor (Typically between 1.0 (close to wing) and 2.0 (far away))
HTail.Inverted = False

HTail.ClSlopeAt = (-5*ARCDEG, 10*ARCDEG) 
HTail.CmSlopeAt = (-4*ARCDEG, 5*ARCDEG) 

Aircraft.HTailPos = 0              #T-Tail =1 regular tail =0
#
# Elevator properties
#
HTail.Elevator.Fc = 0.5     #Elevator % of Tail chord
HTail.Elevator.Fb = 1.0     #Elevator 100% of rear tail span
HTail.Elevator.Ft = 0.0     #0.25
HTail.Elevator.Weight = 0.1*LBF 
HTail.Elevator.WeightGroup = "HTail"
HTail.Elevator.Servo.Fc  = 0.3
HTail.Elevator.Servo.Fbc = 0.15  #Relocating the HTail Servo closer to the elevator
HTail.Elevator.Servo.Weight = 0.3 * OZF
HTail.Elevator.Servo.WeightGroup = "Controls"
HTail.Elevator.Servo.Torque = 33.3*IN*OZM
#Set the sweep about the elevator hinge
HTail.SweepFc  = 1.0 - HTail.Elevator.Fc #Makes Elevator LE straight
#
# Structural properties
# Spar taken as 1/8 inch width and thickness of the max thickness at the root
#
Basswood = Basswood.copy()
BWRibMat = Balsa.copy()
BWRibMat.Thickness = 1/8 * IN

HTail.SetWeightCalc(ACRibWing)
HTail.WingWeight.RibMat                    = BWRibMat
HTail.WingWeight.RibSpace                  = 6 * IN
HTail.WingWeight.SkinMat                   = Ultracote.copy()
HTail.WingWeight.WeightGroup = 'HTail'
HTail.WingWeight.AddSpar("MainSpar", 1*IN, 1*IN, (0.25,0),1.0, False)
HTail.WingWeight.MainSpar.SparMat.LinearForceDensity = .008*LBF/(1*IN)
HTail.WingWeight.MainSpar.ScaleToWing = [False, False]
HTail.WingWeight.MainSpar.WeightGroup = "HTail"

HTail.WingWeight.AddSpar("LeadingEdge", 0.25*IN, 0.25*IN, (0.01,0),1.0, False)
HTail.WingWeight.LeadingEdge.SparMat = Balsa.copy()
#HTail.WingWeight.LeadingEdge.SparMat.LinearForceDensity = .008*LBF/(1*IN)
HTail.WingWeight.LeadingEdge.ScaleToWing = [False, False]
HTail.WingWeight.LeadingEdge.WeightGroup = "HTail"

HTail.WingWeight.AddSpar("TrailingEdge", 0.5*IN, 0.25*IN, (0.975,0),1.0, False)
HTail.WingWeight.TrailingEdge.SparMat = Balsa.copy()
#HTail.WingWeight.TrailingEdge.SparMat.LinearForceDensity = .008*LBF/(1*IN)
HTail.WingWeight.TrailingEdge.ScaleToWing = [False, False]
HTail.WingWeight.TrailingEdge.WeightGroup = "HTail"

#HTail.WingWeight.AddSpar("TrailingEdge2", 1/16*IN, 11/8*IN, (0.25,1),1.0, False)
#HTail.WingWeight.TrailingEdge2.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
#HTail.WingWeight.TrailingEdge2.Position = (0.45,0.55)
#HTail.WingWeight.TrailingEdge2.ScaleToWing = [False, False]
#HTail.WingWeight.TrailingEdge2.WeightGroup = "HTail"

#==============================================================================
# Vertical tail
#==============================================================================
VTail = Aircraft.VTail
VTail.Airfoil = 'NACA0012'
#VTail.VC      = 0.09
#VTail.AR      = 2
VTail.b       = 18 *IN
VTail.TR      = 0.75
VTail.Axis    = (0, 1)        #(0,1)
VTail.L       = HTail.L-6*IN  #Setting Vtail at distance back From Wing
VTail.o_eff    = 0.96
VTail.S       = 189 * IN**2

VTail.FullWing = False
VTail.Symmetric = False
Aircraft.VTailPos = 0
#
# Rudder properties
VTail.Rudder.Fc = 0.5
VTail.Rudder.Weight = 0.05*LBF
VTail.Rudder.WeightGroup = "VTail"
VTail.Rudder.SgnDup    = -1.0
VTail.Rudder.Servo.Fc  = 0.3
VTail.Rudder.Servo.Fbc = 0
#VTail.Rudder.Servo.Weight = 5*GRAM*gacc
VTail.Rudder.Servo.Weight = 0.3 * OZF
VTail.Rudder.Servo.WeightGroup = "Controls"
VTail.Rudder.Servo.Torque = 33.3*IN*OZM

#Set the sweep about the rudder hinge
VTail.SweepFc = 1.0 #- VTail.Rudder.Fc
#
# Structural properties
# Spar taken as 1/8 inch width and thickness of the max thickness at the root
VTail.SetWeightCalc(ACRibWing)
VTail.WingWeight.RibMat                    = BWRibMat
VTail.WingWeight.RibSpace                  = 5 * IN
VTail.WingWeight.SkinMat                   = Ultracote.copy()
VTail.WingWeight.WeightGroup = 'VTail'
VTail.WingWeight.AddSpar("MainSpar", 1*IN, 1*IN, (0.25,0),1.0, False)
VTail.WingWeight.MainSpar.SparMat.LinearForceDensity = .008*LBF/(1*IN) #= Balsa.copy()
VTail.WingWeight.MainSpar.ScaleToWing = [False, False]
VTail.WingWeight.MainSpar.WeightGroup = "VTail"

VTail.WingWeight.AddSpar("LeadingEdge", 1/8*IN, 1/8*IN, (0.008,0),1.0, False)
VTail.WingWeight.LeadingEdge.SparMat = Balsa.copy()
#VTail.WingWeight.LeadingEdge.LinearForceDensity = .008*LBF/(1*IN)
VTail.WingWeight.LeadingEdge.ScaleToWing = [False, False]
VTail.WingWeight.LeadingEdge.WeightGroup = "VTail"

VTail.WingWeight.AddSpar("TrailingEdge", 1/16*IN, 1.75*IN, (0.915,0),1.0, False)
VTail.WingWeight.TrailingEdge.SparMat = Balsa.copy()
#VTail.WingWeight.TrailingEdge.LinearForceDensity = .008*LBF/(1*IN)
VTail.WingWeight.TrailingEdge.ScaleToWing = [False, False]
VTail.WingWeight.TrailingEdge.WeightGroup = "VTail"

#VTail.WingWeight.AddSpar("TrailingEdge2", 1/16*IN, 1.75*IN, (0.25,1),1.0, False)
#VTail.WingWeight.TrailingEdge2.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
#VTail.WingWeight.TrailingEdge2.Position = (0.915,-0.2)
#VTail.WingWeight.TrailingEdge2.ScaleToWing = [False, False]
#VTail.WingWeight.TrailingEdge2.WeightGroup = "VTail"

###############################################################################
#
# Landing Gear
#
###############################################################################
Aluminum = Aluminum.copy()
Steel    = Steel.copy()
MainGear = Aircraft.MainGear
#MainGear.Theta        = 60 * ARCDEG
MainGear.GearHeight   = 6 * IN
#MainGear.StrutL       = 0.2 * IN
MainGear.StrutW       = 0.1 * IN
MainGear.StrutH       = 0.125 * IN
MainGear.WheelDiam    = 4 * IN    
MainGear.X[1]         = 6.0 * IN
MainGear.Strut.Weight = 1.35* LBF 
MainGear.Strut.WeightGroup = "LandingGear"
MainGear.Wheel.Weight = 0.1*LBF 
MainGear.Wheel.WeightGroup = "LandingGear"

NoseGear = Aircraft.NoseGear
NoseGear.StrutW    = 0.1 * IN
NoseGear.StrutH    = 0.1 * IN
NoseGear.WheelDiam = 4 * IN
NoseGear.Strut.Weight = 1 * LBF 
NoseGear.Strut.WeightGroup = "LandingGear"
NoseGear.Wheel.Weight = .1*LBF
NoseGear.Wheel.WeightGroup = "LandingGear"


Aircraft.EmptyWeight = Aircraft.EmptyWeight


if __name__ == '__main__':
        

    print
    print 'Aircraft    V_LO:', AsUnit( Aircraft.GetV_LO(), 'ft/s')
    print 'Wing        V_LO:', AsUnit( Aircraft.Wing.GetV_LO(), 'ft/s')
    print
    print 'V max climb    : ', AsUnit( Aircraft.V_max_climb(),   'ft/s')
    print 'V max          : ', AsUnit( Aircraft.Vmax(),          'ft/s')
    print 'Ground Roll    : ', AsUnit( Aircraft.Groundroll(),    'ft') 
    print 'Total Weight   : ', AsUnit( Aircraft.TotalWeight,     'lbf')
    #print 'Payload Weight : ', AsUnit( Aircraft.PayloadWeight(), 'lbf')
    print 'Wing Height    : ', AsUnit( Aircraft.Wing.Upper(0*IN),'in')
    print 'Vertical Tail H: ', AsUnit( Aircraft.VTail.Tip()[2],  'in' )
    print 'HTail Incidence: ', AsUnit( Aircraft.HTail.i,         'deg')
    print "Lift of AoA    : ", AsUnit( Aircraft.GetAlphaFus_LO(),'deg')
    print "Zero CM AoA    : ", AsUnit( Aircraft.Alpha_Zero_CM,   'deg')
    print 'HTail  VC      : ', AsUnit( Aircraft.HTail.VC) 
    print 'VTail  VC      : ', AsUnit( Aircraft.VTail.VC)
    print 'VTail Area     : ', AsUnit( Aircraft.VTail.S, 'in**2')
    print 'HTail Area     : ', AsUnit( Aircraft.HTail.S, 'in**2')
    print 'HTail Length   : ', AsUnit( Aircraft.HTail.L, 'in')
    #print 'Empty Weight   : ', AsUnit( Aircraft.EmptyWeight,     'lbs')
 
    Aircraft.Draw()
    Aircraft.WriteAVLAircraft('AVLAircraft.avl')  
      
#    VTail.WingWeight.DrawRibs = False
#    VTail.WingWeight.DrawDetail = False
#    VTail.WingWeight.Draw(fig = 2)
#    VTail.Draw(fig = 2)
#    
#    HTail.WingWeight.DrawRibs = False
#    HTail.WingWeight.DrawDetail = False
#    HTail.WingWeight.Draw(fig = 3)
#    HTail.Draw(fig = 3)
    
   # Aircraft.PlotPolarsSlopes(fig=3)
    #Aircraft.PlotCMPolars(4, (-10*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10 * ARCDEG), XcgOffsets=(+0.05, -0.05))
    ## CG LIMITS: AFT = +12%, FWD = -22%
    #HTail.Draw2DAirfoilPolars(fig=2)
    #Aircraft.PlotCLCMComponents(fig = 5, del_es = (-10*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10 * ARCDEG))
    #Aircraft.PlotPropulsionPerformance(fig=6)
    
    pyl.show()
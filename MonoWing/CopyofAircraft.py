from __future__ import division # let 5/2 = 2.5 rather than 2
#from os import environ as _environ; _environ["scalar_off"] = "off"

from scalar.units import M, FT, IN, ARCDEG, RAD, LBF, SEC, KG, SLUG, OZF, gacc, GRAM, OZM
from scalar.units import AsUnit
from Aerothon.ACAircraft import ACTailAircraft
from Aerothon.ACWingWeight import ACSolidWing, ACRibWing
from Aerothon.DefaultMaterialsLibrary import Monokote, PinkFoam, Basswood, Steel, Balsa, Aluminum, Ultracote
from Fuselage import Fuselage
from Adv2019Aircraft.Propulsion.Aircraft_Propulsion import Propulsion
from Wing import Wing      #Always note which wing you're using (Currently working with wing small)
import pylab as pyl
import cmath as math
from Aerothon.ACAircraft import ACTailAircraft

#
# Create the Aircraft from the ACTailAircraft class
#``
Aircraft = ACTailAircraft()
Aircraft.name = 'AdvAeroCats_2014'


# 
# Assign the already generated parts
#
Aircraft.SetFuselage(Fuselage)
Aircraft.SetPropulsion(Propulsion)
Aircraft.SetWing(Wing)

#
# Position the wing on the top of the fuselage
#
Aircraft.WingFuseFrac = 1.05
Aircraft.Wing.i = 0*ARCDEG
#
# Aircraft Properties
# Total weight is going to change
Aircraft.TotalWeight = 27*LBF 
# Engine align
Aircraft.EngineAlign = 1.0

Aircraft.TippingAngle     = 8.5*ARCDEG # Black line on AC plot, set to Lift Off AoA
Aircraft.RotationAngle    = 15*ARCDEG # Red line on AC plot, set 15 deg
Aircraft.Alpha_Groundroll = 0*ARCDEG 

Aircraft.CMSlopeAt   = (2 * ARCDEG, 10 * ARCDEG) 
Aircraft.CLSlopeAt   = (3 * ARCDEG, 14 * ARCDEG)
Aircraft.CLHTSlopeAt = (-5 * ARCDEG, 10 * ARCDEG)
Aircraft.DWSlopeAt   = (3 * ARCDEG, 15 * ARCDEG)


Aircraft.Alpha_Zero_CM  = 3.0 * ARCDEG   #for steady level flight
Aircraft.StaticMargin   = 0.55           
Aircraft.WingXMaxIt = 60
#
# Maximum velocity for plotting purposes
#
Aircraft.VmaxPlt = 150*FT/SEC

#
# Estimate for the time the aircraft rotates on the ground during takeoff
#
Aircraft.RotationTime = 0.1 * SEC

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
HTail.AR       = 4
# HTail.b        = 29 * IN
HTail.TR       = 0.7
HTail.o_eff    = 0.96
# HTail.S        = 225 * IN**2
HTail.L        = Wing.MAC()*2.8   #Setting lh (dist tail is from main wing, check to see if wing or front of fuselage)
HTail.VC       = 1.43  # 0.8 for S1223 airfoil
HTail.FullWing = True
HTail.DWF      = 1.32             #Main wing Down wash factor (Typically between 1.0 (close to wing) and 2.0 (far away))
HTail.Inverted = False

HTail.ClSlopeAt = (-5*ARCDEG, 10*ARCDEG) 
HTail.CmSlopeAt = (-4*ARCDEG, 5*ARCDEG) 


Aircraft.HTailPos = 0              #T-Tail =1 regular tail =0

#
# Elevator properties
#
HTail.Elevator.Fc = .30     #Elevator % of Tail chord
HTail.Elevator.Fb = 1.0     #Elevator 100% of rear tail span
HTail.Elevator.Ft = 0.0 #0.25
HTail.Elevator.Weight = 0.1*LBF 
HTail.Elevator.WeightGroup = "HTail"
HTail.Elevator.Servo.Fc  = 0.3
HTail.Elevator.Servo.Fbc = 0.15  #Relocating the HTail Servo closer to the elevator
HTail.Elevator.Servo.Weight = 0.77 * OZF
HTail.Elevator.Servo.WeightGroup = "Controls"
HTail.Elevator.Servo.Torque = 55*IN*OZM
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
HTail.WingWeight.RibSpace                  = 10 * IN
HTail.WingWeight.SkinMat                   = Ultracote.copy()
HTail.WingWeight.WeightGroup = 'HTail'
HTail.WingWeight.AddSpar("MainSpar", 1*IN, 1.25*IN, (0.25,1),1.0, False)
HTail.WingWeight.MainSpar.SparMat.LinearForceDensity = .008*LBF/(1*IN) # = Balsa.copy()
HTail.WingWeight.MainSpar.Position = (0.45,0.55)
HTail.WingWeight.MainSpar.ScaleToWing = [False, False]
HTail.WingWeight.MainSpar.WeightGroup = "HTail"

HTail.WingWeight.AddSpar("LeadingEdge", 1/8*IN, 1/4*IN, (0.25,1),1.0, False)
HTail.WingWeight.LeadingEdge.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
HTail.WingWeight.LeadingEdge.Position = (0.45,0.55)
HTail.WingWeight.LeadingEdge.ScaleToWing = [False, False]
HTail.WingWeight.LeadingEdge.WeightGroup = "HTail"

HTail.WingWeight.AddSpar("TrailingEdge1", 1/16*IN, 11/8*IN, (0.25,1),1.0, False)
HTail.WingWeight.TrailingEdge1.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
HTail.WingWeight.TrailingEdge1.Position = (0.45,0.55)
HTail.WingWeight.TrailingEdge1.ScaleToWing = [False, False]
HTail.WingWeight.TrailingEdge1.WeightGroup = "HTail"

HTail.WingWeight.AddSpar("TrailingEdge2", 1/16*IN, 11/8*IN, (0.25,1),1.0, False)
HTail.WingWeight.TrailingEdge2.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
HTail.WingWeight.TrailingEdge2.Position = (0.45,0.55)
HTail.WingWeight.TrailingEdge2.ScaleToWing = [False, False]
HTail.WingWeight.TrailingEdge2.WeightGroup = "HTail"

#==============================================================================
# Vertical tail
#==============================================================================
VTail = Aircraft.VTail
VTail.Airfoil = 'NACA0012'
VTail.VC      = 0.12
VTail.AR      = 2.  #1.8
VTail.TR      = 0.8
VTail.Axis    = (0, 1)        #(0,1)
VTail.L       = HTail.L-1.45*IN  #Setting Vtail at distance back the H-tail is
VTail.o_eff    = 0.96
# VTail.S       = 100 * IN**2
# VTail.b       = 13 * IN

VTail.FullWing = False
VTail.Symmetric = False
Aircraft.VTailPos = 0


#
# Rudder properties
#
VTail.Rudder.Fc = 0.5
VTail.Rudder.Weight = 0.05*LBF
VTail.Rudder.WeightGroup = "VTail"
VTail.Rudder.SgnDup    = -1.0
VTail.Rudder.Servo.Fc  = 0.3
VTail.Rudder.Servo.Fbc = 0.5
#VTail.Rudder.Servo.Weight = 5*GRAM*gacc
VTail.Rudder.Servo.Weight = 0.77 * OZF
VTail.Rudder.Servo.WeightGroup = "Controls"
VTail.Rudder.Servo.Torque = 55*IN*OZM
#Set the sweep about the rudder hinge
VTail.SweepFc = 1.0 #- VTail.Rudder.Fc

#
# Structural properties
# Spar taken as 1/8 inch width and thickness of the max thickness at the root
#
VTail.SetWeightCalc(ACRibWing)
VTail.WingWeight.RibMat                    = BWRibMat
VTail.WingWeight.RibSpace                  = 5 * IN
VTail.WingWeight.SkinMat                   = Ultracote.copy()
VTail.WingWeight.WeightGroup = 'VTail'
VTail.WingWeight.AddSpar("MainSpar", 1*IN, 1*IN, (0.25,1),1.0, False)
VTail.WingWeight.MainSpar.SparMat.LinearForceDensity = .008*LBF/(1*IN) #= Balsa.copy()
VTail.WingWeight.MainSpar.Position = (0.45,0)
VTail.WingWeight.MainSpar.ScaleToWing = [False, False]
VTail.WingWeight.MainSpar.WeightGroup = "VTail"

VTail.WingWeight.AddSpar("LeadingEdge", 1/8*IN, 1/4*IN, (0.25,1),1.0, False)
VTail.WingWeight.LeadingEdge.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
VTail.WingWeight.LeadingEdge.Position = (0.008,0)
VTail.WingWeight.LeadingEdge.ScaleToWing = [False, False]
VTail.WingWeight.LeadingEdge.WeightGroup = "VTail"

VTail.WingWeight.AddSpar("TrailingEdge1", 1/16*IN, 1.75*IN, (0.25,1),1.0, False)
VTail.WingWeight.TrailingEdge1.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
VTail.WingWeight.TrailingEdge1.Position = (0.915,0.2)
VTail.WingWeight.TrailingEdge1.ScaleToWing = [False, False]
VTail.WingWeight.TrailingEdge1.WeightGroup = "VTail"

VTail.WingWeight.AddSpar("TrailingEdge2", 1/16*IN, 1.75*IN, (0.25,1),1.0, False)
VTail.WingWeight.TrailingEdge2.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
VTail.WingWeight.TrailingEdge2.Position = (0.915,-0.2)
VTail.WingWeight.TrailingEdge2.ScaleToWing = [False, False]
VTail.WingWeight.TrailingEdge2.WeightGroup = "VTail"



###############################################################################
#
# Landing Gear
#
###############################################################################
Aluminum = Aluminum.copy()
Steel    = Steel.copy()
MainGear = Aircraft.MainGear
MainGear.Theta        = 45*ARCDEG
#MainGear.GearHeight   = 7 * IN
MainGear.StrutL       = 7 * IN
MainGear.StrutW       = 0.2 * IN
MainGear.StrutH       = 0.1 * IN
MainGear.WheelDiam    = 4 * IN    # Changed Wheel Diameter to account for AC Tipping Angle
MainGear.X[1]         = 2.5 * IN
MainGear.Strut.Weight = 0.1*LBF #math.pi*(0.125/2*IN)**2*12*IN*Aluminum.ForceDensity #1/8 inch diameter steel, l=12in
MainGear.Strut.WeightGroup = "LandingGear"
MainGear.Wheel.Weight = 0.1*LBF 
MainGear.Wheel.WeightGroup = "LandingGear"

NoseGear = Aircraft.NoseGear
NoseGear.StrutW    = 0.1 * IN
NoseGear.StrutH    = 0.1 * IN
NoseGear.WheelDiam = 4 * IN

NoseGear.Strut.Weight = .3*LBF #math.pi*(0.125/2*IN)**2*8*IN*Steel.ForceDensity #1/8 inch diameter steel, l=8in
NoseGear.Strut.WeightGroup = "LandingGear"
NoseGear.Wheel.Weight = .16*LBF
NoseGear.Wheel.WeightGroup = "LandingGear"

NoseGear.Strut.Weight = 0.2*LBF #math.pi*(0.125/2*IN)**2*8*IN*Steel.ForceDensity #1/8 inch diameter steel, l=8in
NoseGear.Strut.WeightGroup = "LandingGear"
NoseGear.Wheel.Weight = 0.1*LBF
NoseGear.Wheel.WeightGroup = "LandingGear"
# Aircraft.EmptyWeight = Aircraft.EmptyWeight *LBF


if __name__ == '__main__':
        

    print
    print 'Aircraft   V_LO :', AsUnit( Aircraft.GetV_LO(), 'ft/s' )
    print 'Wing       V_LO :', AsUnit( Aircraft.Wing.GetV_LO(), 'ft/s' )
    print

    print 'V max climb    : ', AsUnit( Aircraft.V_max_climb(),   'ft/s')
    print 'V max          : ', AsUnit( Aircraft.Vmax(),          'ft/s')
    print 'Ground Roll    : ', AsUnit( Aircraft.Groundroll(),    'ft') 
    print 'Total Weight   : ', AsUnit( Aircraft.TotalWeight,     'lbf')
    #print 'Payload Weight : ', AsUnit( Aircraft.PayloadWeight(), 'lbf')
    print 'Wing Height    : ', AsUnit( Aircraft.Wing.Upper(0*IN),'in')
    #print 'Vertical Tail H: ', AsUnit( Aircraft.VTail.Tip()[2],  'in' )
    print 'HTail Incidence: ', AsUnit( Aircraft.HTail.i,         'deg')
    print "Lift of AoA    : ", AsUnit( Aircraft.GetAlphaFus_LO(),'deg' )
    print "Zero CM AoA    : ", AsUnit( Aircraft.Alpha_Zero_CM,   'deg' )
    print 'HTail  VC      : ', AsUnit( Aircraft.HTail.VC) 
    print 'VTail  VC      : ', AsUnit( Aircraft.VTail.VC)
    print 'VTail Area     : ', AsUnit( Aircraft.VTail.S, 'in**2')
    print 'HTail Area     : ', AsUnit( Aircraft.HTail.S, 'in**2')
    #print 'Empty Weight   : ', AsUnit( Aircraft.EmptyWeight,     'm*kg/s**2')
 
    Aircraft.Draw()
    Aircraft.WriteAVLAircraft('AVLAircraft_Latest2.avl')  
#      
#    VTail.WingWeight.DrawRibs = True
#    VTail.WingWeight.DrawDetail = True
#    VTail.WingWeight.Draw(fig = 2)
#    VTail.Draw(fig = 2)
#    
#    HTail.WingWeight.DrawRibs = True
#    HTail.WingWeight.DrawDetail = Tr
#    HTail.WingWeight.Draw(fig = 3)
#    HTail.Draw(fig = 3)
    
    #Aircraft.PlotPolarsSlopes(fig=3)
    #Aircraft.PlotCMPolars(4, (-10*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10 * ARCDEG), XcgOffsets=(+0.1, -0.1))
    #HTail.Draw2DAirfoilPolars(fig=2)
    #Aircraft.PlotCLCMComponents(fig = 5, del_es = (-10*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10 * ARCDEG))
    #Aircraft.PlotPropulsionPerformance(fig=5)
    
    pyl.show()
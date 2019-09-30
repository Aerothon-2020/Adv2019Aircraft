from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import IN, LBF, SLUG, FT, OZF
from scalar.units import AsUnit
from Aerothon.ACFuselage import ACFuselage
from Adv2019Aircraft.Structures.Materials import BalsaBH, ACPlyBH, ACPlySkin, BassStringer, BalsaStringer, Monokote, Steel

Fuselage = ACFuselage()
#
# Create the sections of the fuselage
#
Fuselage.AddSection('Nose'   , 6*IN, -1)
Fuselage.AddSection('PyldBay', 15*IN, -1)
Fuselage.AddSection('Tail', 19*IN, 1)

# Size the engine fire wall
#
Fuselage.Nose.FrontBulk.Width  = 1.0*IN
Fuselage.Nose.FrontBulk.Height = 1.0*IN
Fuselage.Nose.FrontBulk.Material = ACPlyBH.copy()
Fuselage.Nose.Align             = 0.7
Fuselage.Nose.SkinMat = Monokote.copy()
Fuselage.Nose.StringerMat.LinearForceDensity = .01*LBF/IN
Fuselage.Nose.FrontBulk.WeightGroup = 'Fuselage'

#
# Size the payload bay
#
Fuselage.PyldBay.FrontBulk.Width  = 1.0*IN
Fuselage.PyldBay.FrontBulk.Height = 1.0*IN
Fuselage.PyldBay.BackBulk.Width   = 1.0*IN
Fuselage.PyldBay.BackBulk.Height  = 1.0*IN
Fuselage.PyldBay.FrontBulk.Material = ACPlyBH.copy()
Fuselage.PyldBay.BackBulk.Material  = ACPlyBH.copy()
Fuselage.PyldBay.SkinMat = Monokote.copy()
Fuselage.PyldBay.StringerMat.LinearForceDensity = 0.01*LBF/IN
Fuselage.PyldBay.FrontBulk.WeightGroup = 'Fuselage'
Fuselage.PyldBay.BackBulk.WeightGroup = 'Fuselage'
Fuselage.PyldBay.WeightGroup = "Fuselage"

#
#
Fuselage.Tail.BackBulk.Width  = 1.0*IN
Fuselage.Tail.BackBulk.Height = 1.0*IN
Fuselage.Tail.FrontBulk.Material = ACPlyBH.copy()
Fuselage.Tail.Align             = 1
Fuselage.Tail.SkinMat = Monokote.copy()
Fuselage.Tail.StringerMat.LinearForceDensity = .01*LBF/IN
Fuselage.Tail.BackBulk.WeightGroup = 'Fuselage'
Fuselage.Tail.FrontBulk.WeightGroup = 'Fuselage'
#
# Add some components to the nose section
# Nose section components contain propulsion components and nose wheel steering - MH 10/19
# Can add ballast to the nose section of the fuselage if more forward weight is needed for CG balancing - MH 10/20/13
#
#Fuselage.Nose.AddComponent    ("Motor",            0.85*LBF, (-2.0*IN,2*IN,2*IN),     "Front"    ,(0.0, 0.5, 0.5) )
#Fuselage.Nose.AddComponent    ("MotorBattery" ,    1.07*LBF, (5.5*IN,1.5*IN,1.5*IN) , "Back"    , (0.0, 0.5, 0.66) )
#Fuselage.Nose.AddComponent    ("NoseWheelServo",  0.05*LBF, (1.2*IN,0.5*IN,1.2*IN) , "Back"    , (0.0, 0.2, 0.25) )
#Fuselage.Nose.AddComponent    ("SpeedController", 0.27*LBF, (3.0*IN,2.0*IN,1.0*IN) , "Back"   , (0.0, 0.5, 0.85) )
#Fuselage.Nose.AddComponent    ( "Ballast"      , 0.75*LBF, (2.0*IN,1.0*IN,1.0*IN)  , "Back"    , (0.0, 0.8, 0.5) )
#
#Fuselage.Nose.Motor.WeightGroup = "Propulsion"
#Fuselage.Nose.MotorBattery.WeightGroup = "Propulsion"
#Fuselage.Nose.NoseWheelServo.WeightGroup = "Controls"
#Fuselage.Nose.SpeedController.WeightGroup = "Propulsion"
#Fuselage.Nose.Ballast.WeightGroup = "Ballast"
#
# Add Avionics and Flight Control Systems
#Fuselage.PyldBay.AddComponent    ("PixHawk"       , 0.16*LBF, (4.0*IN,1.8*IN,1.5*IN), "Front", (0.0, 0.5, 0.75))
#Fuselage.PyldBay.AddComponent    ("PowerDist"     , 0.04*LBF, (2.0*IN,0.7*IN,1.3*IN), "Top", (0.2, 0.25, 0.0))
#Fuselage.PyldBay.AddComponent    ("GPS"           , 0.17*LBF, (0.5*IN,2.5*IN,2.5*IN), "Top", (0.06, 0.5, 0.0))
#Fuselage.PyldBay.AddComponent    ("Battery"       , 0.16*LBF, (2.5*IN,1.5*IN,1.0*IN), "Top", ())
#Fuselage.PyldBay.AddComponent    ("Reciever"      , 0.03*LBF, (1.0*IN,0.5*IN,2.0*IN), "Top", (0.2, 0.75, 0.0))
#Fuselage.PyldBay.AddComponent    ("TelemetryRcv"  , 0.11*LBF, (4.8*IN,1.5*IN,1.0*IN), "Front", (0.0, 0.5, 0.5))
#
#Fuselage.PyldBay.PixHawk.WeightGroup = "Controller"
#Fuselage.PyldBay.PowerDist.WeightGroup = "Controller"
#Fuselage.PyldBay.GPS.WeightGroup = "Controller"
#Fuselage.PyldBay.Battery.WeightGroup = "Controller"
#Fuselage.PyldBay.Reciever.WeightGroup = "Telemetry"
#Fuselage.PyldBay.TelemetryRcv.WeightGroup = "Telemetry"

#
# Add Telemetry System Components
#Fuselage.PyldBay.AddComponent   ( "GPSMod"      , 0.04*LBF, (0.5*IN,1.6*IN,1.6*IN), "Bottom", (0.083,0.17,0.5))
#Fuselage.PyldBay.AddComponent   ( "TelemXMit"   , 0.01*LBF, (2.3*IN,0.8*IN,0.3*IN), "Bottom", (0.083,0.5,0.5))
#Fuselage.PyldBay.AddComponent   ( "TelemAnt"    , 0.03*LBF, (4.3*IN,0.4*IN,0.4*IN), "Bottom", (0.083,0.5,0.5))
#Fuselage.PyldBay.AddComponent   ( "Airspeed"    , 0.02*LBF, (0.4*IN,0.8*IN,0.8*IN), "Bottom", (0.083,0.83,0.5))
#
#Fuselage.PyldBay.GPSMod.WeightGroup = "Telemetry"
#Fuselage.PyldBay.TelemXMit.WeightGroup = "Telemetry"
#Fuselage.PyldBay.TelemAnt.WeightGroup = "Telemetry"
#Fuselage.PyldBay.Airspeed.WeightGroup = "Telemetry"
#
# Add Flight Control System Components
#Fuselage.Nose.AddComponent    ( "Receiver"   , 0.030*LBF, (1.9*IN,1.6*IN,0.6*IN),  "Top" , (0.9583 , 0.5, 0.5) )
#Fuselage.Nose.AddComponent    ( "Battery"    , 0.150*LBF,  (3.0*IN,1.5*IN,1.0*IN),  "Top" , (0.875 , 0.5, 0.5) )
#
#Fuselage.Nose.Receiver.WeightGroup = "FCSystem"
#Fuselage.Nose.Battery.WeightGroup = "FCSystem"
#
# Add FPV Video System Components
#Fuselage.Nose.AddComponent ( "Camera"       , 0.07*LBF, (0.5*IN,0.8*IN,0.8*IN), "Bottom" , (0.867, 0.5, 0.5))
#Fuselage.PyldBay.AddComponent ( "OSDBoard"     , 0.11*LBF, (0.3*IN,2.4*IN,0.7*IN), "Bottom" , (0.9375, 0.5, 0.5))
#.PyldTaper.AddComponent ( "VideoXMit"    , 0.14*LBF, (1.1*IN,2.7*IN,1.1*IN), "Top"   , (0.5,0.5,0.2))
#Fuselage.PyldBay.AddComponent ( "VideoBatt"    , 0.14*LBF, (0.8*IN,2.1*IN,1.2*IN), "Back"   , (0.5,0.5,0.4))
#
#Fuselage.Nose.Camera.WeightGroup = "Video"
#Fuselage.PyldBay.OSDBoard.WeightGroup = "Video"
#Fuselage.PyldTaper.VideoXMit.WeightGroup = "Video"
#Fuselage.PyldBay.VideoBatt.WeightGroup = "Video"
#

# Define which section contains the CG of the aircraft
#
Fuselage.XcgSection = Fuselage.PyldBay
Fuselage.XcgSecFrac = .25
#
# Define the Payload Objects with the Drop Cargo on the CG
#Fuselage.PyldBay.AddComponent ( "Water1"      , 2*LBF,   (8.0*IN,5.5*IN,3.25*IN), "Bottom", (0.3,0.5,0.0) )
#Fuselage.PyldBay.AddComponent ( "Water2"      , 2*LBF,   (8.0*IN,5.5*IN,3.25*IN), "Bottom", (0.9,0.5,0.0) )
#Fuselage.PyldBay.AddComponent ( "RelServo2"   , 0.05*LBF,  (1.2*IN,0.5*IN,1.2*IN), "Bottom", (0.8,0.5,0.0) )
#Fuselage.PyldBay.AddComponent ( "RelServo1"   , 0.05*LBF,  (1.2*IN,0.5*IN,1.2*IN), "Bottom", (0.2,0.5,0.0) )
#
#Fuselage.PyldBay.Water1.WeightGroup = "Payload"
#Fuselage.PyldBay.Water2.WeightGroup = "Payload"
#Fuselage.PyldBay.RelServo2.WeightGroup = "Controls"
#Fuselage.PyldBay.RelServo1.WeightGroup = "Controls"

# No payload for advanced class
#Fuselage.Payload = None
#Fuselage.Payload.Width  = 5*IN
#Fuselage.Payload.Length = 8*IN
#Fuselage.Payload.Face = 'Bottom'
#Fuselage.Payload.Material = Steel.copy()
#Fuselage.Payload.Weight = 20*LBF

#
# Determine which bulkhead should be set by the horizontal tail
#
Fuselage.TailBulk = Fuselage.Tail.BackBulk
Fuselage.TailBulk.WeightGroup = 'Fuselage'

if __name__ == '__main__':
    import pylab as pyl
    
    print 'Nose       Weight :', AsUnit( Fuselage.Nose.Weight, 'lbf' )
    print 'PyldBay    Weight :', AsUnit( Fuselage.PyldBay.Weight, 'lbf' )
    print 'Tail       Weight :', AsUnit( Fuselage.Tail.Weight, 'lbf')
    
    print 'Fuselage Weight    :', AsUnit( Fuselage.Weight, 'lbf' )
    print 'Fuselage MOI       :', AsUnit( Fuselage.MOI(), 'slug*ft**2' )
    print 'Fuselage CG        :', AsUnit( Fuselage.CG(), 'in' )
    print 'Fuselage Desired CG:', AsUnit( Fuselage.AircraftCG(), 'in' )
    
    
    Fuselage.Draw()
    pyl.show()
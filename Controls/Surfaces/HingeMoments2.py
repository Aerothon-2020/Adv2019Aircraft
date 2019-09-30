#from os import environ as _environ; _environ["scalar_off"] = "off"

from Aerothon.ACControls import ACControls
from Aerothon.ACXFoil import ACXFoil
from Aerothon import AeroUtil
from scalar.units import SEC, ARCDEG, LBF, IN, FT, OZF
from scalar.units import AsUnit
import pylab as pyl
import numpy as npy
from Aircraft_Models.Adv2014Aircraft_AeroCats.MonoWing.CopyofAircraft import Aircraft


Execute = True

Vs = npy.linspace(Aircraft.GetV_LO()/(FT/SEC), Aircraft.Vmax()/(FT/SEC), 11)*FT/SEC
des = npy.linspace(5, 20, 3)*ARCDEG
alpha2d = 3*ARCDEG

# Use the following to investigate the effects of changing geometry
#Aircraft.Wing.Aileron.Fc = 0.15
#Aircraft.Wing.Aileron.Fb = 0.334 #Need adjusted to make aileron 3% from tip
#Aircraft.Wing.Aileron.Ft = 0.1337

#This are the ratios of the servo arm to the control horn arm. The control arm length is the distance to the hinge.
# ArmRatio = (Servo Arm)/(Control Arm)

Aileron_ArmRatio = 0.5
Elevator_ArmRatio = 0.75
Rudder_ArmRatio = 1

Aircraft.Wing.Aileron.PlotHingeMoment(fig=1, RunDir='XFoil/Aileron/', alpha2d=alpha2d, Ht=1, ArmRatio=Aileron_ArmRatio, des=des, Vs=Vs, Execute=Execute)
pyl.title('Aileron Hinge Moment')
Aircraft.HTail.Elevator.PlotHingeMoment(fig=2, RunDir='XFoil/Elevator/', alpha2d=alpha2d, Ht=1, ArmRatio=Elevator_ArmRatio, des=des, Vs=Vs, Execute=Execute)
pyl.title('Elevator Hinge Moment')
Aircraft.VTail.Rudder.PlotHingeMoment(fig=3, RunDir='XFoil/Rudder/', alpha2d=alpha2d, Ht=0.5, ArmRatio=Rudder_ArmRatio, des=des, Vs=Vs, Execute=Execute)
pyl.title('Rudder Hinge Moment')

pyl.show()
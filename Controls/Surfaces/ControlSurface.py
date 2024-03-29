
from os import environ as _environ; _environ["scalar_off"] = "off"

from Aerothon.ACControls import ACControls
from Aerothon import AeroUtil
from Adv2019Aircraft.Controls.StatcStability_PolarSlopes import Aircraft
from scalar.units import SEC, ARCDEG, LBF, IN, FT
from scalar.units import AsUnit
import pylab as pyl
import numpy as npy

Execute = True

Controls = ACControls(Aircraft)
Controls.RunDir = 'AVL/'
Controls.AddRun('Stab', 'AVLAircraft.avl', WriteAVLInput = Execute)
Controls.Stab.AddCommand('a a ' + str(Aircraft.Alpha_Zero_CM/ARCDEG) )
Controls.Stab.DumpStability('AVLDeriv.txt')
Controls.Stab.Exit()

if Execute:
    Controls.ExecuteAVL()
    Controls.ReadAVLFiles()

Aircraft.Draw(fig=1)

das = npy.linspace(0,20,20)*ARCDEG
Vs = npy.linspace(Aircraft.GetV_LO()/(FT/SEC), Aircraft.Vmax()/(FT/SEC), 2)*FT/SEC

pyl.figure(2)

legend = []
for V in Vs:
   Pda = []
   for da in das:
       Pda.append( Controls.Deriv[0].RollDueToAileron(da, 'Aileron', V = V) / (ARCDEG/SEC))
   
   # Uncomment following line if plotting for more than 2 flight velocities        
   #legend.append( AsUnit(V, 'ft/s', '%1.0f') )
   pyl.plot(das/ARCDEG, Pda) 

# Comment following 2 lines if plotting for more than 2 flight velocities
legend.append('$V_{LO}=$' + AsUnit(Aircraft.GetV_LO(), 'ft/s','%1.0f'))
legend.append('$V_{max}=$' + AsUnit(Aircraft.Vmax(), 'ft/s','%1.0f'))

pyl.xlabel('Aileron Deflection (deg)')
pyl.ylabel('Roll Rate (deg/s)')
pyl.legend(legend)
pyl.grid()

Wing = Aircraft.Wing
LLT  = Aircraft.Wing.LLT

y = npy.linspace(-Wing.b/2/IN, Wing.b/2/IN, 61)*IN

#LLT.Alpha3d = 5*ARCDEG

pyl.figure(3)
pyl.subplot(121)
pyl.plot(y/IN, LLT.Alpha_i(y)/ARCDEG)
pyl.xlabel("y (in)")
pyl.ylabel("Induced Angle (deg)")

pyl.axvline(x=Wing.Aileron.Tip()/IN)
pyl.axvline(x=Wing.Aileron.Root()/IN)

pyl.subplot(122)
pyl.plot(y/IN, LLT.Cl(y))
pyl.xlabel("y (in)")
pyl.ylabel("Cl")
pyl.axvline(x=Wing.Aileron.Tip()/IN)
pyl.axvline(x=Wing.Aileron.Root()/IN)

pyl.show()
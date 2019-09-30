#from os import environ as _environ; _environ["scalar_off"] = "off"

from Aerothon.ACControls import ACControls
from Aircraft_Models.Adv2014Aircraft_AeroCats.Controls.StatcStability_PolarSlopes2 import Aircraft
from scalar.units import SEC, ARCDEG, FT, LBF
import pylab as pyl
import numpy as npy

Execute = True
#
# Do a trade study on horizontal tail volume coefficient
#

HTail = Aircraft.HTail
Controls = ACControls(Aircraft)

#HTail.Airfoil = 'NACA3012'
#
# This is the directory where the AVL related files will be written.
# This directory must exist for AVL to execute properly
#
Controls.RunDir = 'AVLHT/'

VCs = npy.linspace(1.1,2,4)

for i in range(len(VCs)):
    print "VC = ", VCs[i]
    run = 'Run' + str(i)
    HTail.VC = VCs[i]
    Controls.AddRun('Stab','AVLAircraft' + str(i) + '.avl', WriteAVLInput = Execute)
    Controls.Stab.AddCommand('a a 8')  #Define angle for analysis
    Controls.Runs[i].DumpStability('STFile' + str(i) + '.txt')

if Execute:
    Controls.ExecuteAVL()

Controls.ReadAVLFiles()

q = Aircraft.Getq_LO()
PDamp      = npy.empty(len(VCs))
iht        = npy.empty(len(VCs))
GroundRoll = npy.empty(len(VCs))
HTDrag     = npy.empty(len(VCs))

t = npy.linspace(0,5)*SEC

legend = []
for i in range(len(VCs)):
    HTail.VC = VCs[i]
    Controls.SetToAircraft()
 #   Controls.Deriv[i].StabilityTable(i+2)
    PDamp[i] = Controls.Deriv[i].PitchDamp()
    iht[i] = HTail.i/ARCDEG
    HTDrag[i] = HTail.CD(0*ARCDEG, 0*ARCDEG)*HTail.S*q / LBF
    GroundRoll[i] = Aircraft.Groundroll()/FT
    Controls.Deriv[i].PlotPitchResponseDueToElevator(3 * ARCDEG, t, 'Elevator', fig = 1)
    Aircraft.PlotTailLoad(fig=6)
    legend.append('VC = %1.2f' % VCs[i])

pyl.figure(1)
pyl.xlabel('Time (sec)')
pyl.ylabel('Elevator step input response')
pyl.title('Horizontal Tail Sizing Trade')
pyl.legend(legend, loc = 'best')

pyl.figure(2)
pyl.plot(VCs, PDamp)
pyl.xlabel('Horizontal Tail Volume Coefficient')
pyl.ylabel('Pitch Damping Coefficient')
pyl.title('Horizontal Tail Sizing Trade')
pyl.axhline(y = 1, color = 'k')

pyl.figure(3)
pyl.plot(VCs, iht)
pyl.xlabel('Horizontal Tail Volume Coefficient')
pyl.ylabel('Horizontal Tail Incidence Angle (deg)')
pyl.title('Horizontal Tail Sizing Trade')

pyl.figure(4)
pyl.plot(VCs, GroundRoll)
pyl.xlabel('Horizontal Tail Volume Coefficient')
pyl.ylabel('Ground Roll (ft)')
pyl.title('Horizontal Tail Sizing Trade')

pyl.figure(5)
pyl.plot(VCs, HTDrag)
pyl.xlabel('Horizontal Tail Volume Coefficient')
pyl.ylabel('Horizontal Tail Lift off Drag (lbf)')
pyl.title('Horizontal Tail Sizing Trade')

pyl.figure(6)
pyl.subplot(324)
pyl.legend(legend, loc = 'best')

pyl.show()

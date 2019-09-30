from Aerothon.ACControls import ACControls
from Aircraft_Models.Adv2014Aircraft_AeroCats.Controls.StatcStability_PolarSlopes import Aircraft
from scalar.units import SEC, ARCDEG, FT, LBF
import pylab as pyl
import numpy as npy

Execute = True
#
# Do a trade study on horizontal tail volume coefficient
#
HTail = Aircraft.HTail
Controls = ACControls(Aircraft)

#
# This is the directory where the AVL related files will be written.
# This directory must exist for AVL to execute properly
#
Controls.RunDir = 'AVLHT/'

#airfoil = ('NACA2412','NACA2612','NACA2712','NACA2812','NACA2912','e423')
#VCs = (0.345,0.32,0.31,0.295,0.31,0.25)
#VCs = [HTail.VC]*len(airfoil)

airfoil = ('NACA3412','NACA4412','NACA5412', 'NACA6313','NACA6413','NACA6513')

VCs = {} 
VCs['NACA3412'] = 0.22
VCs['NACA4412'] = 0.215
VCs['NACA5412'] = 0.211
VCs['NACA6313'] = 0.218
VCs['NACA6413'] = 0.20
VCs['NACA6513'] = 0.208

CMSlopes = {}
CMSlopes['NACA3412'] = (2 * ARCDEG, 13 * ARCDEG)
CMSlopes['NACA4412'] = (2 * ARCDEG, 11 * ARCDEG)
CMSlopes['NACA5412'] = (2 * ARCDEG, 13 * ARCDEG)
CMSlopes['NACA6313'] = (2 * ARCDEG, 11 * ARCDEG)
CMSlopes['NACA6413'] = (5 * ARCDEG, 16 * ARCDEG)
CMSlopes['NACA6513'] = (2 * ARCDEG, 11 * ARCDEG)

for i in range(len(airfoil)):
    print "Airfoil = ", airfoil[i]
    run = 'Run' + str(i)
    HTail.Airfoil = airfoil[i]
    HTail.VC = VCs[airfoil[i]]
    Aircraft.CMSlopeAt = CMSlopes[airfoil[i]]
    Controls.AddRun('Stab','AVLAircraft' + str(i) + '.avl', WriteAVLInput = Execute)
    Controls.Stab.AddCommand('a a 2')  #Define angle for analysis
    Controls.Runs[i].DumpStability('STFile' + str(i) + '.txt')

if Execute:
    Controls.ExecuteAVL()

Controls.ReadAVLFiles()

q = Aircraft.Getq_LO()
PDamp      = npy.empty(len(airfoil))
iht        = npy.empty(len(airfoil))
GroundRoll = npy.empty(len(airfoil))
HTDrag     = npy.empty(len(airfoil))

t = npy.linspace(0,2)*SEC

legend = []
for i in range(len(airfoil)):
    HTail.Airfoil = airfoil[i]
    HTail.VC = VCs[airfoil[i]]
    Aircraft.CMSlopeAt = CMSlopes[airfoil[i]]
    Controls.SetToAircraft()
#    Controls.Deriv[i].StabilityTable(i+2)
    PDamp[i] = Controls.Deriv[i].PitchDamp()
    iht[i] = HTail.i/ARCDEG
    HTDrag[i] = HTail.CD(0*ARCDEG, 0*ARCDEG)*HTail.S*q / LBF
    GroundRoll[i] = Aircraft.Groundroll()/FT
    Controls.Deriv[i].PlotPitchResponseDueToElevator(10 * ARCDEG, t, 'Elevator', fig = 1)
    Aircraft.PlotTailLoad(fig=6)
    legend.append('Airfoil = ' + airfoil[i])

pyl.figure(1)
pyl.xlabel('Time (sec)')
pyl.ylabel('Elevator step input response')
pyl.title('Horizontal Tail Sizing Trade')
pyl.legend(legend, loc = 'best')

pyl.figure(2)
pyl.plot(range(len(airfoil)), PDamp)
pyl.xlabel('Airfoil Number')
pyl.ylabel('Pitch Damping Coefficient')
pyl.title('Horizontal Tail Sizing Trade')
pyl.axhline(y = 1, color = 'k')

pyl.figure(3)
pyl.plot(range(len(airfoil)), iht)
pyl.xlabel('Airfoil Number')
pyl.ylabel('Horizontal Tail Incidence Angle (deg)')
pyl.title('Horizontal Tail Sizing Trade')

pyl.figure(4)
pyl.plot(range(len(airfoil)), GroundRoll)
pyl.xlabel('Airfoil Number')
pyl.ylabel('Ground Roll (ft)')
pyl.title('Horizontal Tail Sizing Trade')

pyl.figure(5)
pyl.plot(range(len(airfoil)), HTDrag)
pyl.xlabel('Airfoil Number')
pyl.ylabel('Horizontal Tail Lift off Drag (lbf)')
pyl.title('Horizontal Tail Sizing Trade')

#pyl.figure(6)
#pyl.subplot(324)
#pyl.legend(legend, loc = 'best')

pyl.show()

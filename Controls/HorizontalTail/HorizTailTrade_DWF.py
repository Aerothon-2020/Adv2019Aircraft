from Aerothon.ACControls import ACControls
from Aircraft_Models.Adv2014Aircraft_AeroCats.Controls.StatcStability_PolarSlopes import Aircraft
from scalar.units import IN, LBF, ARCDEG, SEC
from scalar.units import AsUnit
import pylab as pyl
import numpy as npy
import cmath as math


Execute = True

#
# Set-up AVL Controls Run
#
Controls = ACControls(Aircraft)


DWF = npy.linspace(1.3,1.7,10)
Xnp = []
Cm = []
iht = []

HTail = Aircraft.HTail

Aircraft.Refresh()
Aircraft.Draw(2)
Aircraft.PlotCMPolars(3, (-10*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10 * ARCDEG), XcgOffsets=(+0.05, -0.05))


SetDWF = HTail.DWF

print "DWF, iht : ", SetDWF, AsUnit( Aircraft.HTail.i, 'deg' )

Controls.RunDir = 'AVLDWF/'
for i in range(len(DWF)):
    print "DWF = ", DWF[i]
    run = 'Run' + str(i)
    HTail.DWF = DWF[i]
    Aircraft.Refresh()
    Controls.AddRun(run,'AVLAircraft' + str(i) + '.avl', WriteAVLInput = Execute)
    Controls.Runs[i].AddCommand('a a ' + str(Aircraft.Alpha_Zero_CM/ARCDEG) )
    Controls.Runs[i].DumpStability('STFile' + str(i) + '.txt')
    iht.append( Aircraft.HTail.i )


if Execute:
    Controls.ExecuteAVL()

Controls.ReadAVLFiles()


print
print
print
for i in range(len(DWF)):
    Xnp.append( Controls.Deriv[i].Xnp )
    Cm.append( Controls.Deriv[i].Cmtot )
    print "DWF, Xnp, Cm, iht : ", DWF[i], Xnp[-1], Cm[-1], 'in', AsUnit( iht[i], 'deg' )
    
print " Lift of AoA ", AsUnit( Aircraft.GetAlphaFus_LO(), 'deg' )
print " Zero CM AoA ", AsUnit( Aircraft.Alpha_Zero_CM, 'deg' )

pyl.figure(1)
pyl.subplot(211)
pyl.title("All lines will intersect with the proper Down Wash Factor")
pyl.plot(DWF, Xnp)
pyl.plot((SetDWF, SetDWF), (Xnp[0], Xnp[-1]))
pyl.plot((DWF[0], DWF[-1]), (Aircraft.Xnp()/IN, Aircraft.Xnp()/IN))
pyl.legend(['AVL', 'Set DWF', 'Design Xnp'])
pyl.xlabel("DWF")
pyl.ylabel("Xnp (in)")

pyl.subplot(212)
pyl.plot(DWF, Cm)
pyl.plot((SetDWF, SetDWF), (Cm[0], Cm[-1]))
pyl.axhline(0, color='k')
pyl.legend(['AVL', 'Set DWF'])
#pyl.plot((DWF[0], DWF[-1]), (Aircraft.Xnp()/IN, Aircraft.Xnp()/IN))
pyl.xlabel("DWF")
pyl.ylabel("Cm")

pyl.show()
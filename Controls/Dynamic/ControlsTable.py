from Aerothon.ACControls import ACControls
from Adv2019Aircraft.MonoWing.Aircraft import Aircraft


from scalar.units import IN, LBF, ARCDEG, SEC
from scalar.units import AsUnit
import pylab as pyl
import numpy as npy
import cmath as math

#Aircraft.VTail.VC        = 0.15
#Aircraft.VTail.AR        = 1.5
#Aircraft.VTail.TR        = 0.8
#Aircraft.VTail.Rudder.Fc = 0.75

#Aircraft.Wing.Airfoil = 'E423'
#Aircraft.HTail.VC = 0.2
#Aircraft.Wing.Gam     = [ 3.3*ARCDEG,10*ARCDEG]
#Aircraft.Wing.ConstUpper = False

Execute = False
#
# Set-up AVL Controls Run
#
Controls = ACControls(Aircraft)

#Controls.StaticMargin = 0.05

Controls.RunDir = 'AVL/'
Controls.AddRun('Stability', 'AVLAircraft.avl', WriteAVLInput = Execute)
Controls.Stability.AddCommand('a a ' + str(Aircraft.Alpha_Zero_CM/ARCDEG) )
Controls.Stability.DumpStability('AVLDeriv.txt')
Controls.Stability.Exit()

if Execute:
    Controls.ExecuteAVL()

Controls.ReadAVLFiles()

Deriv = Controls.Deriv[0]


Aircraft.PlotTailLoad(fig=1)

Deriv.StabilityTable(fig=2)

Deriv.PlotStability(fig=3)

t = npy.linspace(0,2)*SEC
Deriv.PlotPitchResponseDueToElevator(10 * ARCDEG, t, 'Elevator', fig = 4)

Deriv.ControlsTables(fig=5)

print
print
print 'Steady state roll rate: ', AsUnit( Deriv.RollDueToAileron(15 * ARCDEG, 'Aileron'), 'deg/s' )
print 'Steady state pitch rate: ', Deriv.PitchResponseDueToElevator(20 * ARCDEG, 1*SEC, 'Elevator')*180/math.pi
print 'Yaw Damping : ', Deriv.Np()
print 'AVL Xnp      : ', Deriv.Xnp, 'in'
print 'Aircraft Xnp : ', AsUnit( Aircraft.Xnp(), 'in' )
#print 'Horizontal Tail incidence angle  : ', AsUnit( Aircraft.HTail.i, 'deg' )


Ma = Deriv.Ma()
Mq = Deriv.Mq()
Madot = Deriv.Madot()
print
print 'AVL Cma, Ma    : ', Deriv.Cma, Ma
print 'AVL Ma**0.5    : ', (-Ma)**0.5
print 'AVL sqrt(Ma)   : ', math.sqrt(-Ma/(1/SEC**2) )
print 'AVL Cmq, Mq    : ', Deriv.Cmq, Mq
print 'AVL Madot      : ', Madot
print -((Mq + Madot) / (2 * (-Ma)**0.5 ))

print 'Aircraft Cmadot   : ', Aircraft.Cmadot()
print 'Aircraft Cmq      : ', Aircraft.Cmq()

print 'Spiral Mode: ', Deriv.SpiralMode()
print 'Spiral double time: ', Deriv.SpiralDoubleTime()
print 'Lb:          ',Deriv.Lb()
print 'Nb = ', Deriv.Nb()
print 'Nr = ', Deriv.Nr()
print 'Np = ', Deriv.Np()
print 'Lb = ', Deriv.Lb()
print 'Lr = ', Deriv.Lr()
#print 'AVL Clr    : ', Deriv.Clr
#print 'AVL Clb    : ', Deriv.Clb
#print 'AVL Cnr    : ', Deriv.Cnr
#print 'AVL Cnb    : ', Deriv.Cnb



Aircraft.Draw(6)
pyl.show()
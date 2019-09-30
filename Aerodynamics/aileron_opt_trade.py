from os import environ as _environ; _environ["scalar_off"] = "off"

from Aerothon.ACControls import ACControls
from Aerothon import AeroUtil
from Aircraft_Models.Adv2014Aircraft_AeroCats.Controls.StatcStability_PolarSlopes import Aircraft
from scalar.units import SEC, ARCDEG, LBF, IN, FT
from scalar.units import AsUnit
import pylab as pyl
import numpy as npy

Wing = Aircraft.Wing
y = npy.linspace(-Wing.b/2/IN, Wing.b/2/IN, 61)*IN

print "Wingspan  : ", Wing.b/2/IN

legend = [];

Fbs = npy.linspace(0.545, 0.545,1) 
TRs = npy.linspace(0.47,0.52,1)
for Fb in Fbs:
    Aircraft.Wing.Fb=[Fb,1]
    for TR in TRs:
        Aircraft.Wing.TR=[1,TR]
        #Aircraft,Wing.Draw(fig = 3)
        LLT = Aircraft.Wing.LLT
        print("Fb of {}, TR of {}".format(Fb,TR))
        print "Wing Area : ", AsUnit(Aircraft.Wing.S, 'in**2')
        print "Wing CL   : ", LLT.CL()
        pyl.figure(4)
        pyl.plot(y/IN,LLT.Cl(y))
        #pyl.axvline(x = -21, color = 'k', lw = 1)    #added by Brock Pleiman (Aileron placement)
        #pyl.axvline(x = -37, color = 'k', lw = 1)     #added by Brock Pleiman (Aileron placement)
        pyl.xlabel("y (in)")
        pyl.ylabel('Cl')
        legend.append("TR = " + str(TR) + ",Fb = " + str(Fb))

        
pyl.axvline(x=Wing.Aileron.Tip()/IN)
pyl.axvline(x=Wing.Aileron.Root()/IN)
pyl.legend(legend, loc = 1)
pyl.plt.grid(True)
pyl.plt.ylim(1,1.6)
#pyl.show()        
#  Selected Wing Design
#TR=0.417 
#Fb=0.417
print("Selected Wing Design")
Aircraft.Wing.Draw(fig = 1)
LLT  = Aircraft.Wing.LLT
print "Wing Area   : ", AsUnit(Aircraft.Wing.S, 'in**2' )
print "Wing CL     : ", LLT.CL()
pyl.figure(5)
pyl.plot(y/IN, LLT.Cl(y))
pyl.xlabel("y (in)")
pyl.ylabel("Cl")
legend.append("Selected Wing Design")        

#  Rectangular Wing
Aircraft.Wing.TR = [1.0,1.0]
Aircraft.Wing.Draw(fig = 2)
LLT = Aircraft.Wing.LLT
print "Wing Area   : ", AsUnit(Aircraft.Wing.S, 'in**2' )
print "Wing CL     : ", LLT.CL()
pyl.figure(5)
pyl.plot(y/IN, LLT.Cl(y))
#pyl.axvline(x = -21, color = 'k', lw = 1)    #added by Brock Pleiman (Aileron placement)
#pyl.axvline(x = -37, color = 'k', lw = 1)     #added by Brock Pleiman (Aileron placement)
pyl.xlabel("y (in)")
pyl.ylabel("Cl")
legend.append("Rectangular wing")

#  Elliptic Approximation using single sections of constant taper
Aircraft.Wing.Fb      = [0.001,1]
Aircraft.Wing.TR = [1.0,0.45] #"Elliptic"
Aircraft.Wing.Draw(fig = 3)
LLT = Aircraft.Wing.LLT
print "Wing Area   : ", AsUnit(Aircraft.Wing.S, 'in**2' )
print "Wing CL     : ", LLT.CL()
pyl.figure(5)
pyl.plot(y/IN, LLT.Cl(y))
pyl.xlabel("y (in)")
pyl.ylabel("Cl")
legend.append("Elliptic Approx.")

pyl.axvline(x=Wing.Aileron.Tip()/IN)
pyl.axvline(x=Wing.Aileron.Root()/IN)
pyl.legend(legend, loc = 1)
pyl.plt.grid(True)
pyl.plt.ylim(1,1.6)
pyl.show()

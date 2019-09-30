from os import environ as _environ; _environ["scalar_off"] = "off"

from Aircraft_Models.Adv2014Aircraft_AeroCats.MonoWing.Wing import Wing
from Aerothon.ACLiftingLine import ACLiftingLine
import numpy as npy
import pylab as pyl
from scalar.units import IN, ARCDEG
from scalar.units import AsUnit

#Wing.Airfoil = 'E423_B'

LLT = ACLiftingLine(Wing)

y = npy.linspace(-Wing.b/2/IN, Wing.b/2/IN, 50)*IN

#LLT.nSpan = 101
LLT.Alpha3d = 5*ARCDEG

pyl.figure(4)
pyl.plot(y/IN, LLT.Cl(y))
pyl.grid(True)
pyl.ylim([1.0,1.6])
pyl.xlabel("y (in)")
pyl.ylabel("Cl")
pyl.axvline(x=Wing.Aileron.Tip()/IN)
pyl.axvline(x=Wing.Aileron.Root()/IN)


Fbs = npy.linspace(0.5, 0.6, 3) 
TRs = npy.linspace(0.47, 0.6, 3)

LoD = {}
CL  = {}
e   = {}

for Fb in Fbs:
    LoD[Fb] = {}
    CL[Fb] = {}
    e[Fb] = {}
    for TR in TRs:

        Wing.Fb = [Fb,1]
        Wing.TR = [1,TR]

        LoD[Fb][TR] = LLT.CL()/LLT.CD()
        CL[Fb][TR] = LLT.CL()
        e[Fb][TR] = LLT.OswaldEff()
        print
        print 'Fb  : ', Fb, '    TR :', TR
        print 'CL  : ', LLT.CL()
        print 'CDi : ', LLT.CDi()
        print 'CD  : ', LLT.CD()
        print 'L/D : ', LLT.CL()/LLT.CD()
        print 'e   : ', LLT.OswaldEff()
        

def SetMax(val, max, Fb, TR):
    
    if val[Fb][TR] > max[0]:
        max[0] = val[Fb][TR]
        max[1] = Fb
        max[2] = TR

maxLoD = [0,0,0]
maxCL  = [0,0,0]
maxe   = [0,0,0]
for Fb in Fbs:
    for TR in TRs:
        
        SetMax(LoD, maxLoD, Fb, TR)
        SetMax(CL , maxCL, Fb, TR)
        SetMax(e  , maxe, Fb, TR)

def PrintMax(name, max, fig):
    print "Max ", name, '  ', max[0], ' at Fb ', max[1], ', TR', max[2] 
    Wing.Fb = [max[1],1]
    Wing.TR = [1,max[2]]
    Wing.Draw(fig=fig)
    pyl.title('Max ' + name)

print
print
PrintMax('LoD', maxLoD, 1)
PrintMax('CL', maxCL, 2)
PrintMax('e', maxe, 3)

pyl.figure(3)
def Plot(values, ylabel):
    legend = []
    for Fb in Fbs:
        pyl.plot(TRs, [values[Fb][TR] for TR in TRs] )
        legend.append('Fb = ' + str(Fb))
        
    pyl.legend(legend, loc = 'best')
    pyl.ylabel(ylabel)
    pyl.xlabel('TR')

pyl.subplot(131)
Plot(LoD, 'LoD')
pyl.subplot(132)
Plot(CL, 'CL')
pyl.subplot(133)
Plot(e, 'Oswald Efficiency')



pyl.show()

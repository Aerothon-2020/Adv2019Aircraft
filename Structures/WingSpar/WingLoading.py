#
# This file demonstrates how to plot wing loading and bending stress of the main spar.
# Most numbers are fictitious and are for demonstrative purposes only (i.e they are made up).
#
from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import IN, FT, PSI, LBF, MPa, KG, M, gacc
from scalar.units import AsUnit
from Aircraft_Models.Adv2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
import pylab as pyl
import numpy as npy

#
# The velocity which loads will be computed
#
Vmax = Aircraft.GetV_LO()*.85

global fignum
fignum = 1

def PlotLiftSurfLoad(Surface, GLoad = 1.0):
    #
    # Plots loads and bending stresses on a lifting surface
    #
    # Inputs:
    #    Surface - A lifting surface with a wing weight calculation
    #    SparFc  - Spar chordwise location in fraction of the chord
    #    SparT   - The thickness of the main spar
    #    MaxBendStress - Optional maximum allowed bending stress of the spar
    #    GLoad   - Generic GLoad multiplier
    
    global fignum
    #
    # Plot the loads on the Surface
    #
    Surface.PlotSpanLoading(V = Vmax, LdMult = GLoad, fig = fignum);       fignum += 1
    Surface.PlotNormalizedSpanLoading(Vmax, LdMult = GLoad, fig = fignum); fignum += 1
    
    WingWeight = Surface.GetWeightCalc()
    #
    # Plot the bending stress
    #
    WingWeight.PlotBendingStress(Vmax, fig = fignum); fignum += 1
    
Aircraft.Wing.WingWeight.MainSpar.MaxBendStress = 6319.26926775*PSI

GLoad = 5.0

Aircraft.Wing.AddPointLoad(Aircraft.Fuselage.PyldBay.BackBulk.Width/2, -Aircraft.TotalWeight/2*GLoad)

PlotLiftSurfLoad(Aircraft.Wing, GLoad = GLoad)
#PlotLiftSurfLoad(Aircraft.HTail, GLoad = GLoad)
#PlotLiftSurfLoad(Aircraft.VTail, GLoad = GLoad)


#Basswood properties
Sm = Aircraft.Wing.WingWeight.MainSpar.MaxBendStress
#BM = 1152.75*LBF*IN #Aircraft.Wing.MomentLoading(V = Vmax)*GLoad
#BM = 10*LBF*IN #Aircraft.Wing.MomentLoading(V = Vmax)*GLoad
#M = M[-1]
H = 1.75*IN 
h = 1/8*IN 

#SparLoc = 5*IN
Joint = 17.5*IN


b = Aircraft.Wing.b/2.

y = npy.linspace(0.0, b / IN, 70)*IN
Load   = Aircraft.Wing.LoadDistSchreiner(y, Vmax) * GLoad
Shear  = Aircraft.Wing.ShearLoading(y, Vmax, Load)
Moment = Aircraft.Wing.MomentLoading(y, Vmax, ShearLoad = Shear)

#
# Moment of inertia for an I beam
#
# Ix = w*h**3/12 (Moment of inertia of the top and bottom area)
# A  = w*h
# I  = 2*(Ix + A*(H/2-h/2)**2)
#
# Bending stress
#
# Sm = BM*H/2/I
# I = BM*H/2/Sm
#
# Solve for the width
#
# I = 2*(w*h**3/12 + w*h*(H/2-h/2)**2)
# w = I/( 2*(h**3/12 + h*(H/2-h/2)**2) )
#

H = npy.empty(len(y))*IN
W = npy.empty(len(y))*IN
Built = npy.empty(len(y))*IN
for i in xrange(len(y)):
    BM = Moment[i]
    
    #H[i]= Aircraft.Wing.Thickness(y[i], Aircraft.Wing.LE(y[i]) + SparLoc)
    yy = (y[i] - Joint)/(b - Joint)
    if y[i] < Joint : 
        H[i] = 1.794*IN
    else:
        H[i] = (1.794*IN)*(1 - yy) + 0.595*IN*yy

    if y[i] < Joint : 
        Built[i] = 1.75*IN 
    else:
        Built[i] = 1.75*IN*(1 - yy) + 0.8*IN*yy
    
    I = BM*H[i]/2/Sm              
    W[i] = I/( 2.*(h**3/12 + h*(H[i]/2-h/2)**2) )

pyl.figure(20)
pyl.ylim([0,2.0])
pyl.plot(y/IN, H/IN)
pyl.plot(y/IN, Built/IN)
pyl.plot(y/IN, W/IN)
pyl.xlabel('Wing Semi Span (in)')
pyl.ylabel('Spar Height/Width (in)') 
pyl.legend(['Spar Height', 'Spar Width', 'Required Width'])
#pyl.ylim([0, 0.8])

Density = 490*KG/M**3*gacc

print "Maximum moment       : ", AsUnit( Moment[0], 'lbf*in' )
print "Required Spar Height : ", AsUnit( H, 'in' )
print "Required Spar Width  : ", AsUnit( W, 'in' )
print "Weight               : ", AsUnit( Density*W*H*Aircraft.Wing.b, 'ozf' )


#print "Moment : ", AsUnit(3500*LBF*6*FT, 'lbf*ft')



print "Load : ", AsUnit( Moment[0]/(72*IN/2), 'lbf')
#print "Load : ", AsUnit( Moment[0]/(2*FT), 'lbf')
pyl.show()

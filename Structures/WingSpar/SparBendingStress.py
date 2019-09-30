from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import IN, FT, PSI, LBF, MPa, KG, M, gacc
from scalar.units import AsUnit

W = 1.75*IN   # Spar Width
H = 1.801*IN # Spar Height 
h = 1/8*IN # Spar Cap Height

#
# Moment arm w/ span of 115 in
# Wing mounts 2 in from center of fuselage
L = 32 * IN / 2 

#
# Breaking load (From last year)
#
F = 135*LBF

#
# Bending moment applied in experiment
#
M = L*F

#
# Calculate the moment of intertia using an I-beam representation
#
# Ix = (W*h**3)/12 (Moment of inertia of the top and bottom area)
# A  = W*h
# I  = 2*(Ix + A*(H/2-h/2)**2)

Ix = (W*h**3)/12
A  = W*h
I  = 2*(Ix + A*(H/2-h/2)**2)

#
# Calculate the bending stress
#

Sm = M*(H/2)/I

print "Breaking Bending Stress : ", AsUnit( Sm, 'psi')

import matplotlib.pyplot as plt

from os import environ as _environ; _environ["scalar_off"] = "off"

from Aerothon.ACControls import ACControls
from Aerothon import AeroUtil
from Reg2015Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
from scalar.units import SEC, ARCDEG, LBF, IN, FT
from scalar.units import AsUnit
import pylab as pyl
import numpy as npy
import cmath as math
from operator import truediv

#Weight History
#from Aircraft_Models.Reg2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
TotWeight14 = 33.00*LBF/4.448222
PayWeight14 = 25.64*LBF/4.448222
EWeight14 = TotWeight14 - PayWeight14
W0_14 = TotWeight14
W0_14 = PayWeight14/(1 - EWeight14/W0_14)
#from Aircraft_Models.Reg2015Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
TotWeight15 = 43.0*LBF/4.448222
PayWeight15 = 35.0*LBF/4.448222
EWeight15 = TotWeight15 - PayWeight15
W0_15 = TotWeight14
W0_15 = PayWeight15/(1 - EWeight15/W0_15)
#from Aircraft_Models.Reg2013Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
TotWeight13 = 52.5*LBF/4.448222
PayWeight13 = 41.66*LBF/4.448222
EWeight13 = TotWeight13 - PayWeight13
W0_13 = TotWeight13
W0_13 = PayWeight13/(1 - EWeight13/W0_13)
#from Aircraft_Models.Reg2012Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
TotWeight12 = 50.1*LBF/4.448222
PayWeight12 = 40.25*LBF/4.448222
EWeight12 = TotWeight12 - PayWeight12
W0_12 = TotWeight12
W0_12 = PayWeight12/(1 - EWeight12/W0_12)
#from Aircraft_Models.Reg2011Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
TotWeight11 = 50.5*LBF/4.448222
PayWeight11 = 41.77*LBF/4.448222
EWeight11 = TotWeight11 - PayWeight11
W0_11 = TotWeight11
W0_11 = PayWeight11/(1 - EWeight11/W0_11)
#from Aircraft_Models.Reg2010Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
TotWeight10 = 47*LBF/4.448222
PayWeight10 = 40*LBF/4.448222
EWeight10 = TotWeight10 - PayWeight10
W0_10 = TotWeight10
W0_10 = PayWeight10/(1 - EWeight10/W0_10)

print '2015 W0 = :', EWeight15/W0_15
print '2014 W0 = :', EWeight14/W0_14
print '2013 W0 = :', EWeight13/W0_13
print '2012 W0 = :', EWeight12/W0_12
print '2011 W0 = :', EWeight11/W0_11
print '2010 W0 = :', EWeight10/W0_10

#pyl.figure(1)
PayWeight = [PayWeight10, PayWeight11, PayWeight12, PayWeight13, PayWeight14, PayWeight15]
EWeight = [EWeight10/W0_10, EWeight11/W0_11, EWeight12/W0_12, EWeight13/W0_13, EWeight14/W0_14,EWeight15/W0_15]
#plt.scatter(PayWeight,EWeight)
#plt.xlabel('W_payload')
#plt.ylabel('W_empty/W0')
#plt.title('Payload vs. Empty Weight/Total Weight')
#   plt.legend('2010' '2011' '2012' '2013' '2014' '2015')
#plt.grid()
#pyl.show()

#CL Estimation
Wing = Aircraft.Wing
Wing.b = 96*IN
y = npy.linspace(-Wing.b/2/IN, Wing.b/2/IN, 61)*IN
LLT = Aircraft.Wing.LLT

Cl = LLT.Cl(y)
Cd = LLT.Cd(y)

Cl_tip = npy.min(Cl)
Cl_root = npy.max(Cl)
Cl_max = ((Cl_tip+Cl_root)/2)*0.95
print 'Cl_max ~= : ',Cl_max

#Weight/Planform Area
from Reg2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
rho= 1.223
Vlo_14 = Aircraft.GetV_LO()
Vstall = Vlo_14/1.1
W_S_2014 = 0.5*rho*Vstall**2*Cl_max

from Reg2013Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
Vlo_13 = Aircraft.GetV_LO()
Vstall = Vlo_13/1.1
W_S_2013 = 0.5*rho*Vstall**2*Cl_max

from Reg2012Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
Vlo_12 = Aircraft.GetV_LO()
Vstall = Vlo_12/1.1
W_S_2012 = 0.5*rho*Vstall**2*Cl_max

from Reg2011Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
Vlo_11 = Aircraft.GetV_LO()
Vstall = Vlo_11/1.1
W_S_2011 = 0.5*rho*Vstall**2*Cl_max

print 'W/S 2011 = ', W_S_2011
print 'W/S 2012 = ', W_S_2012
print 'W/S 2013 = ', W_S_2013
print 'W/S 2014 = ', W_S_2014
pyl.figure(2)
pyl.scatter(11,W_S_2011,s=20, c=u'b')
pyl.scatter(12,W_S_2012,s=20, c=u'g')
pyl.scatter(13,W_S_2013,s=20, c=u'r')
pyl.scatter(14,W_S_2014,s=20, c=u'c')
legend = ('2011', '2012','2013','2014')
pyl.legend(legend, loc = 'center right')
pyl.xlabel('Model Year -2000')
pyl.ylabel('W/S')
pyl.title('Weight to Planform Area Ratio History')
pyl.grid()

#Planform Area, S
S_11 = W0_11*(W_S_2011)**(-1)
S_12 = W0_12*(W_S_2012)**(-1)
S_13 = W0_13*(W_S_2013)**(-1)
S_14 = W0_14*(W_S_2014)**(-1)
print 'Planform Area 2011 = ', S_11
print 'Planform Area 2012 = ', S_12
print 'Planform Area 2013 = ', S_13
print 'Planform Area 2014 = ', S_14

#Thrust to Weight Ratio
T_W_11 = (1.21*W_S_2011)/(9.81*rho*Cl_max*S_11*0.7*Vlo_11)
T_W_12 = (1.21*W_S_2012)/(9.81*rho*Cl_max*S_12*0.7*Vlo_12)
T_W_13 = (1.21*W_S_2013)/(9.81*rho*Cl_max*S_13*0.7*Vlo_13)
T_W_14 = (1.21*W_S_2014)/(9.81*rho*Cl_max*S_14*0.7*Vlo_14)
print 'T/W 2011 =', T_W_11
print 'T/W 2012 =', T_W_12
print 'T/W 2013 =', T_W_13
print 'T/W 2014 =', T_W_14

pyl.figure(3)
pyl.scatter(11,T_W_11,s=20, c=u'b')
pyl.scatter(12,T_W_12,s=20, c=u'g')
pyl.scatter(13,T_W_13,s=20, c=u'r')
pyl.scatter(14,T_W_14,s=20, c=u'c')
legend= ('2011', '2012','2013','2014')
pyl.legend(legend, loc = 'center right')
pyl.xlabel('Model Year -2000')
pyl.ylabel('T/W')
pyl.grid()
pyl.title('Thrust to Weight Ratio History')

Cdmax = npy.max(Cd)
mur = 0.15
h = Wing.Chord(0*FT)
b = Wing.b
G = ((16*h/b)**2)/(1+(16*h/b)**2)
AR = b**2/h
k1 = 1
#KA_2011 = (-rho/(2*W_S_2011))*(Cdmax+Cdmax+(k1+G/(math.pi*e*AR))*Cl_max**2-mur*Cl_max)

##
##
## First part of code from Jake's Aerodynamics_oldRev1.m
rho = 0.0023769 #Standard air density in slug/ft^3
We_hist = [8.50, 10.84, 8.94, 8.25] #Historical Empty Weight Data for Regular Class
W0_hist = [33.00, 50.34, 50.5, 50.0] #Historical GTOW Data for Regular Class
WeW0_hist = map(truediv,We_hist,W0_hist) #Historical Empty/GTOW for Regular Class
Wp_hist = [24.5, 39.5, 41.56, 41.75] #Historical Payload Weight for Regular Class
S_hist = [1700.00, 3485.00, 3450.00, 2950.00]
S_hist[:] = [S/144 for S in S_hist] #Historical Planform Area for Regular Class 
Wing_loadhist = map(truediv,W0_hist,S_hist) #Historical Wing Loading for Regular Class
CLmax_hist = [2.3, 2.4, 2.4, 2.3232]
CLmax_hist = [x*0.9 for x in CLmax_hist] #Historical Maximum Lift Coefficient (Not sure if these were 2D or 3D)
beneathroot = [W*(2/rho) for W in Wing_loadhist]
CLmax_histund1 = [1/C for C in CLmax_hist]
beneathroot2 = [a*b for a,b in zip(beneathroot,CLmax_histund1)]
Vstall_hist = [b**0.5 for b in beneathroot2] #npy.linalg.matrix_power(beneathroot2,0.5) #Calculation of Historical Stalling Velocity

pyl.figure(4)
pyl.scatter(Wp_hist,WeW0_hist)
pyl.title('Historical Empty Weight-to-GTOW Versus Payload')
pyl.xlabel('Payload Weight (lbf)')
pyl.ylabel('Empty Weight/GTOW (lbf/lbf)')
pyl.grid()

pyl.figure(5)
pyl.scatter(Wp_hist,Wing_loadhist)
pyl.title('Historical Wing Loading Versus Payload')
pyl.xlabel('Payload Weight (lbf)')
pyl.ylabel('Wing Loading (lbf/ft^2)');
pyl.grid()

pyl.figure(6)
pyl.scatter(Wp_hist,CLmax_hist)
pyl.title('Historical Maximum Lift Coefficient Versus Payload')
pyl.xlabel('Payload Weight (lbf)')
pyl.ylabel('Maximum Lift Coefficient');
pyl.grid()

pyl.figure(7)
pyl.scatter(Wp_hist,Vstall_hist)
pyl.title('Historical Stalling Velocity Versus Payload')
pyl.xlabel('Payload Weight (lbf)')
pyl.ylabel('Stalling Velocity (ft/s)');
pyl.grid()



pyl.show()


#linalg.solve(a, b)
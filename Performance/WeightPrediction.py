from __future__ import division # let 5/2 = 2.5 rather than 2
import numpy as npy
import pylab as pyl
from scalar.units import LBF
from Aircraft_Models.Adv2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft

#Get maximum score of lift two pounds more than predicted
#Aircraft.TotalWeight = Aircraft.TotalWeight - 2*LBF

TW = Aircraft.TotalWeight
EW = Aircraft.EmptyWeight
h  = Aircraft.Wing.Alt_LO

Aircraft.PlotWeightPrediction(TeamName = "U.C.A.L.D.", 
                              TeamNumber = 216, 
                              fig=1, 
                              TotalWeight = 27*LBF, 
                              EmptyWeight = 8.0*LBF, 
                              h = h, 
                              ShowDesign = False)

pyl.show()

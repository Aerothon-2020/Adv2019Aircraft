import pylab as pyl
import numpy as npy
from scalar.units import LBF


WeightUnit = LBF
WeightName = 'lbf'
Weights = {}
TotalWeight = []

#------------------
def AddAircraft(Aircraft):
    TotalWeight.append( Aircraft.TotalWeight/WeightUnit )
    GroupWeights = Aircraft.GetWeightTable().GetGroupWeights()
    for Group, Weight in GroupWeights.items():
        Weights[Group].append( Weight/WeightUnit )


#------------------
from Aircraft05 import Aircraft

#First setup the arrays for the weights
Groups = Aircraft.GetWeightTable().GetGroups()
for Group in Groups:
    Weights[Group] = []

AddAircraft(Aircraft)

from Aircraft07 import Aircraft

AddAircraft(Aircraft)

from Aircraft09 import Aircraft

AddAircraft(Aircraft)


pyl.figure(1)
for Weight in Weights.values():
    pyl.plot(TotalWeight, Weight)

pyl.xlabel("Total Weight (" + WeightName + ")")
pyl.ylabel("Group Weights (" + WeightName + ")")
pyl.legend(Groups, loc='best')


pyl.show()
import pylab as pyl
import numpy as npy
from scalar.units import LBF, IN

TotalWeight = []
PayloadWeight = []
EmptyWeight = []
Span = []
Area = []

from Aircraft_144_ConstVC import Aircraft

TotalWeight += [Aircraft.TotalWeight / LBF]
EmptyWeight += [Aircraft.EmptyWeight / LBF]
PayloadWeight += [Aircraft.PayloadWeight() / LBF]
from Aircraft_144_ConstVC import Wing
Span+= [Wing.b / IN]
Area+= [Wing.S/ IN**2]

from Aircraft_148_ConstVC import Aircraft

TotalWeight += [Aircraft.TotalWeight / LBF]
EmptyWeight += [Aircraft.EmptyWeight / LBF]
PayloadWeight += [Aircraft.PayloadWeight() / LBF]
from Aircraft_148_ConstVC import Wing
Span+= [Wing.b / IN]
Area+= [Wing.S/ IN**2]

from Aircraft_152_ConstVC import Aircraft

TotalWeight += [Aircraft.TotalWeight / LBF]
EmptyWeight += [Aircraft.EmptyWeight / LBF]
PayloadWeight += [Aircraft.PayloadWeight() / LBF]
from Aircraft_152_ConstVC import Wing
Span+= [Wing.b / IN]
Area+= [Wing.S/ IN**2]

from Aircraft_154_ConstVC import Aircraft
TotalWeight += [Aircraft.TotalWeight / LBF]
EmptyWeight += [Aircraft.EmptyWeight / LBF]
PayloadWeight += [Aircraft.PayloadWeight() / LBF]
from Aircraft_154_ConstVC import Wing
Span+= [Wing.b / IN]
Area+= [Wing.S/ IN**2]

from Aircraft_155_ConstVC import Aircraft

TotalWeight += [Aircraft.TotalWeight / LBF]
EmptyWeight += [Aircraft.EmptyWeight / LBF]
PayloadWeight += [Aircraft.PayloadWeight() / LBF]

from Aircraft_155_ConstVC import Wing
Span+= [Wing.b / IN]
Area+= [Wing.S/ IN**2]

from Aircraft_156_ConstVC import Aircraft

TotalWeight += [Aircraft.TotalWeight / LBF]
EmptyWeight += [Aircraft.EmptyWeight / LBF]
PayloadWeight += [Aircraft.PayloadWeight() / LBF]
from Aircraft_156_ConstVC import Wing
Span+= [Wing.b / IN]
Area+= [Wing.S/ IN**2]

from Aircraft_158_ConstVC import Aircraft

TotalWeight += [Aircraft.TotalWeight / LBF]
EmptyWeight += [Aircraft.EmptyWeight / LBF]
PayloadWeight += [Aircraft.PayloadWeight() / LBF]
from Aircraft_158_ConstVC import Wing
Span+= [Wing.b / IN]
Area+= [Wing.S/ IN**2]






pyl.figure(1)
pyl.plot(TotalWeight, EmptyWeight)

pyl.xlabel("Total Weight (lbf)")
pyl.ylabel("Empty Weight (lbf)")


pyl.figure(2)
pyl.plot(Span, TotalWeight)

pyl.xlabel("Span (in)")
pyl.ylabel("Total Weight (lbf)")

pyl.figure(3)
pyl.plot(Span, PayloadWeight)

pyl.xlabel("Span (in)")
pyl.ylabel("Payload Weight (lbf)")


pyl.figure(4)
pyl.plot(Span, Area)

pyl.xlabel("Span (in)")
pyl.ylabel("Wing Area (in**2)")

pyl.show()
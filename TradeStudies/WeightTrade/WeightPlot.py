import pylab as pyl
import numpy as npy
from scalar.units import LBF, IN

TotalWeight = []
PayloadWeight = []
EmptyWeight = []
Span = []
Area = []
TotalWeightGE = []
PayloadWeightGE = []
EmptyWeightGE = []
SpanGE = []
AreaGE = []
from Aircraft_144 import Aircraft

TotalWeight += [Aircraft.TotalWeight / LBF]
EmptyWeight += [Aircraft.EmptyWeight / LBF]
PayloadWeight += [Aircraft.PayloadWeight() / LBF]
from Aircraft_144 import Wing
Span+= [Wing.b / IN]
Area+= [Wing.S/ IN**2]

from Aircraft_148 import Aircraft

TotalWeight += [Aircraft.TotalWeight / LBF]
EmptyWeight += [Aircraft.EmptyWeight / LBF]
PayloadWeight += [Aircraft.PayloadWeight() / LBF]
from Aircraft_148 import Wing
Span+= [Wing.b / IN]
Area+= [Wing.S/ IN**2]

from Aircraft_150 import Aircraft
TotalWeight += [Aircraft.TotalWeight / LBF]
EmptyWeight += [Aircraft.EmptyWeight / LBF]
PayloadWeight += [Aircraft.PayloadWeight() / LBF]
from Aircraft_150 import Wing
Span+= [Wing.b / IN]
Area+= [Wing.S/ IN**2]


from Aircraft_152 import Aircraft

TotalWeight += [Aircraft.TotalWeight / LBF]
EmptyWeight += [Aircraft.EmptyWeight / LBF]
PayloadWeight += [Aircraft.PayloadWeight() / LBF]
from Aircraft_152 import Wing
Span+= [Wing.b / IN]
Area+= [Wing.S/ IN**2]

from Aircraft_154 import Aircraft
TotalWeight += [Aircraft.TotalWeight / LBF]
EmptyWeight += [Aircraft.EmptyWeight / LBF]
PayloadWeight += [Aircraft.PayloadWeight() / LBF]
from Aircraft_154 import Wing
Span+= [Wing.b / IN]
Area+= [Wing.S/ IN**2]

#from Aircraft_155 import Aircraft

#TotalWeight += [Aircraft.TotalWeight / LBF]
#EmptyWeight += [Aircraft.EmptyWeight / LBF]
#PayloadWeight += [Aircraft.PayloadWeight() / LBF]

#from Aircraft_155 import Wing
#Span+= [Wing.b / IN]
#Area+= [Wing.S/ IN**2]

from Aircraft_156 import Aircraft

TotalWeight += [Aircraft.TotalWeight / LBF]
EmptyWeight += [Aircraft.EmptyWeight / LBF]
PayloadWeight += [Aircraft.PayloadWeight() / LBF]
from Aircraft_156 import Wing
Span+= [Wing.b / IN]
Area+= [Wing.S/ IN**2]

from Aircraft_158 import Aircraft

TotalWeight += [Aircraft.TotalWeight / LBF]
EmptyWeight += [Aircraft.EmptyWeight / LBF]
PayloadWeight += [Aircraft.PayloadWeight() / LBF]
from Aircraft_158 import Wing
Span+= [Wing.b / IN]
Area+= [Wing.S/ IN**2]

#from Aircraft_162_lnv109A_9 import Aircraft
#TotalWeight += [Aircraft.TotalWeight / LBF]
#EmptyWeight += [Aircraft.EmptyWeight / LBF]
#PayloadWeight += [Aircraft.PayloadWeight() / LBF]
#from Aircraft_162_lnv109A_9 import Wing
#Span+= [Wing.b / IN]
#Area+= [Wing.S/ IN**2]

####GE Aircraft
from Aircraft_144GE import Aircraft

TotalWeightGE += [Aircraft.TotalWeight / LBF]
EmptyWeightGE += [Aircraft.EmptyWeight / LBF]
PayloadWeightGE += [Aircraft.PayloadWeight() / LBF]
from Aircraft_144GE import Wing
SpanGE+= [Wing.b / IN]
AreaGE+= [Wing.S/ IN**2]

from Aircraft_148GE import Aircraft

TotalWeightGE += [Aircraft.TotalWeight / LBF]
EmptyWeightGE += [Aircraft.EmptyWeight / LBF]
PayloadWeightGE += [Aircraft.PayloadWeight() / LBF]
from Aircraft_148GE import Wing
SpanGE+= [Wing.b / IN]
AreaGE+= [Wing.S/ IN**2]

from Aircraft_150GE import Aircraft
TotalWeightGE += [Aircraft.TotalWeight / LBF]
EmptyWeightGE += [Aircraft.EmptyWeight / LBF]
PayloadWeightGE += [Aircraft.PayloadWeight() / LBF]
from Aircraft_150GE import Wing
SpanGE+= [Wing.b / IN]
AreaGE+= [Wing.S/ IN**2]


from Aircraft_152GE import Aircraft

TotalWeightGE += [Aircraft.TotalWeight / LBF]
EmptyWeightGE += [Aircraft.EmptyWeight / LBF]
PayloadWeightGE += [Aircraft.PayloadWeight() / LBF]
from Aircraft_152GE import Wing
SpanGE+= [Wing.b / IN]
AreaGE+= [Wing.S/ IN**2]

from Aircraft_154GE import Aircraft
TotalWeightGE += [Aircraft.TotalWeight / LBF]
EmptyWeightGE += [Aircraft.EmptyWeight / LBF]
PayloadWeightGE += [Aircraft.PayloadWeight() / LBF]
from Aircraft_154GE import Wing
SpanGE+= [Wing.b / IN]
AreaGE+= [Wing.S/ IN**2]

#from Aircraft_155GE import Aircraft

#TotalWeight += [Aircraft.TotalWeight / LBF]
#EmptyWeight += [Aircraft.EmptyWeight / LBF]
#PayloadWeight += [Aircraft.PayloadWeight() / LBF]

#from Aircraft_155GE import Wing
#Span+= [Wing.b / IN]
#Area+= [Wing.S/ IN**2]

from Aircraft_156GE import Aircraft

TotalWeightGE += [Aircraft.TotalWeight / LBF]
EmptyWeightGE += [Aircraft.EmptyWeight / LBF]
PayloadWeightGE += [Aircraft.PayloadWeight() / LBF]
from Aircraft_156GE import Wing
SpanGE+= [Wing.b / IN]
AreaGE+= [Wing.S/ IN**2]

from Aircraft_158GE import Aircraft

TotalWeightGE += [Aircraft.TotalWeight / LBF]
EmptyWeightGE += [Aircraft.EmptyWeight / LBF]
PayloadWeightGE += [Aircraft.PayloadWeight() / LBF]
from Aircraft_158GE import Wing
SpanGE+= [Wing.b / IN]
AreaGE+= [Wing.S/ IN**2]



pyl.figure(1)
pyl.plot(TotalWeight, EmptyWeight)
pyl.plot(TotalWeightGE, EmptyWeightGE)

pyl.xlabel("Total Weight (lbf)")
pyl.ylabel("Empty Weight (lbf)")


pyl.figure(2)
pyl.plot(Span, TotalWeight)
pyl.plot(SpanGE, TotalWeightGE)

pyl.xlabel("Span (in)")
pyl.ylabel("Total Weight (lbf)")

pyl.figure(3)
pyl.plot(Span, PayloadWeight)
pyl.plot(SpanGE, PayloadWeightGE)

pyl.xlabel("Span (in)")
pyl.ylabel("Payload Weight (lbf)")


pyl.figure(4)
pyl.plot(Span, Area)
pyl.plot(SpanGE, AreaGE)

pyl.xlabel("Span (in)")
pyl.ylabel("Wing Area (in**2)")

pyl.figure(5)
pyl.plot(TotalWeight, Area)
pyl.plot(TotalWeightGE, AreaGE)

pyl.xlabel("Total Weight (lbf)")
pyl.ylabel("Wing Area (in**2)")
pyl.show()
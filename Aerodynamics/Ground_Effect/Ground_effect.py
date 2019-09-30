from Aircraft_winglets import Aircraft, Wing, Fuselage, ACSolidWing, ACRibWing
from Aerothon.DefaultMaterialsLibrary import Monokote, PinkFoam, Basswood, Steel, Balsa, Aluminum, Ultracote
from scalar.units import ARCDEG, FT, SEC, LBF, IN
from scalar.units import AsUnit
import pylab as pyl
import numpy as npy
from scalar.units import IN

Aircraft.Draw()

Z_array = [0.5,0.4,0.3,0.2,0.1,0.0,-0.1,-0.2,-0.3,-0.4,-0.5,-0.75,-1.0,-1.5,-2.0,-3.0,-4.0,-5.0,-10.0,-15.0,-20.0,-30.0,-40.0,-50.0,-100.0,-200.0]

#fname_base = ('AVL\AVLAircraft')
fname_base = ('AVL\AVLAircraft_winglets')

#Aircraft.WriteAVLAircraft(fname_base + '_noGE')

for i in Z_array:
    Aircraft.iZsym = 1
    Aircraft.Zsym = i * IN
    
    fname = fname_base + '_GE_Zsym_'    
    
    if i<0:
        fname = fname + 'n' + str(abs(i))
    else:
        fname = fname + 'p' + str(abs(i))

    #Aircraft.WriteAVLAircraft(fname + '.avl')
    
    print fname
    
    
    
    #Controls.RunDir = 'AVL/'
    #Controls.AddRun('Stab', 'AVLAircraft.avl', WriteAVLInput = Execute)
    #Controls.Stab.AddCommand('a a ' + str(Aircraft.Alpha_Zero_CM/ARCDEG) )
    #Controls.Stab.DumpStability('AVLDeriv.txt')
    #Controls.Stab.Exit()

    #if Execute:
    #    Controls.ExecuteAVL()

    #Controls.ReadAVLFiles()
            
        
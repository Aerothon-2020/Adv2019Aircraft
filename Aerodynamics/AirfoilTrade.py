from Aerothon.ACAirfoil import ACAirfoil
import pylab as pyl

Airfoils = ["E423","E423_B","S1223"]#Main wing
#Airfoils = ["NACA2408","E169"]#Horz tail
#Airfoils = ["NACA0010","NACA0012","NACA0015"]#vert tail

for AirfoilName in Airfoils:
    Airfoil = ACAirfoil(AirfoilName)
    Airfoil.PlotReportPolars(fig=1, Re=413946)#main wing
    #Airfoil.PlotReportPolars(fig=1, Re=174000)#tail horz and vert
    
pyl.subplot(311)
pyl.legend(Airfoils, loc = "best")


pyl.show()
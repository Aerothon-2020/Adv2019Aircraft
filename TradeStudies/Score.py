import numpy as npy
import pylab as pyl
from scalar.units import LBF

def ScoreEquation(TW, EW, Predicted):
    # EW = Empty Weight (lbf)
    # PW = Payload Weight
    # TW = Total Weight ( PW + EW )
    return 

if __name__ == '__main__':
    # EW = Empty Weight (lbf)
    # Pf = Payload Fraction ( PW/(EW + PW) )
    # PW = Payload Weight
    # TW = Total Weight ( PW + EW )
    # Score = (2-EW)*(Pf)*120

    EW = npy.linspace(0.1, 1.0, 10)

    # Desired score
    Scores = npy.linspace(100,160 , 7)

    legend = []

    for Score in Scores:

        Pf = Score/((2 - EW)*120)
        
        for i in xrange(len(Pf)):
            if Pf[i] > 0.9:
                Pf[i] = 0.899

        
        PW = Pf*EW/(1 -  Pf)
        TW = PW + EW
        
        legend.append('Score ' + str(Score))
        
        pyl.figure(1)   
        pyl.subplot(131)
        pyl.plot(EW, Pf)
        pyl.xlabel('Empty Weight (lbf)')
        pyl.ylabel('Payload Fraction')
        pyl.subplot(132)
        pyl.xlabel('Empty Weight (lbf)')
        pyl.ylabel('Total Weight (lbf)')
        pyl.plot(EW, TW)

    pyl.subplot(131)
    pyl.legend(legend, loc='best')
    pyl.grid()
    pyl.subplot(132)
    pyl.legend(legend, loc='best')
    pyl.grid()

    legend = []
    TWs = [2.5, 3, 3.5, 4, 4.5]

    for TW in TWs:
        PW = TW - EW
        Pf = PW/TW
        
        Score = (2-EW)*(Pf)*120
        
        legend.append('Total Weight ' + str(TW) + ' lbf')
        
        pyl.subplot(133)   
        pyl.plot(EW, Score)
        pyl.xlabel('Empty Weight (lbf)')
        pyl.ylabel('Score')

    pyl.subplot(133)
    pyl.legend(legend, loc='upper right')
    pyl.grid()

    pyl.show()

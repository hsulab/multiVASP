import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from LinearMethods import LinearMethod
from PreSelection import PreSelection

from DataOperators import pkload

def cmp_etype():
    feas, Ets_best, means, stds = pkload('Best_las_Ets.pk') 
    feas, Etsra_best, means, stds = pkload('Best_las_Etsra.pk') 

    def outs(bests):
        for name, coef in bests.items():
            print('{:<20} -> {:<10}'.format(name, round(coef, 4)))

    print('Ets')
    outs(Ets_best)
    print('Etsra')
    outs(Etsra_best)

def main():
    #cmp_etype()
    view_cv()

if __name__ == '__main__':
    main()

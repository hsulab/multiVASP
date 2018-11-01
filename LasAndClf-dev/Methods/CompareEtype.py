#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: CompareEtype.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 一 10/29 22:05:10 2018
#########################################################################
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from LinearMethods import LinearMethod
from PreSelection import PreSelection

from DataOperators import pkload

def cmp_etype():
    feas, Ea_best, means, stds = pkload('Best_las_Ea.pk') 
    feas, Ets_best, means, stds = pkload('Best_las_Ets.pk') 
    feas, Etsra_best, means, stds = pkload('Best_las_Etsra.pk') 

    def outs(bests):
        for name, coef in bests.items():
            print('{:<20} -> {:<10}'.format(name, round(coef, 4)))

    print('Ea')
    outs(Ea_best)
    print('Ets')
    outs(Ets_best)
    print('Etsra')
    outs(Etsra_best)

def view_cv():
    Etype = 'Etsra'
    LinearMethod('las', Etype, cvtest=10, ran=2)
    gslas = pkload('las_'+Etype+'.pk')
    PreSelection('las_'+Etype+'.pk')
    nc = pkload('PosCoef_las_'+Etype+'.pk')
    print('*'*20)
    print(gslas.best_params_)
    print(gslas.cv_results_['mean_test_MSE'])
    print('*'*20)

    print('Positive Coefficient ', len(nc.keys()))
    for name, coef in nc.items():
        print('{:<20} -> {:<10}'.format(name, round(coef, 4)))

def main():
    #cmp_etype()
    view_cv()

if __name__ == '__main__':
    main()

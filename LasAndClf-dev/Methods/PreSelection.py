#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: PreSelection.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
'System'
import time

'SciLibs'
import math
import numpy as np
import pandas as pd

'Plot'
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

'sklearn'
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso,LassoLars,LassoCV,LassoLarsCV
from sklearn.model_selection import KFold

'Data Operation'
import pickle
from DataOperators import GetDS
from DataOperators import pkload
from DataOperators import pkdump

def std_yx(y, X):
    'StandardScaler Data'
    scaler_y = StandardScaler().fit(y)
    y_ = scaler_y.transform(y).ravel()
    scaler_X = StandardScaler()
    X_ = scaler_X.fit_transform(X)
    return y_, X_, scaler_y, scaler_X

logtime = time.strftime("%Y%m%d")
def PreSelection(pkfile):
    'Load DataSet'
    print('Loading DataSet...')
    DS = GetDS(pkfile.split('.')[0].split('_')[1])

    'Load Pickle'
    print('Loading '+pkfile+'...')
    gs = pkload(pkfile)
    if pkfile == 'lsr.pk':
        best_gs = gs
    else:
        best_gs = gs.best_estimator_
    params = best_gs.get_params()

    'Get Positive Coef'
    print('Collecting Coefficients...')
    # get feature name and coef
    feanames = DS['fea_names']
    coefs = best_gs.coef_
    #
    name_coef = {}
    for name, coef in zip(feanames, coefs):
        if abs(coef) > 0:
            name_coef[name] = coef
    # sort fea by abs value
    nc_sorted = sorted(name_coef.items(), key=lambda d:abs(d[1]), reverse=True)
    nc_dict = {}
    for t in nc_sorted:
        nc_dict[t[0]] =t[1]

    'Dump Pickle'
    print('Dumping Pickle...')
    laspk = (params, nc_dict)
    pkdump('PosCoef_'+pkfile, laspk)

    print('Success...')

if __name__ == '__main__':
    PreSelection('las_Ea.pk')

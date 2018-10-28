#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: DumpPKs.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
'System'
import time

'SciLibs'
import numpy as np
import pandas as pd

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
def load_las():
    'Load DataSet'
    print('Loading DataSet...')
    DS = GetDS()

    'Load Pickle'
    print('Loading gsLasso...')
    gs_las = pkload('gslas.pk')
    best_las = gs_las.best_estimator_
    params = best_las.get_params()

    'Get Positive Coef'
    print('Collecting Coefficients...')
    # get feature name and coef
    feanames = DS['fea_names']
    coefs = best_las.coef_
    fea_coef = {}
    for name, coef in zip(feanames, coefs):
        if abs(coef) > 0:
            fea_coef[name] = coef
    # sort fea by abs value
    fc_sorted = sorted(fea_coef.items(), key=lambda d:abs(d[1]), reverse=True)
    fc_dict = {}
    for t in fc_sorted:
        fc_dict[t[0]] =t[1]

    'Dump Pickle'
    print('Dumping LassoPickle...')
    laspk = (params, fc_dict)
    pkdump('BestLas.pk', laspk)

if __name__ == '__main__':
    'total feastures 8454'
    load_las()

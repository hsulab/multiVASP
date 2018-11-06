#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: PerOls.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
'System'
import sys
import time

'SciLib'
import math
import numpy as np
import pandas as pd

'sklearn'
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso

'Data Operations'
import pickle

'MyLibs'
import decorates as deco
from DataOperators import GetDS
from DataOperators import pkload
from DataOperators import pkdump

from PosSelection import PosSelection

def std_yx(y, X):
    'StandardScaler Data'
    scaler_y = StandardScaler().fit(y)
    y_ = scaler_y.transform(y).ravel()
    scaler_X = StandardScaler()
    X_ = scaler_X.fit_transform(X)
    return y_, X_, scaler_y, scaler_X

@deco.timer
def LinearMethod(Etype, a):
    print('-'*20)
    'Pre Data'
    print('Preprocessing %s Data...' %Etype)
    DS = GetDS(Etype)
    y = DS['target']; X = DS['features']
    feanames =DS['fea_names']

    print('Here are ', len(y), ' samples.')
    ts=0; tsra=0
    for m in DS['Etype']:
        if m == 'ts':
            ts += 1
        elif m == 'tsra':
            tsra += 1
    print('TS: ', ts, ' TSra: ', tsra)

    'Scaler Data'
    print('-'*20)
    print('StandScalering Data...')
    y, X, sy, sX = std_yx(y, X)

    'Lasso Regression'
    print('Running Lasso Regression...')
    las = Lasso(alpha=a, fit_intercept=True, normalize=False, \
            max_iter=10000, random_state=None, selection='random')
    las.fit(X, y)
    y_p = las.predict(X)

    print('Model Score')
    mse = metrics.mean_squared_error(y, y_p)
    r2 = metrics.r2_score(y, y_p)
    print('mse --> ', mse)
    print('r2 --> ', r2)

    print('-'*20)
    coefs = las.coef_
    nc = PosSelection(feanames, coefs)
    print('Here are %d Nonzero Coefficients...' %(len(nc.keys())))
    for name, coef in nc.items():
        print(name, ' --> ', coef)
    print('-'*20)
    print('Save Model...')
    pkdump(Etype+'_final.pk', (las, nc))

def main():
    'total feastures 8454'
    LinearMethod('Etsra', 0.037)

if __name__ == '__main__':
    main()

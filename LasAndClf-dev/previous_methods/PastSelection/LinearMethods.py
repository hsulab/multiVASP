#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: LinearMethods.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
'System'
import  sys
sys.path.append('..')
import time

'Plot'
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  

'SciLib'
import math
import numpy as np
import pandas as pd

'sklearn'
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression,Lasso,Ridge

'Data Operations'
import pickle

'MyLibs'
import decorates as deco
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
@deco.timer
def LinearMethod(method, dstype, cvtest=3, ran=None):
    print('-'*20)
    'Pre Data'
    print('Preprocessing Data...')
    DS = GetDS(dstype)
    y = DS['target']; X = DS['features']
    print('Here are ', len(y), ' samples.')
    ts=0; tsra=0
    for m in DS['Etype']:
        if m == 'ts':
            ts += 1
        elif m == 'tsra':
            tsra += 1
    print('TS: ', ts, ' TSra: ', tsra)

    'Scaler Data'
    print('StandScalering Data...')
    y, X, sy, sX = std_yx(y, X)

    def LeastSqure(y, X):# {{{
        'LeastSqure Regression'
        print('Running LeastSqure Regression...')
        # set params
        lsr = LinearRegression(fit_intercept=True, normalize=False, n_jobs=-1)
        # run model
        lsr.fit(X, y)
        
        return lsr# }}}

    'Lasso Regression GridSearch'
    def LassoReg(y, X):
        print('Running Lasso Regression GridSearch...')
        # set gridsearch parameters
        las = Lasso(fit_intercept=True, normalize=False, \
                max_iter=1000, random_state=ran, selection='random')
        param_grid = {'alpha':np.linspace(0.01,1,100)}
        scoring = {'R2':'r2', 'MSE':'neg_mean_squared_error'}
        # run gs
        gs_las = GridSearchCV(las, param_grid=param_grid, \
                scoring=scoring, cv=cvtest, refit='MSE', \
                n_jobs=-1, iid=False, return_train_score=True)
        gs_las.fit(X, y)

        return gs_las

    'Ridge Regression GridSearch'
    def RidgeReg(y, X):
        print('Running Ridge Regression GridSearch...')
        # set gridsearch parameters
        rid = Ridge(fit_intercept=True, normalize=False, max_iter=1000)
        param_grid = {'alpha':np.linspace(0.01,1,100)}
        scoring = {'R^2':'explained_variance', \
                'MSE':metrics.make_scorer(metrics.mean_squared_error)}
        # run gs
        gs_rid = GridSearchCV(rid, param_grid=param_grid, \
                scoring=scoring, cv=cvtest, refit='R^2', \
                n_jobs=-1, return_train_score=True)
        gs_rid.fit(X, y)

        return gs_rid

    if method == 'lsr':
        ret = LeastSqure(y, X)
    elif method == 'las':
        ret = LassoReg(y, X)
    elif method == 'rid':
        ret = RidgeReg(y, X)
    else:
        print('Wrong Case.')
        return 0

    'Model Save'
    print('Saving '+method+' Model... --> %s' %(method+'_'+dstype+'.pk'))
    pkdump(method+'_'+dstype+'.pk', ret)
    print('-'*20)

def main():
    'total feastures 8454'
    LinearMethod('las', 'Ea')

if __name__ == '__main__':
    main()

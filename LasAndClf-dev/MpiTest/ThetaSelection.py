#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: ThetaSelection.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 四 11/ 1 15:22:25 2018
#########################################################################
''
import os

'SciLibs'
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold, RepeatedKFold
from sklearn import metrics
from sklearn.linear_model import Lasso, LinearRegression

'MyLibs'
from DataOps import GetDS

from DataOps import timer
from DataOps import StdScaler
from DataOps import RanFolds
from DataOps import PosSelection
from DataOps import CheckDuplicates

def GetPosCoef(Etype, a):
    'Get Full Data'
    DS = GetDS(Etype)
    y = DS['target']; X=DS['features']
    feanames = DS['fea_names']

    'Lasso with BestAlpha'
    las = Lasso(alpha=a, fit_intercept=True, \
            normalize=False, max_iter=10000, \
            random_state=None, selection='random')

    y_s, X_s, sy, sX = StdScaler(y, X)
    las.fit(X_s, y_s) 
    coefs = las.coef_
    
    'Get Positive Coefficients'
    name_coef = PosSelection(feanames, coefs)

    return name_coef

@timer
def OlsCV(y, X, cv_splits, cv_repeats):
    'y=reduced_y, X=reduced_X'
    ols = LinearRegression(fit_intercept=True, normalize=False)

    ols_MeanMSEs = []
    folds = RanFolds(y, splits=cv_splits, repeats=cv_repeats)
    for kfold in folds.values():
        ols_MSE = 0
        for i in range(len(kfold)):
            train_index = kfold[i][0]
            test_index = kfold[i][1]
            y_train, X_train = y[train_index], X[train_index]
            y_test, X_test = y[test_index], X[test_index]

            ry_s, rX_s, r_sy, r_sX = StdScaler(y_train, X_train)
            ols.fit(rX_s, ry_s)
            ry_p = ols.predict(r_sX.transform(X_test))
            
            ols_MSE += metrics.mean_squared_error(r_sy.transform(y_test), ry_p)

        ols_MeanMSEs.append(ols_MSE/len(kfold))

    return ols_MeanMSEs

def GetBestAlphas():
    slots = 2
    outs = ''
    if os.path.exists('./outs'):
        os.remove('./outs')

    for i in range(slots):
        with open('./slot'+str(i)+'_outs', 'r') as f_out:
            out = f_out.readlines()
        with open('./outs', 'a') as f_outs:
            for line in out:
                f_outs.write(line)

    ''
    BestAlphas = []
    f = os.popen('grep \'BestAlpha\' outs')
    for line in f.readlines():
        line = line.strip('\n')
        BestAlphas.append(float(line.split(' ')[3]))

    return BestAlphas

@timer
def ThetaSelection(Etype='Ets', cv_splits=5, cv_repeats=1, \
        best_alphas=[0.1], test_thetas=np.linspace(0.50, 1, 11)):

    'Theta Selection'
    print('<- Theta Selection START ->')
    theta_MeanMSEs = []
    for theta in test_thetas:
        print('Theta <%0.2f>' %theta)
        'Get Alpha'
        alpha_by_theta = round(np.percentile(best_alphas, theta*100), 3)
        name_coef = GetPosCoef(Etype, alpha_by_theta)

        'OLS'
        reduced_DS = GetDS(Etype, name_coef.keys())
        reduced_y = reduced_DS['target']; reduced_X = reduced_DS['features']
        ols_MeanMSEs = OlsCV(reduced_y, reduced_X, cv_splits, cv_repeats)

        theta_MeanMSEs.append(np.array(ols_MeanMSEs).sum()/len(ols_MeanMSEs))

    CheckDuplicates(theta_MeanMSEs)
    print(theta_MeanMSEs)
    best_index = theta_MeanMSEs.index(min(theta_MeanMSEs))
    best_theta = test_thetas[best_index]

    print('<- Theta Selection DONE ->')
    print('Best Theta --> ', best_theta)
    alpha_by_theta = round(np.percentile(best_alphas, best_theta*100), 3)
    print('Selected Alpha --> ', alpha_by_theta)

from Params import Etype
from Params import tcv_splits
from Params import tcv_repeats
from Params import test_thetas
if __name__ == '__main__':
    'ThetaSelection-Params'
    best_alphas = GetBestAlphas()
    print('<- Theta-Selection Setting ->')
    print('K-Folds Setting --> splits: %d repeats: %d' %(tcv_splits, tcv_repeats))
    print('TestThetas --> From %f to %f Total %d' \
            %(test_thetas[0], test_thetas[-1], len(test_thetas)))

    ThetaSelection(Etype, tcv_splits, tcv_repeats, best_alphas, test_thetas)

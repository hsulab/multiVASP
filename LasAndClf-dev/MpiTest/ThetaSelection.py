#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: ThetaSelection.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 四 11/ 1 15:22:25 2018
#########################################################################
'SciLibs'
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold, RepeatedKFold
from sklearn import metrics
from sklearn.linear_model import Lasso, LinearRegression

'MyLibs'
from DataOperators import GetDS
from DataOperators import pkload
from DataOperators import pkdump

from Decorates import timer

from PosSelection import PosSelection

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

@timer
def ThetaSelection(Etype='Etsra', cv_splits=5, cv_repeats=1, \
        best_alphas=[0.1], test_thetas=np.linspace(0.50, 1, 11)):
    '''
    Important Params
    --> test_thetas
    Etype = 'Etsra'
    test_thetas = np.linspace(0.50, 1, 11)
    cv_splits = 5; cv_repeats = 1
    best_alphas = PercenLas(Etype)
    '''

    'Theta Selection'
    print('<- Theta Selection START ->')
    theta_MeanMSEs = []
    for theta in test_thetas:
        print('Theta <%0.2f>' %theta)
        'Get Alpha'
        alpha_by_theta = round(np.percentile(best_alphas, theta*100), 3)
        name_coef = GetPosCoef('Etsra', alpha_by_theta)

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

if __name__ == '__main__':
    'ThetaSelection-Params'
    cv_splits = 5; cv_repeats = 1
    test_thetas = np.linspace(0.50, 1, 11)
    print('<- Theta-Selection Setting ->')
    print('K-Folds Setting --> splits: %d repeats: %d' %(cv_splits, cv_repeats))
    print('TestThetas --> From %f to %f Total %d' \
            %(test_thetas[0], test_thetas[-1], len(test_thetas)))

    ThetaSelection(Etype, cv_splits, cv_repeats, best_alphas, test_thetas)

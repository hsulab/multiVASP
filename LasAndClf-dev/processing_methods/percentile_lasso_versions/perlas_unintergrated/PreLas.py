#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: PreLas.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
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
from decorates import timer

def std_yx(y, X):
    'StandardScaler Data'
    scaler_y = StandardScaler().fit(y)
    y_ = scaler_y.transform(y)
    scaler_X = StandardScaler()
    X_ = scaler_X.fit_transform(X)
    return y_, X_, scaler_y, scaler_X

def RanCV(y, splits, repeats):
    'Set Params'
    rkf = RepeatedKFold(n_splits=splits, n_repeats=repeats, random_state=0)

    'Get Index'
    folds = {}
    for i in range(1, repeats+1):
        folds[i] = []
    i = 0; j = 0
    for train_index, test_index in rkf.split(y):
        if j % splits == 0:
            i += 1
        folds[i].append([train_index, test_index])
        j += 1

    return folds

@timer
def LasCV(y, X, kfold):
    def las_train(y_train, X_train, a=0.01):
        'Scaler'
        y, X, sy, sX = std_yx(y_train, X_train)

        'Lasso Regression'
        las = Lasso(alpha=a, fit_intercept=True, normalize=False, \
                max_iter=10000, random_state=None, selection='random')
        las.fit(X, y)

        return las, sy, sX

    def las_test(y_test, X_test, las, sy, sX):
        'Scaler Use the Train Scaler\
                That is why i dont use cross_validate'
        y = sy.transform(y_test)
        X = sX.transform(X_test)

        'Predict'
        y_p = las.predict(X)
        MSE = metrics.mean_squared_error(y, y_p)
        return MSE

    def CalcMeanMSE(MSEs):
        'Mean-MSE'
        MSEs = np.array(MSEs)
        n_MSE = len(MSEs)
        sum_MSE = MSEs.sum()
        mean_MSE = sum_MSE / n_MSE
        
        return mean_MSE

    def CalcStdMSE(MSEs, mean_MSE):
        MSEs = np.array(MSEs)
        n_MSE = len(MSEs)
        sum_MSE2 = (MSEs * MSEs).sum()
        mean_MSE2 = sum_MSE2 / n_MSE
        # std
        std_MSE = (mean_MSE2-mean_MSE**2)**0.5
        return std_MSE

    'LasCV'
    MeanMSEs = [] 
    alphas = np.linspace(0.01, 1, 100)
    for a in alphas:
        a_MSEs = []
        for i in range(len(kfold)):
            'Get train and test set'
            train_index = kfold[i][0]
            test_index = kfold[i][0]
            y_train, X_train = y[train_index], X[train_index]
            y_test, X_test = y[test_index], X[test_index]
            
            'Train and Test'
            las, sy, sX = las_train(y_train, X_train, a)
            a_MSE = las_test(y_test, X_test, las, sy, sX)
            a_MSEs.append(a_MSE)
        MeanMSEs.append(CalcMeanMSE(a_MSEs))
    best_index = MeanMSEs.index(min(MeanMSEs)) 

    print('LasCV-->BestAlpha: ', alphas[best_index])

@timer
def PreLas():
    'Pre Data'
    print('Preparing Data...')
    DS = GetDS('Etsra')
    y = DS['target']; X = DS['features']

    'Get RepeatedKFolds'
    print('Generating Folds...')
    folds = RanCV(y, splits=5, repeats=2)

    ''
    print('*'*20)
    print('< Percentile-Lasso > ...')
    count = 1
    for fold in folds.values(): 
        print('Fold <%d>' %count)
        LasCV(y, X, fold)
        count += 1
    print('*'*20)

if __name__ == '__main__':
    'total feastures 6662'
    PreLas()

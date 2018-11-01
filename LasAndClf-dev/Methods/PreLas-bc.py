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

from PosSelection import PosSelection

def StdScaler(y, X):
    'StandardScaler Data'
    scaler_y = StandardScaler().fit(y)
    y_ = scaler_y.transform(y)
    scaler_X = StandardScaler()
    X_ = scaler_X.fit_transform(X)
    return y_, X_, scaler_y, scaler_X

def RanFolds(y, splits, repeats):
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
def LasCV(y, X, kfold, alphas):
    def las_train(y_train, X_train, a=0.01):
        'Scaler'
        y, X, sy, sX = StdScaler(y_train, X_train)

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
    #alphas = np.linspace(0.01, 1, 100)
    for a in alphas:
        a_MSEs = []
        for i in range(len(kfold)):
            'Get train and test set'
            train_index = kfold[i][0]
            test_index = kfold[i][1]
            y_train, X_train = y[train_index], X[train_index]
            y_test, X_test = y[test_index], X[test_index]
            
            'Train and Test'
            las, sy, sX = las_train(y_train, X_train, a)
            a_MSE = las_test(y_test, X_test, las, sy, sX)
            a_MSEs.append(a_MSE)

        MeanMSEs.append(CalcMeanMSE(a_MSEs))

    'Get Best'
    best_index = MeanMSEs.index(min(MeanMSEs)) 
    best_alpha = alphas[best_index]

    'Here y and X are original data, which should be std.'
    best_las, sy, sX = las_train(y, X, best_alpha)
    r2_score = round(best_las.score(sX.transform(X), sy.transform(y)), 2)

    coefs = best_las.coef_
    pos_coefs = []
    for coef in coefs:
        if abs(coef) > 0:
            pos_coefs.append(coef)

    n_poscoef = len(pos_coefs)

    print('LasCV-->BestAlpha: ', best_alpha)
    print('OneShot-->BestR2Score: ', r2_score)
    print('OneShot-->N_PosCoefs: ', n_poscoef)

    return best_alpha

@timer
def PreLas():
    '''
    Important Parameters:
    --> splits, repeats, test_alphas,
    '''

    'Pre Data'
    print('Preparing Data...')
    DS = GetDS('Etsra')
    y = DS['target']; X = DS['features']

    'Get RepeatedKFolds'
    print('Generating Folds...')
    folds = RanFolds(y, splits=5, repeats=10)

    ''
    print('*'*20)
    print('< Percentile-Lasso > ...')
    best_alphas = []
    test_alphas = np.linspace(0.01, 0.1, 10)
    count = 1
    for fold in folds.values(): 
        print('-'*20)
        print('Fold <%d>' %count)
        best_alpha = LasCV(y, X, fold, test_alphas)
        best_alphas.append(best_alpha)
        count += 1
        print('-'*20)
    print('*'*20)

    return best_alphas

def ThetaSelection():
    ''
    best_alphas = PreLas()

    DS = GetDS('Etsra')
    y = DS['target']; X=DS['features']

    'Percentile Lasso'
    best_alphas_sorted = sorted(best_alphas)

    thetas = np.linspace(0.50, 1, 11)
    for theta in thetas:
        per_index = int(theta*len(best_alphas))
        alpha_by_theta = best_alphas_sorted[per_index]

        'Lasso'
        las = Lasso(alpha=alpha_by_theta, fit_intercept=True, \
                normalize=False, max_iter=10000, \
                random_state=None, selection='random')
        y_s, X_s, sy, sX = StdScaler(y, X)
        las.fit(y_s, X_s) 
        coefs = las.coef_

        feanames = DS['fea_names']
        name_coef = PosSelection(feanames, coefs)

        'OLS'
        reduced_DS = GetDS('Etsra', name_coef.keys())
        reduced_y = reduced_DS['target']; reduced_X = reduced_DS['features']
        ols = LinearRegression(fit_intercept=True, normalize=False)

        # CV
        r_y_s, r_X_s, r_sy, r_sX = StdScaler(reduced_y, reduced_X)
        ols.fit(r_y_s, r_X_s)
        
        folds = RanFolds(y, splits=5, repeats=1)

        ''
        print('*'*20)
        print('< Theta-Selection > ...')
        count = 1
        for fold in folds.values(): 
            print('-'*20)
            print('Fold <%d>' %count)
            count += 1
            print('-'*20)
        print('*'*20)

if __name__ == '__main__':
    'total feastures 6662'
    ThetaSelection()

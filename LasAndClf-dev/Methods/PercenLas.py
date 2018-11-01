#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: PercenLas.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
'System'

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

def CheckDuplicates(alist):
    if len(alist) != len(set(alist)):
        print('Warning -- Have Duplicates !!!')


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

    'Get Best, having same aloha is fine.'
    #CheckDuplicates(MeanMSEs)
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

    print('LasCV --> BestAlpha: ', best_alpha)
    print('OneShot --> BestR2Score: ', r2_score)
    print('OneShot --> N_PosCoefs: ', n_poscoef)

    return best_alpha

@timer
def PercenLas(Etype='Etsra', cv_splits=5, cv_repeats=5, \
        test_alphas=np.linspace(0.01, 0.1, 10)):
    '''
    Important Parameters:
    --> splits, repeats, test_alphas
    cv_splits = 5; cv_repeats = 5
    test_alphas = np.linspace(0.01, 0.1, 10)
    '''

    'Pre Data'
    print('<- Preparing Data for Percentile-LASSO ->')
    DS = GetDS(Etype)
    y = DS['target']; X = DS['features']

    'Get RepeatedKFolds'
    print('<- Generating %d [%d-Fold]s ->' %(cv_repeats, cv_splits))
    folds = RanFolds(y, splits=cv_splits, repeats=cv_repeats)

    ''
    print('*'*20)
    print('<- Percentile-LASSO START -> ...')
    best_alphas = []; count = 1
    for fold in folds.values(): 
        print('-'*20)
        print('Fold <%d>' %count)
        best_alpha = LasCV(y, X, fold, test_alphas)
        best_alphas.append(best_alpha)
        count += 1
        print('-'*20)
    print('*'*20)
    print('<- Percentile-LASSO DONE -> ...')

    return best_alphas

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
def ThetaSelection(Etype='Etsra', cv_splits=5, cv_repeats=5, \
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
    'total feastures 6662'
    Etype = 'Etsra'

    'PercenLas-Params'
    cv_splits = 5; cv_repeats = 5
    test_alphas = np.linspace(0.01, 0.1, 10)
    print('<- Percentile-LASSO Setting ->')
    print('K-Folds Setting --> splits: %d repeats: %d' %(cv_splits, cv_repeats))
    print('TestAlphs --> From %f to %f Total %d' \
            %(test_alphas[0], test_alphas[-1], len(test_alphas)))

    best_alphas = PercenLas(Etype, cv_splits, cv_repeats, \
            test_alphas)

    'ThetaSelection-Params'
    cv_splits = 5; cv_repeats = 1
    test_thetas = np.linspace(0.50, 1, 11)
    print('<- Theta-Selection Setting ->')
    print('K-Folds Setting --> splits: %d repeats: %d' %(cv_splits, cv_repeats))
    print('TestThetas --> From %f to %f Total %d' \
            %(test_thetas[0], test_thetas[-1], len(test_thetas)))

    ThetaSelection(Etype, cv_splits, cv_repeats, best_alphas, test_thetas)

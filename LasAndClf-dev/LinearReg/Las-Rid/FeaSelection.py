#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: FeaSelection.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
'System'
import time

'SciLibs'
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from sklearn import metrics
from sklearn.linear_model import LinearRegression

'MyLibs'
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

def cv_yx(y, n):
    kf = KFold(n_splits=n)
    folds_index = []
    for train_index, test_index in kf.split(y):
        folds_index.append([train_index, test_index])
    return folds_index

logtime = time.strftime("%Y%m%d")
def reg_assemble(y, X):
    def reg_train(y, X):
        'Scaler'
        y, X, sy, sX = std_yx(y.reshape(-1,1), X)

        'Linear Regression'
        model = LinearRegression(fit_intercept=True, normalize=False, n_jobs=-1)
        model.fit(X, y)
        return model, sy, sX

    def reg_test(y, X, model, sy, sX):
        'Scaler Use the Train Scaler\
                That is why i dont use cross_validate'
        y = sy.transform(y.reshape(-1,1))
        X = sX.transform(X)

        'Predict'
        y_p = model.predict(X)
        MSE = metrics.mean_squared_error(y, y_p)
        return MSE

    'K-Folds'
    n=3; folds_index = cv_yx(y, n); MSEs = []
    for i in range(n):
        fold=folds_index[i]
        y_train, X_train = y[fold[0]], X[fold[0]]
        y_test, X_test = y[fold[1]], X[fold[1]]

        'Train and Test'
        model, sy, sX = reg_train(y_train, X_train)
        MSE = reg_test(y_test, X_test, model, sy, sX)
        MSEs.append(MSE)

    'Mean-MSE and Std-MSE'
    MSEs = np.array(MSEs)
    n_MSEs = len(MSEs)
    # sum
    sum_MSEs = MSEs.sum()
    sum_MSEs2 = (MSEs * MSEs).sum()
    # mean
    mean_MSE = sum_MSEs / n_MSEs
    mean_MSE2 = sum_MSEs2 / n_MSEs
    # std
    std_MSE = (mean_MSE2-mean_MSE**2)**0.5
    return mean_MSE, std_MSE

def FeaSelection(pkfile):
    'Pre Data'
    print('Preparing Data...')
    params, feas = pkload(pkfile)
    DS = GetDS('Ets', feas.keys())
    y = DS['target']; X = DS['features']

    'Feature Selection'
    print('Selecting Features...')
    mean_MSEs = []; std_MSEs = []
    feas_number = len(X[0])
    for i in range(feas_number):
        X_slice = []
        for j in range(i+1):
            X_slice.append(X.T[j])
        X_slice = np.array(X_slice).T
        mean_MSE, std_MSE = reg_assemble(y, X_slice)
        mean_MSEs.append(mean_MSE)
        std_MSEs.append(std_MSE)

    'Get Feas Name'
    names = list(feas.keys())
    best_index = mean_MSEs.index(min(mean_MSEs))
    best_feas = {}
    for i in range(best_index+1):
        best_feas[names[i]] = feas[names[i]]

    'Dump Pickle'
    print('Saving pk...')
    bestreg_pk = (feas, best_feas, mean_MSEs, std_MSEs)
    pkdump('Best'+pkfile.strip('PosCoef'), bestreg_pk) 
    print('Success...')

if __name__ == '__main__':
    'total feastures 6662'
    FeaSelection('PosCoef_las_Ea.pk')

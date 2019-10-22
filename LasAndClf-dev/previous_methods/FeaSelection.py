#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: FeaSelection.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
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

def cv_yx(y, n):
    kf = KFold(n_splits=n, shuffle=True, random_state=0)
    folds_index = []
    for train_index, test_index in kf.split(y):
        folds_index.append([train_index, test_index])
    return folds_index

def reg_assemble(y, X):
    def reg_train(y, X):
        'Linear Regression'
        model = LinearRegression(fit_intercept=True, normalize=False, n_jobs=-1)
        model.fit(X, y)
        return model

    def reg_test(y, X, model):
        'Predict'
        y_p = model.predict(X)
        MSE = metrics.mean_squared_error(y, y_p)
        return MSE

    'K-Folds'
    n=5; folds_index = cv_yx(y, n); MSEs = []
    for i in range(n):
        fold=folds_index[i]
        y_train, X_train = y[fold[0]], X[fold[0]]
        y_test, X_test = y[fold[1]], X[fold[1]]

        'Train and Test'
        model = reg_train(y_train, X_train)
        MSE = reg_test(y_test, X_test, model)
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

def FeaSelection():
    'Pre Data'
    print('Preparing Data...')
    las, nc = pkload('Ets_final.pk')
    DS = GetDS('Ets', nc.keys())
    y = DS['target']; X = DS['features']

    names = list(nc.keys())

    for i in range(len(names)):
        t = names[i].split('_')[0]
        if t == 'h':
            X.T[i] = np.sin((X.T[i]/2)**2)
        elif t == 'a':
            X.T[i] = X.T[i]**2

    'Feature Selection'
    print('Selecting Features...')
    mean_MSEs = []; std_MSEs = []; r2s = []
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
    best_index = mean_MSEs.index(min(mean_MSEs))
    best_feas = {}
    for i in range(best_index+1):
        best_feas[names[i]] = nc[names[i]]

    'Dump Pickle'
    print('Saving pk...')
    bestreg_pk = (nc, best_feas, mean_MSEs, std_MSEs)
    pkdump('Best_Ets.pk', bestreg_pk) 
    print('Success...')

if __name__ == '__main__':
    FeaSelection()

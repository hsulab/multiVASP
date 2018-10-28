#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: SelectedReg.py
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
from DataOperators import pkload
from DataOperators import pkdump

'Wait to be change.'
def pre_yx():
    'Load Pickle'
    params, feas = pkload('BestLas.pk')

    'Get Total DataSet and Top Features'
    df = pd.read_csv('../../CH4_DataSet.csv', index_col = 0)

    'Get index and values'
    yx_indexs = df.iloc[:,range(4)] # 'name', 'mtype', 'E_ts', 'E_tsra'
    yx_vals = df.loc[:, feas.keys()] # E and Geo

    'Get DataSet'
    DS = {}
    DS['name'] = yx_indexs.iloc[:,range(1)].values
    DS['mtype'] = yx_indexs.iloc[:,range(1,2)].values
    DS['target'] = df.loc[:, 'mE'].values
    DS['features'] = yx_vals.values

    return feas, DS
###
def std_yx(y, X):
    'StandardScaler Data'
    scaler_y = StandardScaler().fit(y)
    y_ = scaler_y.transform(y).ravel()
    scaler_X = StandardScaler()
    X_ = scaler_X.fit_transform(X)
    return y_, X_, scaler_y, scaler_X
##
def cv_yx(y, n):
    kf = KFold(n_splits=n)
    folds_index = []
    for train_index, test_index in kf.split(y):
        folds_index.append([train_index, test_index])
    return folds_index
###
logtime = time.strftime("%Y%m%d")
def reg_assemble(y, X):
    def reg_train(y, X):
        'Scaler'
        y, X, sy, sX = std_yx(y.reshape(-1,1), X)

        'Linear Regression'
        model = LinearRegression()
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
###
def cvreg_yx():
    'Pre Data'
    feas, DS = pre_yx() # feas is dict {name:coef}
    y = DS['target']; X = DS['features']

    'Feature Selection'
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
    min_index = mean_MSEs.index(min(mean_MSEs))
    best_feas = []; best_coefs = []
    for i in range(min_index):
        best_feas.append(names[i])
        best_coefs.append(feas[names[i]])

    'Dump Pickle'
    bestreg_pk = (feas, best_feas, best_coefs, \
            mean_MSEs, std_MSEs)
    pkdump('bestreg-test.pk', bestreg_pk) 
###
if __name__ == '__main__':
    'total feastures 8454'
    cvreg_yx()

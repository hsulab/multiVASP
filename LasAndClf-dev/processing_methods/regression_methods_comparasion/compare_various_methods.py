#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import os
import time

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  

import numpy as np
import pandas as pd

from sklearn import metrics 
from sklearn.linear_model import LinearRegression, Lasso, Ridge 

from sklearn import svm 

from sklearn.preprocessing import StandardScaler 
from sklearn import tree
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor 
from sklearn.model_selection import GridSearchCV, KFold, RepeatedKFold 


"""
paper figure 9
"""


def generate_dataset_from_csv(target_name='Ea', fea_names='all'):
    """
    Description:
        Return a dictionary with mechanism types, target(activation energy),
        features(adsorption energies and geometrical descriptors) and their names.
    """
    # from csv file to dataframe 
    if os.path.exists(DS_CSV):
        df = pd.read_csv(DS_CSV, index_col=0)
    else:
        raise ValueError('DataSet CSV does not exist.')

    # choose different targets: preferred or specific activation energy (three kinds)
    if target_name == 'Ea':
        df = df
        E = 'mE'
    elif target_name == 'Edelta':
        df = df.loc[df.loc[:,'E_ts']!='np.nan', :]
        df = df.loc[df.loc[:,'E_tsra']!='np.nan', :]

        df.loc[:,'E_ts'] = df.loc[:,'E_ts'].values.astype(np.float64) - \
                df.loc[:,'E_tsra'].values.astype(np.float64)
        E = 'E_ts'
    elif target_name == 'Eclf':
        df = df.loc[df.loc[:,'E_ts']!='np.nan', :]
        df = df.loc[df.loc[:,'E_tsra']!='np.nan', :]
        E = 'mE'
    elif target_name == 'Ets':
        df = df.loc[df.loc[:,'E_ts']!='np.nan', :]
        E = 'E_ts'
    elif target_name == 'Etsra':
        df = df.loc[df.loc[:,'E_tsra']!='np.nan', :]
        E = 'E_tsra'

    # 'name', 'mtype', 'E_ts', 'E_tsra', Ea: min(E_ts, E_tsra)
    nodescriptors = ['name', 'mtype', 'E_ts', 'E_tsra', 'Ea']
    indexs_cols = df.iloc[:, 0:len(nodescriptors)]

    # choose number of descriptors (E_Hab3, E_CH3ab, Geos, ...)
    if fea_names == 'all':
        vals_cols = df.iloc[:,range(len(nodescriptors),len(df.columns))]
    else:
        vals_cols = df.loc[:, fea_names]

    # Get DataSet
    DS = {}

    DS['Etype'] = indexs_cols.loc[:, 'mtype'].values
    DS['target'] = indexs_cols.loc[:,E].values.reshape(-1,1).astype(np.float64)
    DS['fea_names'] = vals_cols.columns.values
    DS['features'] = vals_cols.values.astype(np.float64)

    return DS


def randomize_repeated_folds(y, splits, repeats):
    """
    Description:
        Get randomized k-folds from sklearn function, 
        and arrange them in dict.
    """
    # get randomized k-folds
    rkf = RepeatedKFold(n_splits=splits, n_repeats=repeats, random_state=0)

    # rearrange folds
    folds = {}
    for i in range(1, repeats+1):
        folds[i] = []

    i, j = 0, 0
    for train_index, test_index in rkf.split(y):
        if j % splits == 0:
            i += 1
        folds[i].append([train_index, test_index])
        j += 1

    return folds


def stardard_scaling(y, X):
    """
    Description:
        StandardScaler Data.
    In:
        unnormalized data y and X.
    Out:
        normalized data: y_s and X_s.
        scaler function: s_y and s_X
    """
    # scale y
    scaler4y = StandardScaler().fit(y)
    y_scalered = scaler4y.transform(y)

    # scale X
    scaler4X = StandardScaler()
    X_scalered = scaler4X.fit_transform(X)

    return y_scalered, X_scalered, scaler4y, scaler4X


def plot_gbdt_classification():
    # feature names 
    '''
    feanames = ['E_CH3ab', 'E_Hab3', \
            'a_O2-M4-C_CH3ab', 'h_O2-C-M4-H1_CH3ab', 'd_H1-C_CH3ab', \
            'h_O2-H1-M4-C_CH3ab', 'a_O2-M4-H1_Hab3'] 
    feanames = ['a_O2-M4-C_CH3ab', 'h_O2-C-M4-H1_CH3ab', 'd_H1-C_CH3ab', \
            'h_O2-H1-M4-C_CH3ab', 'a_O2-M4-H1_Hab3'] 
    '''

    # prepare dataset 
    DS = generate_dataset_from_csv('Etsra')
    y, X = DS['target'], DS['features']
    folds = list(randomize_repeated_folds(y, 5, 1).values())[0] 

    methods = {}

    methods['ols'] = LinearRegression(fit_intercept=True, normalize=False)
    methods['ridge'] = Ridge(alpha=0.01, fit_intercept=True, normalize=False, \
            max_iter=10000, tol=1e-6, random_state=None)
    methods['lasso'] = Lasso(alpha=0.01, fit_intercept=True, normalize=False, \
            max_iter=10000, random_state=None, selection='random')

    methods['svm'] = svm.SVR(kernel='rbf', tol=1e-6) 
    methods['gbr'] = GradientBoostingRegressor(n_estimators=100)

    for name, method in methods.items(): 
        train_MSEs, test_MSEs = [], [] 
        train_r2s, test_r2s = [], [] 
        for train, test in folds:
            y_train, X_train = y[train], X[train] 
            y_s, X_s, s4y, s4X = stardard_scaling(y_train, X_train) 
            method.fit(X_s, y_s.ravel()) 

            y_p = s4y.inverse_transform(method.predict(X_s))
            train_MSEs.append(metrics.mean_squared_error(y_train, y_p))
            train_r2s.append(metrics.r2_score(y_train, y_p))

            # test 
            y_test, X_test = y[test], X[test] 
            y_s, X_s = s4y.transform(y_test), s4X.transform(X_test) 

            y_p = s4y.inverse_transform(method.predict(X_s)) 
            test_MSEs.append(metrics.mean_squared_error(y_test, y_p))
            test_r2s.append(metrics.r2_score(y_test, y_p))


        print(name)
        print('mean: %.4f %.2f' %(np.mean(train_MSEs), np.mean(train_r2s)))
        print('var: %.4f %.2f' %(np.var(train_MSEs), np.var(train_r2s)))

        print('mean: %.4f %.2f' %(np.mean(test_MSEs), np.mean(test_r2s)))
        print('var: %.4f %.2f' %(np.var(test_MSEs), np.var(test_r2s)))


if __name__ == '__main__':
    DS_CSV = './CH4_10.csv'
    plot_gbdt_classification() 

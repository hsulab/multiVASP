#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: DataOperators.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六 10/27 21:07:14 2018
#########################################################################
''
import time

'SciLibs'
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import RepeatedKFold

def timer(func):
    'Count Time'
    def inner(*args, **kwargs): #1
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(str(func.__name__)+' TakeTime: ', round(end-start, 4), 's')
         
        return ret #2

    return inner

def CheckDuplicates(alist):
    if len(alist) != len(set(alist)):
        print('Warning -- Have Duplicates !!!')

def StdScaler(y, X):
    'StandardScaler Data'
    scaler4y = StandardScaler().fit(y)
    y_scalered = scaler4y.transform(y)

    scaler4X = StandardScaler()
    X_scalered = scaler4X.fit_transform(X)

    return y_scalered, X_scalered, scaler4y, scaler4X

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

def GetDS(dstype, n_feas='all'):
    'Get Data and Index'
    df = pd.read_csv('../Data/CH4_DataSet.csv', index_col=0)
    if dstype == 'Ea':
        df = df
        En = 4
    elif dstype == 'Ets':
        df = df.loc[df.loc[:,'E_ts']!='np.nan', :]
        En = 2
    elif dstype == 'Etsra':
        df = df.loc[df.loc[:,'E_tsra']!='np.nan', :]
        En = 3

    ''
    # 'name', 'mtype', 'E_ts', 'E_tsra', Ea: min(E_ts, E_tsra)
    indexs_cols = df.iloc[:,range(5)]
    # E_Hab3, E_CH3ab, Geos
    if n_feas == 'all':
        vals_cols = df.iloc[:,range(5,len(df.columns))]
    else:
        vals_cols = df.loc[:, n_feas]

    'Get DataSet'
    DS = {}
    DS['Etype'] = indexs_cols.loc[:, 'mtype'].values
    DS['target'] = indexs_cols.iloc[:, En].values.reshape(-1,1).astype(np.float64)
    DS['features'] = vals_cols.values.astype(np.float64)
    DS['fea_names'] = vals_cols.columns.values

    return DS

if __name__ == '__main__':
    GetDS('Ea')

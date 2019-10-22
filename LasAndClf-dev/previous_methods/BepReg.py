#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

'System'
import sys

'SciLibs'
import numpy as np
import pandas as pd

'sklearn'
from sklearn import metrics
from sklearn.linear_model import LinearRegression

'MyLibs'
from DataOperators import pkdump

def GetDS(dstype):
    'Get Total DataSet'
    df = pd.read_csv('../Data/fE_CH4.csv', index_col = 0)
    feas_E = ['E_ts', 'E_tsra', 'E_Hab2','E_Hab3','E_CH3ab','E_CH3ab2']

    'Get index and values'
    if dstype == 'ts':
        DS = {}
        df = df.loc[df.loc[:,'E_ts']!='np.nan', :]
        df = df.loc[df.loc[:,'E_CH3ab']!='np.nan', :]
        df = df.loc[df.loc[:,'E_CH3ab2']!='np.nan', :]
        DS['target'] = df.loc[:, 'E_ts'].values.astype('float').reshape(-1,1)
        DS['Hab2_CH3ab'] = (df.loc[:, 'E_Hab2'].values.astype('float') + \
                df.loc[:, 'E_CH3ab'].values.astype('float')).reshape(-1,1)
        DS['Hab2_CH3ab2'] = (df.loc[:, 'E_Hab2'].values.astype('float') + \
                df.loc[:, 'E_CH3ab2'].values.astype('float')).reshape(-1,1)
        DS['Hab3_CH3ab'] = (df.loc[:, 'E_Hab3'].values.astype('float') + \
                df.loc[:, 'E_CH3ab'].values.astype('float')).reshape(-1,1)
        DS['Hab3_CH3ab2'] = (df.loc[:, 'E_Hab3'].values.astype('float') + \
                df.loc[:, 'E_CH3ab2'].values.astype('float')).reshape(-1,1)
    else:
        DS = {}
        df = df.loc[df.loc[:,'E_tsra']!='np.nan', :]
        df = df.loc[df.loc[:,'name']!='pureMnO2', :]
        DS['target'] = df.loc[:, 'E_tsra'].values.astype('float').reshape(-1,1)
        DS['Hab2'] = df.loc[:, 'E_Hab2'].values.astype('float').reshape(-1,1)
        DS['Hab3'] = df.loc[:, 'E_Hab3'].values.astype('float').reshape(-1,1)

    return DS

def BepReg(dstype):
    'Pre and Scaler Data'
    print('Loading Data...')
    DS = GetDS(dstype)
    y = DS['target']
    DS.pop('target')

    'LinearRegression'
    for Xname in DS.keys():
        print('Calcing '+Xname+'...')
        X = DS[Xname]
        model = LinearRegression(fit_intercept=True, normalize=False, n_jobs=-1)
        model.fit(X, y)
        y_p = model.predict(X)
        r2 = metrics.r2_score(y, y_p)
        mse = metrics.mean_squared_error(y, y_p)
        pkdump(dstype+'_'+Xname+'.pk', (y, y_p, r2, mse))
    print('Success...')

if __name__ == '__main__':
    BepReg('tsra')

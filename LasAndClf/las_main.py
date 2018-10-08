#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: main_lasso.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
import time
### plot
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  
### scilibs
import numpy as np
import pandas as pd
'sklearn'
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso,LassoLars,LassoCV,LassoLarsCV
from sklearn.model_selection import KFold
### mylibs
import decorates as deco
###
def pre_yx():
    'Get Data and Index'
    df = pd.read_csv('./CH4_DataSet.csv', index_col=0)
    yx_indexs = df.iloc[:,range(4)] # 'name', 'mtype', 'E_ts', 'E_tsra'
    yx_vals = df.iloc[:,range(4,len(df.columns))] # E and Geo
    'Get DataSet'
    DS = {}
    DS['target'] = yx_vals.iloc[:,range(1)].values
    DS['features'] = yx_vals.iloc[:,range(1,len(yx_vals.columns))].values
    DS['fea_names'] = yx_vals.columns[1:].values
    return DS
###
def std_yx(y, X):
    'StandardScaler Data'
    scaler_y = StandardScaler().fit(y)
    y_ = scaler_y.transform(y).ravel()
    scaler_X = StandardScaler()
    X_ = scaler_X.fit_transform(X)
    return y_, X_, scaler_y, scaler_X
###
logtime = time.strftime("%Y%m%d")
@deco.printer(r'./Logs/las_'+logtime+'.txt', 'out')
def las_yx():
    'Pre Data'
    DS = pre_yx()
    y = DS['target']
    X = DS['features']
    'Scaler Data'
    y, X, sy, sX = std_yx(y, X)
    'Lasso Regression'
    model = LassoLars(alpha=0.01, eps=1e-6, max_iter=10000)
    model.fit(X, y)
    'Model Settings'
    model_params = model.get_params()
    'Model Predict'
    y_p = model.predict(X)
    model_params['Score__R2'] = round(metrics.explained_variance_score(y, y_p))
    'Coef and Feas'
    fea_coef = {}
    feas = DS['fea_names']
    coefs = model.coef_
    for fea, coef in zip(feas, coefs):
        fea_coef[fea] = round(coef, 8)
    return model_params, fea_coef
###
def cv_yx(y, n):
    kf = KFold(n_splits=n)
    folds_index = []
    for train_index, test_index in kf.split(y):
        folds_index.append([train_index, test_index])
    return folds_index
###
if __name__ == '__main__':
    'total feastures 8454'
    las_yx()

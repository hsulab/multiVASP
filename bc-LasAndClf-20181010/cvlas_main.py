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
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso,LassoLars,LassoCV,LassoLarsCV
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
#@deco.printer(r'./Logs/las_'+logtime+'.txt', 'out')
def las_yx():
    'Pre Data'
    DS = pre_yx()
    y = DS['target']
    X = DS['features']
    'Scaler Data'
    y, X, sy, sX = std_yx(y, X)
    'Lasso Regression'
    las = LassoLars(fit_intercept=True, normalize=False, max_iter=10000)
    param_grid = {'alpha':np.linspace(0,1,5)}
    scoring = {'R^2':'r2', 'MSE':metrics.make_scorer(metrics.mean_squared_error)}
    model = GridSearchCV(las, param_grid=param_grid, scoring=scoring, cv=5, refit='R^2', n_jobs=-1, return_train_score=True)
    model.fit(X, y)
    'Model Settings'
    'Model Results'
    print(model.cv_results_)
###
if __name__ == '__main__':
    'total feastures 8454'
    las_yx()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: main_lasso.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
import sys
import time
### scilibs
import numpy as np
import pandas as pd
'sklearn'
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso,LassoLars,LassoCV,LassoLarsCV
from sklearn.model_selection import KFold
''
import pickle
### mylibs
sys.path.append('..')
import decorates as deco
###
def pre_yx():
    'Get Data and Index'
    df = pd.read_csv('../CH4_DataSet.csv', index_col=0)
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
def load_las():
    'Load DataSet'
    print('Loading DataSet...')
    DS = pre_yx()

    'Load Pickle'
    print('Loading gsLasso...')
    with open('./Log/gslas.pk', 'rb') as f:
        gs_las = pickle.load(f)
    best_las = gs_las.best_estimator_
    params = best_las.get_params()

    'Get Positive Coef'
    print('Collecting Coefficients...')
    # get feature name and coef
    feanames = DS['fea_names']
    coefs = best_las.coef_
    fea_coef = {}
    for name, coef in zip(feanames, coefs):
        if abs(coef) > 0:
            fea_coef[name] = coef
    # sort fea by abs value
    fc_sorted = sorted(fea_coef.items(), key=lambda d:abs(d[1]), reverse=True)
    fc_dict = {}
    for t in fc_sorted:
        fc_dict[t[0]] =t[1]

    'Dump Pickle'
    print('Dumping LassoPickle...')
    laspk = (params, fc_dict)
    with open('./Log/las.pk', 'wb') as f:
        pickle.dump(laspk, f)
###
if __name__ == '__main__':
    'total feastures 8454'
    load_las()

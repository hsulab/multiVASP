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
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso,LassoLars,LassoCV,LassoLarsCV
from sklearn.model_selection import KFold
### mylibs
import collectdata as cd
import decorates as deco
###
def pre_yx(n_geofeas):
    'Get Data and Index'
    df = cd.get_data(n_geofeas)
    yx_indexs = df.iloc[:,range(2)] # 'name' and 'mtype'
    yx_vals = df.iloc[:,range(2,len(df.columns))] # E and Geo
    'Get DataSet'
    DataSet = {}
    DataSet['target'] = yx_vals.iloc[:,range(1)].values
    DataSet['features'] = yx_vals.iloc[:,range(1,len(yx_vals.columns))].values
    DataSet['fea_names'] = yx_vals.columns[1:]
    return DataSet
###
def std_yx(n_geofeas):
    'Pre Data'
    DS = pre_yx(n_geofeas)
    y = DS['target']
    X = DS['features']
    'StandardScaler Data'
    scaler_y = StandardScaler().fit(y)
    y_ = scaler_y.transform(y)
    scaler_X = StandardScaler()
    X_ = scaler_X.fit_transform(X)
    DS['target'] = y_.ravel()
    DS['features'] = X_
    return DS
###
def cv_yx(yx):
    kf = KFold(n_splits=3)
    for train, test in kf.split(yx):
        print("%s %s" % (train, test))
###
@deco.printer(r'./Logs/haha3.test', 'out')
def data_lasso(n_geofeas):
    'Pre and Scaler Data'
    DS = std_yx(n_geofeas)
    y = DS['target']
    X = DS['features']
    'Lasso Regression'
    model = LassoCV(cv=5, max_iter=10000)
    model.fit(X, y)
    'Model Settings'
    model_params = model.get_params()
    model_params['Alpha'] = round(model.alpha_, 8)
    model_params['Iters'] = model.n_iter_
    model_params['Score'] = round(model.score(X,y), 8)
    'Coef and Feas'
    fea_coef = {}
    feas = DS['fea_names']
    coefs = model.coef_
    for fea, coef in zip(feas, coefs):
        fea_coef[fea] = round(coef, 8)
    return model_params, fea_coef
###
if __name__ == '__main__':
    'total feastures 8454'
    data_lasso(8454)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: reg_main.py
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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
### mylibs
import decorates as deco
import readlog as rl
###
def pre_yx():
    'Get Total DataSet and Top Features'
    las = './Logs/las_20181008.txt'
    df = pd.read_csv('./CH4_DataSet.csv', index_col = 0)
    feas_top = rl.read_las(las, 100) # dict
    feas_col = []
    for key in feas_top.keys():
        feas_col.append(key)
    'Get index and values'
    yx_indexs = df.iloc[:,range(4)] # 'name', 'mtype', 'E_ts', 'E_tsra'
    yx_vals = df.loc[:, feas_col] # E and Geo
    'Get DataSet'
    DS = {}
    DS['name'] = yx_indexs.iloc[:,range(1)].values
    DS['mtype'] = yx_indexs.iloc[:,range(1,2)].values
    DS['target'] = df.loc[:, 'mE'].values
    DS['features'] = yx_vals.values
    DS['fea_names'] = feas_col
    return DS
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
def reg_yx(y, X):
    'Train'
    def reg_train(y, X):
        'Scaler'
        y, X, sy, sX = std_yx(y.reshape(-1,1), X)
        'Linear Regression'
        model = LinearRegression()
        model.fit(X, y)
        '''Coef and Feas'
        coefs = model.coef_
        inter = round(model.intercept_)'''
        return model, sy, sX
    'Test'
    def reg_test(y, X, model, sy, sX):
        'Scaler'
        y = sy.transform(y.reshape(-1,1))
        X = sX.transform(X)
        'Predict'
        y_p = model.predict(X)
        MSE = metrics.mean_squared_error(y, y_p)
        return MSE
    'K-Folds'
    n=10; folds_index = cv_yx(y, n)
    S_MSE = 0; M_MSE = 0
    content = ''
    for i in range(n):
        content += ' r'+str(i)+'->'
        fold=folds_index[i]
        y_train, X_train = y[fold[0]], X[fold[0]]
        content += '>'+str(len(y_train))
        y_test, X_test = y[fold[1]], X[fold[1]]
        content += '<'+str(len(y_test))
        'Train and Test'
        model, sy, sX = reg_train(y_train, X_train)
        MSE = reg_test(y_test, X_test, model, sy, sX)
        S_MSE += MSE
    M_MSE = S_MSE / n
    content += '\nMean MSE = '+str(round(M_MSE, 4))+'\n'
    return content, M_MSE
###
def cvreg_yx():
    'Logfile'
    logfile = './Logs/cvreg/cv_'+logtime+'.txt'
    'Pre Data'
    DS = pre_yx()
    y = DS['target']; X = DS['features']
    ''
    MSEs = []
    feas_number = len(X[0])
    content =''
    for i in range(feas_number):
        content += 'FeaSet->'+str(i+1)
        X_slice = []
        for j in range(i+1):
            X_slice.append(X.T[j])
        X_slice = np.array(X_slice).T
        cv_content, M_MSE = reg_yx(y, X_slice)
        content += cv_content
        MSEs.append(M_MSE)
    with open(logfile, 'w+') as f:
        f.write(content)
    'Get Feas Name'
    names = DS['fea_names']
    min_index = MSEs.index(min(MSEs))
    best_feas = []
    for i in range(min_index):
        best_feas.append(names[i])
    with open(logfile, 'a+') as f:
        f.write('Best Number: '+str(min_index+1)+'\n')
        f.write(str(best_feas))
    'plt'
    fig, ax = plt.subplots()
    ax.plot(range(1,len(MSEs)+1), MSEs, 'k--', lw=4)
    ax.set_xlabel('Feas Number')
    ax.set_ylabel('Mean MSE')
    ax.set_title('FeaSet Determine')
    plt.savefig('./Logs/cvreg/'+'fd'+'.png', bbox='tight')
###
def plt_yx(note, y, y_p):
    'plt'
    fig, ax = plt.subplots()
    ax.scatter(y, y_p, edgecolors=(0, 0, 0))
    ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    ax.set_title('Ea v.s. E_('+note+')')
    plt.savefig('./Logs/reg/'+note+'.png', bbox='tight')
###
if __name__ == '__main__':
    'total feastures 8454'
    cvreg_yx()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: PercenLas.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
'System'
import os

'SciLibs'
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import Lasso

'MPI'
from mpi4py import MPI

'MyLibs'
from DataOps import timer
from DataOps import GetDS
from DataOps import StdScaler
from DataOps import RanFolds

@timer
def LasCV(y, X, kfold, alphas):
    def TrainAndTest(y_train, X_train, \
            y_test, X_test, \
            las, a=0.01):
        'Scaler Use the Train Scaler\
                That is why i dont use cross_validate'
        y_train_s, X_train_s, sy, sX = StdScaler(y_train, X_train)

        'Lasso for TrainSet'
        las = Lasso(alpha=a, fit_intercept=True, normalize=False, \
                max_iter=10000, random_state=None, selection='random')
        las.fit(X_train_s, y_train_s)

        'Predict on TestSet'
        y_test_s = sy.transform(y_test); X_test_s = sX.transform(X_test)
        y_test_p = las.predict(X_test_s)
        MSE = metrics.mean_squared_error(y_test_s, y_test_p)

        return MSE

    def CalcMeanMSE(MSEs):
        'Mean-MSE'
        MSEs = np.array(MSEs)
        n_MSE = len(MSEs)
        sum_MSE = MSEs.sum()
        mean_MSE = sum_MSE / n_MSE
        
        return mean_MSE

    'LasCV'
    MeanMSEs = [] 
    #alphas = np.linspace(0.01, 1, 100)
    for a in alphas:
        a_MSEs = []
        for i in range(len(kfold)):
            'Get train and test set'
            train_index = kfold[i][0]
            test_index = kfold[i][1]
            y_train, X_train = y[train_index], X[train_index]
            y_test, X_test = y[test_index], X[test_index]
            
            'Train and Test'
            a_MSE = TrainAndTest(y_train, X_train, \
                    y_test, X_test, a)
            a_MSEs.append(a_MSE)

        MeanMSEs.append(CalcMeanMSE(a_MSEs))

    'Get Best, having same aloha is fine.'
    best_index = MeanMSEs.index(min(MeanMSEs)) 
    best_alpha = alphas[best_index]

    'Here y and X are original data, which should be std.'
    y_s, X_s, s4y, s4X= StdScaler(y, X)

    best_las = Lasso(alpha=a, fit_intercept=True, normalize=False, \
            max_iter=10000, random_state=None, selection='random')
    best_las.fit(X_s, y_s)
    r2_score = round(best_las.score(X_s, y_s), 2)

    coefs = best_las.coef_
    pos_coefs = []
    for coef in coefs:
        if abs(coef) > 0:
            pos_coefs.append(coef)

    n_poscoef = len(pos_coefs)

    outs = ''
    outs += 'LasCV --> BestAlpha: ' + str(best_alpha) + '\n'
    outs += 'OneShot --> BestR2Score: ' + str(r2_score) + '\n'
    outs += 'OneShot --> N_PosCoefs: ' + str(n_poscoef) + '\n'

    return best_alpha, outs

from Params import Etype
from Params import cv_splits
from Params import cv_repeats
from Params import test_alphas
@timer
def PercenLas():
    'Init MPI'
    comm = MPI.COMM_WORLD
    comm_rank = comm.Get_rank()
    comm_size = comm.Get_size()
    
    'Get DS'
    DS = GetDS(Etype)
    y = DS['target']; X = DS['features']

    'Print Initial Setting and Scatter Folds'
    if comm_rank == 0:
        print('<- Percentile-LASSO Setting ->')
        print('Processing Data --> %s' %Etype)
        print('K-Folds Setting --> splits: %d repeats: %d' \
                %(cv_splits, cv_repeats))
        print('TestAlphs --> From %f to %f Total %d' \
                %(test_alphas[0], test_alphas[-1], len(test_alphas)))

        print('<- Generating %d [%d-Fold]s ->' %(cv_repeats, cv_splits))
        # folds is a dict, {1:fold}
        folds = RanFolds(y, splits=cv_splits, repeats=cv_repeats)

        folds_list = []
        for number, fold in folds.items():
            folds_list.append([number, fold])
        print(folds_list)

        folds_scatter = []
        folds_num = len(folds.keys())
        n = int(folds_num/comm_size)
        for i in range(comm_size):
            if i*n+n < n*comm_size:
                start, end = i*n, i*n+n
                folds_scatter.append(folds_list[start:end])
            else:
                start = i*n
                folds_scatter.append(folds_list[start:])
    else:
        folds_scatter = None

    'Process Folds'
    print('*'*20+'\n<- Slot'+str(comm_rank)+' Percentile-LASSO Start->\n'+'*'*20)
    # Check SlotsFile
    for slotfile in os.listdir('./'):
        if 'slot' in slotfile:
            print('%s is removed.' %slotfile)
            os.remove(slotfile)

    local_folds = comm.scatter(folds_scatter, root=0)

    best_alphas = []
    for num_fold in local_folds: 
        num = num_fold[0]
        fold = num_fold[1]
        outs = ''
        outs += '-'*20 + '\n'
        outs += 'Fold <%d>' %(num) + '\n'
        best_alpha, las_outs = LasCV(y, X, fold, test_alphas)
        print('%d Best_Alpha %f' %(num, best_alpha))
        outs += las_outs
        best_alphas.append(best_alpha)
        outs += '-'*20 + '\n'
        with open('./slot'+str(comm_rank)+'_outs', 'a') as f:
            f.write(outs)
    print('*'*20+'\n<- Slot'+str(comm_rank)+' Percentile-LASSO Done->\n'+'*'*20)

if __name__ == '__main__':
    PercenLas()

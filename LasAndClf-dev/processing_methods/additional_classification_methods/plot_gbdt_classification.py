#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import os
import time

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  

import numpy as np
import pandas as pd

from sklearn import preprocessing
from sklearn import tree
from sklearn.ensemble import GradientBoostingClassifier 
from sklearn.model_selection import GridSearchCV 


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


def plot_gbdt_classification():
    # feature names 
    feanames = ['E_CH3ab', 'E_Hab3', \
            'a_O2-M4-C_CH3ab', 'h_O2-C-M4-H1_CH3ab', 'd_H1-C_CH3ab', \
            'h_O2-H1-M4-C_CH3ab', 'a_O2-M4-H1_Hab3'] 
    '''
    feanames = ['a_O2-M4-C_CH3ab', 'h_O2-C-M4-H1_CH3ab', 'd_H1-C_CH3ab', \
            'h_O2-H1-M4-C_CH3ab', 'a_O2-M4-H1_Hab3'] 
    '''

    # prepare dataset 
    #DS = generate_dataset_from_csv('Eclf', feanames)
    DS = generate_dataset_from_csv('Eclf')

    # get labels 
    labels = DS['Etype'].tolist() # label list

    lb = preprocessing.LabelBinarizer()
    y = lb.fit_transform(labels).ravel() 

    feavals = DS['features']
    X = np.array(feavals.tolist())


    clf = GradientBoostingClassifier(n_estimators=100, random_state=0)
    params = {'max_depth': [1,3,5], 'learning_rate': [5, 2, 1, 0.6, 0.4, 0.2, 0.1]}
    gs = GridSearchCV(clf, params, cv=5)
    gs.fit(X, y)
    #print(gs.best_params_)
    print(gs.cv_results_)

    clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.4, \
            max_depth=1, random_state=0)
    clf.fit(X, y)

    for name, coef in zip(DS['fea_names'], clf.feature_importances_):
        if np.fabs(coef) > 1e-6:
            print('%s: %.2f' %(name, coef))

def plot_dbdt_classification():
    fig, ax = plt.subplots(1, 2, figsize=(16,6))
    plt.suptitle('Classification for Methane Activation')
    plt.tight_layout(pad=2.0, w_pad=4.0, h_pad=2.0)
    plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=0.90, \
            wspace=None, hspace=0.5)



if __name__ == '__main__':
    DS_CSV = './CH4_3.csv'
    plot_gbdt_classification() 

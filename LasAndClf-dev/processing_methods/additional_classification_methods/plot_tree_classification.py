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
from sklearn.preprocessing import StandardScaler


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


def plot_tree_classification():
    # feature names 
    '''
    feanames = ['E_CH3ab', 'E_Hab3', \
            'a_O2-M4-C_CH3ab', 'h_O2-C-M4-H1_CH3ab', 'd_H1-C_CH3ab', \
            'h_O2-H1-M4-C_CH3ab', 'a_O2-M4-H1_Hab3'] 
    '''
    feanames = ['a_O2-M4-C_CH3ab', 'h_O2-C-M4-H1_CH3ab', 'd_H1-C_CH3ab', \
            'h_O2-H1-M4-C_CH3ab', 'a_O2-M4-H1_Hab3'] 

    # prepare dataset 
    DS = generate_dataset_from_csv('Eclf', feanames)

    # get labels 
    labels = DS['Etype'].tolist() # label list

    lb = preprocessing.LabelBinarizer()
    y = lb.fit_transform(labels)

    feavals = DS['features']
    X = np.array(feavals.tolist())

    # classification 
    clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3, min_samples_leaf=1) #创建一个分类器，entropy决定了用ID3算法
    clf = clf.fit(X, y)
    
    # visualization 
    treefile = './tree.txt'
    tree.export_graphviz(clf, feature_names=DS['fea_names'], class_names=['ss', 'ra'], out_file = treefile)

    os.system(r'dot -Tpdf %s -o %s.png' %(treefile, os.path.basename(treefile)))

    # model settings 
    clf_params = clf.get_params()
    clf_params['Score'] = round(clf.score(X,y), 8)


if __name__ == '__main__':
    DS_CSV = './CH4_3.csv'
    plot_tree_classification() 

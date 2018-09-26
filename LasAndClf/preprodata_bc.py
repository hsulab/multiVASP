#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: preprodata.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 二  15/09/2018
#########################################################################
import os
import time
###
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  
import numpy as np
import pandas as pd
import seaborn as sns  
### import sklearn
from sklearn import preprocessing
from sklearn.decomposition import PCA
###
def get_ch3ab(data_path, numbers):
    ###
    for csv_name in os.listdir(data_path):
        if 'CH3ab' in csv_name:
            ch3ab_csv_name = csv_name
    ch3ab_csv = os.path.join(data_path, ch3ab_csv_name)
    ch3ab = pd.read_csv(ch3ab_csv, index_col=0)
    ###
    para_numbers = len(ch3ab.columns) - 3
    print('ch3ab has '+str(para_numbers)+' parameters.')
    para_list = []
    for i in range(3, para_numbers):
        para_list.append(ch3ab.columns[i])
    ###
    para_cols = [0]
    for i in range(3, numbers+3):
        para_cols.append(i)
    return ch3ab.iloc[:, para_cols]
###
def get_E(data_path, params):
    for csv_name in os.listdir(data_path):
        if 'rE' in csv_name:
            rE_csv_name = csv_name
    rE_csv = os.path.join(data_path, rE_csv_name)
    rE = pd.read_csv(rE_csv, index_col=0)
    para_numbers = len(rE.columns)
    para_list = ['name'] + list(params)
    return rE.loc[:, para_list]
###
def apply_pca(comps):
    ###
    data_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    ###
    ch3ab = get_ch3ab(data_path, comps)
    ###
    rE = get_E(data_path, ['E_CH3ab'])
    ###
    pca_input = pd.merge(rE, ch3ab, on='name').iloc[:,range(1, 2+comps)].values.astype(float)
    ###
    pca = PCA(n_components=comps+1)
    newX = pca.fit_transform(pca_input)
    print(newX)
    var_ratios = np.around(pca.explained_variance_ratio_, decimals=2)
    print(var_ratios, len(var_ratios))
###
if __name__ == '__main__':
    apply_pca(2)

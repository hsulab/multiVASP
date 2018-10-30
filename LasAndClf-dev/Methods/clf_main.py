#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: clf_main.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
import os
import sys
import time
### plot
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  
### scilibs
import numpy as np
import pandas as pd
import pickle
'sklearn'
from sklearn import preprocessing
from sklearn import tree
from sklearn.preprocessing import StandardScaler
### mylibs
sys.path.append('..')
import decorates as deco
###
def pre_yx():
    'Load'
    with open('../Las/Log/BestReg.pk', 'rb') as f:
        n_feas, best_feas, mean_MSEs, std_MSEs = pickle.load(f)

    'Get Total DataSet'
    df = pd.read_csv('../CH4_DataSet.csv', index_col = 0)

    'Get index and values'
    yx_indexs = df.iloc[:,range(4)] # 'name', 'mtype', 'E_ts', 'E_tsra'
    yx_vals = df.loc[:, best_feas] # E and Geo

    'Get DataSet'
    DS = {}
    DS['name'] = yx_indexs.iloc[:,range(1)].values
    DS['mtype'] = yx_indexs.iloc[:,range(1,2)].values
    #DS['target'] = df.loc[:, 'mE'].values # mE
    DS['features'] = yx_vals.values
    DS['fea_names'] = best_feas
    return DS
###
def clf_yx():
    'Pre DataSet'
    DS = pre_yx()

    'Get Labels'
    mtype = DS['mtype'].tolist() # label list
    labels = []
    for m in mtype:
        for m_ in m:
            labels.append(m_)
    lb = preprocessing.LabelBinarizer()
    y = lb.fit_transform(labels)

    'Get features'
    feas = DS['features']
    X = np.array(feas.tolist())

    'Clf and VisTree'
    #using desicionTree for classfication
    clf = tree.DecisionTreeClassifier(criterion="entropy", min_samples_leaf=5) #创建一个分类器，entropy决定了用ID3算法
    clf = clf.fit(X, y)
    #Visulize model
    logtime = time.strftime("%m%d")
    tree_file = './Log/tree_' + logtime
    with open("./"+tree_file+".txt","w") as f:
        f = tree.export_graphviz(clf, feature_names=DS['fea_names'], class_names=['ss', 'ra'], out_file = f)
    os.system(r'dot -Tpdf ./'+tree_file+'.txt -o ./'+tree_file+'.png')

###
if __name__ == '__main__':
    'total feastures 8454'
    clf_yx()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: clf_main.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
import os
import time
### plot
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  
### scilibs
import numpy as np
import pandas as pd
'sklearn'
from sklearn import preprocessing
from sklearn import tree
from sklearn.preprocessing import StandardScaler
### mylibs
import readlog as rl
import collectdata as cd
import decorates as deco
###
def pre_yx():
    'Get Total DataSet and Top Features'
    cvreg_log = './Logs/cvreg/cv_20181009.txt'
    df = pd.read_csv('./CH4_DataSet.csv', index_col = 0)
    with open(cvreg_log, 'r') as f:
        content = f.readlines()
        feas_tuple = eval(content[-1])
    feas_col = []
    for i in feas_tuple:
        feas_col.append(i[0])
    'Get index and values'
    yx_indexs = df.iloc[:,range(4)] # 'name', 'mtype', 'E_ts', 'E_tsra'
    yx_vals = df.loc[:, feas_col] # E and Geo
    'Get DataSet'
    DS = {}
    DS['name'] = yx_indexs.iloc[:,range(1)].values
    DS['mtype'] = yx_indexs.iloc[:,range(1,2)].values
    DS['target'] = df.loc[:, 'mE'].values # mE
    DS['features'] = yx_vals.values
    DS['fea_names'] = feas_col 
    return DS
###
logtime = time.strftime("%Y%m%d")
@deco.printer(r'./Logs/clf/clf_'+logtime+'.txt', 'out')
def clf_yx():
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
    clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=1, min_samples_leaf=5) #创建一个分类器，entropy决定了用ID3算法
    clf = clf.fit(X, y)
    #Visulize model
    tree_file = './Logs/clf/tree_' + logtime
    with open("./"+tree_file+".txt","w") as f:
        f = tree.export_graphviz(clf, feature_names=DS['fea_names'], class_names=['ss', 'ra'], out_file = f)
    os.system(r'dot -Tpdf ./'+tree_file+'.txt -o ./'+tree_file+'.png')
    'Model Settings'
    clf_params = clf.get_params()
    clf_params['Score'] = round(clf.score(X,y), 8)
    'Coef and Feas'
    fea_coef = {}
    return clf_params, fea_coef
###
if __name__ == '__main__':
    'total feastures 8454'
    clf_yx()

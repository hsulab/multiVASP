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
def pre_yx(n_top):
    'Get Total DataSet and Top Features'
    las = './Logs/las_20181006.txt'
    df = pd.read_csv('./CH4_DataSet.csv', index_col = 0)
    feas_top = rl.read_las(las, n_top) # dict
    feas_col = []
    for key in feas_top.keys():
        feas_col.append(key)
    'Get index and values'
    yx_indexs = df.iloc[:,range(2)] # 'name' and 'mtype'
    yx_vals = df.loc[:, feas_col] # E and Geo
    'Get DataSet'
    DataSet = {}
    DataSet['name'] = yx_indexs.iloc[:,range(1)]
    DataSet['mtype'] = yx_indexs.iloc[:,range(1,2)]
    DataSet['target'] = yx_vals.iloc[:,range(1)].values # mE
    DataSet['features'] = yx_vals.values
    DataSet['fea_names'] = feas_col 
    return DataSet
###
logtime = time.strftime("%Y%m%d")
@deco.printer(r'./Logs/clf_'+logtime+'.txt', 'out')
def clf_yx(n_top):
    DS = pre_yx(n_top)
    print(DS['features'])
    'Get Labels'
    mtype = DS['mtype'].values.tolist() # label list
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
    clf = tree.DecisionTreeClassifier(criterion="entropy") #创建一个分类器，entropy决定了用ID3算法
    clf = clf.fit(X, y)
    #Visulize model
    tree_file = 'tree_' + logtime
    with open("./"+tree_file+".txt","w") as f:
        f = tree.export_graphviz(clf, feature_names=DS['fea_names'], out_file = f)
    os.system(r'dot -Tpdf ./'+tree_file+'.txt -o ./'+tree_file+'.pdf')
    'Model Settings'
    clf_params = clf.get_params()
    clf_params['Score'] = round(clf.score(X,y), 8)
    'Coef and Feas'
    fea_coef = {}
    return clf_params, fea_coef
###
if __name__ == '__main__':
    'total feastures 8454'
    clf_yx(5)

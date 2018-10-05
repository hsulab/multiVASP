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
from sklearn.externals.six import StringIO
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
    DataSet['mtype'] = yx_indexs.iloc[:,range(1,2)]
    DataSet['target'] = yx_vals.iloc[:,range(1)].values
    DataSet['features'] = yx_vals.iloc[:,range(1,len(yx_vals.columns))].values
    DataSet['fea_names'] = yx_vals.columns[1:]
    return DataSet
###
def clf_yx(n_geofeas):
    DS = pre_yx(n_geofeas)
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
    #using desicionTree for classfication
    clf = tree.DecisionTreeClassifier(criterion="entropy") #创建一个分类器，entropy决定了用ID3算法
    clf = clf.fit(X, y)
    #Visulize model
    with open("./hehe.txt","w") as f:
        f = tree.export_graphviz(clf, feature_names=DS['fea_names'], out_file = f)
    os.system(r'dot -Tpdf ./hehe.txt -o ./hehe.pdf')
###
if __name__ == '__main__':
    'total feastures 8454'
    clf_yx(5)

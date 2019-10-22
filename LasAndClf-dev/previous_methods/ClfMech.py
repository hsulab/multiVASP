#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
#########################################################################
# File Name: clf_main.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
'System'
import os
import sys
import time

'Plot'
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  

'SciLibs'
import numpy as np
import pandas as pd
import pickle

'SkLearn'
from sklearn import preprocessing
from sklearn import tree
from sklearn.preprocessing import StandardScaler

'MyLibs'
import decorates as deco
from DataOperators import GetDS
from DataOperators import pkload

def print_dict(d):
    count1 = {'Energy':0, 'Distance':0, 'Angle':0}
    count2 = {'Surface':0, 'H-Adsorption':0, 'CH3-Adsorption':0}
    for name, coef in d.items():
        print(name, ' --> ', round(coef, 4))
        name = name.split('_')
        if name[0] == 'E':
            count1['Energy'] += 1
        elif name[0] == 'd':
            count1['Distance'] += 1
        elif name[0] == 'a':
            count1['Angle'] += 1

        if name[-1] == 'suf':
            count2['Surface'] += 1
        elif name[-1] == 'Hab3':
            count2['H-Adsorption'] += 1
        elif name[-1] == 'CH3ab':
            count2['CH3-Adsorption'] += 1

    print(count1)
    print(count2)

def clf_yx():
    'Load Lasso Results'
    ts_las, ts_nc = pkload('Ets_final.pk')
    print('--Ets--')
    print_dict(ts_nc)
    tsra_las, tsra_nc = pkload('Etsra_final.pk')
    print('--Etsra--')
    print_dict(tsra_nc)

def asds():
    fea_names = list(set(list(ts_nc.keys())+list(tsra_nc.keys())))
    fea_names.remove('E_CH3ab')
    fea_names.remove('E_Hab3')

    'Pre DataSet'
    DS = GetDS('Ea', fea_names)

    'Get Labels'
    mtypes = DS['Etype'].tolist() # label list
    lb = preprocessing.LabelBinarizer()
    y = lb.fit_transform(mtypes)

    'Get features'
    feas = DS['features']
    X = np.array(feas.tolist())

    'Clf and VisTree'
    #using desicionTree for classfication
    clf = tree.DecisionTreeClassifier(criterion="entropy", min_samples_leaf=5) #创建一个分类器，entropy决定了用ID3算法
    clf = clf.fit(X, y)

    #Visulize model
    tree_file = './Pics/tree'
    with open("./"+tree_file+".txt","w") as f:
        f = tree.export_graphviz(clf, feature_names=DS['fea_names'], class_names=['ss', 'ra'], out_file = f)

    os.system(r'dot -Tpdf ./'+tree_file+'.txt -o ./'+tree_file+'.png')

###
if __name__ == '__main__':
    'total feastures 8454'
    clf_yx()

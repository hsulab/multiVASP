#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: main_lasso.py
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
from sklearn.linear_model import Lasso,LassoCV,LassoLarsCV
### mylibs
import collectdata as cd
###
def prepro(feas):
    df = cd.get_data(feas)
    #df.loc[:, 'test'] = 100
    #df.loc[df.loc[:, 'mE'] > 0.1, 'test'] = np.nan
    yx_indexs = df.iloc[:,range(2)]
    yx_vals = df.iloc[:,range(2,len(df.columns))]
    return yx_indexs, yx_vals
    #print(df)
    #print(np.where(np.isnan(yx_df)))
    #print(df.index[np.where(np.isnan(yx_df))[0]])
###
def daya_lasso(nums, outs=1):
    ### X and y
    yx_indexs, yx_vals = prepro(nums)
    y = yx_vals.iloc[:,range(1)]
    X = yx_vals.iloc[:,range(1,len(yx_vals.columns))]
    # ========Lasso回归========
    start_time = time.time()
    ''
    model = Lasso(alpha=0.01)  # 调节alpha可以实现对拟合的程度
    model.fit(X, y)   # 线性回归建模
    end_time = time.time()
    take_time = end_time - start_time
    ''
    ###
    feas = {}
    for i in range(len(list(model.coef_))):
        cof = list(model.coef_)[i]
        feas[yx_vals.columns[i+1]] = cof
    ##
    with open('./features.txt', 'w+') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n')
        f.write('{:<20}{:<20} s\n'.format('Cpu Time',take_time))
        f.write('Model Parameters: \n')
        count = 1
        for param, value in model.get_params().items():
            content = '{:<15}{:^5}{:<15}'.format(str(param),'-->',str(value))
            f.write(content)
            if count % 2 == 0:
                f.write('\n')
            else:
                f.write(' '*10)
            count += 1
        f.write('\nFeatures and Coefficients: \n')
        for fea, cof in feas.items():
            content = '{:<30}{:^5}{:<20}\n'.format(str(fea),'-->',str(cof))
            f.write(content)
    ###
    print('Finished.')
    if outs == 1:
        with open('./features.txt', 'r') as f:
            content = f.readlines()
            for i in range(len(content)):
                print(content[i], end='')
###
if __name__ == '__main__':
    daya_lasso(10)

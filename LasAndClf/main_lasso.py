#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: main_lasso.py
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 六  9/22 22:34:17 2018
#########################################################################
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
def main():
    df = cd.get_data(4)
    df.loc[:, 'test'] = 100
    df.loc[df.loc[:, 'E_ts'] > 0.1, 'test'] = np.nan
    print(df.index[np.where(np.isnan(df))[0]])
###
def daya_lasso():
    di_val = ppd.get_data(10000).values.astype(float)
    y = di_val[:, 1]
    X = di_val[:,range(1,di_val.shape[1])]
    # ========Lasso回归========
    model = Lasso(alpha=0.01)  # 调节alpha可以实现对拟合的程度
    #model = LassoCV()  # LassoCV自动调节alpha可以实现选择最佳的alpha。
    # model = LassoLarsCV()  # LassoLarsCV自动调节alpha可以实现选择最佳的alpha
    model.fit(X, y)   # 线性回归建模
    print('系数矩阵:\n',model.coef_, type(model.coef_))
    print('线性回归模型:\n',model)
    # print('最佳的alpha：',model.alpha_)  # 只有在使用LassoCV、LassoLarsCV时才有效
    # 使用模型预测
    features = []
    for cof in list(model.coef_):
        if cof>0:
            features.append([cof, list(model.coef_).index(cof)])
    ##
    with open('./features.txt', 'w') as f:
        for feature in features:
            f.write(str(feature))
    ###
    print('Finished.')
###
if __name__ == '__main__':
    main()
